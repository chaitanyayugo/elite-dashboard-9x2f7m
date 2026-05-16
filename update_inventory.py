import os
import sys
import json
from datetime import datetime, timezone
import xmlrpc.client

# ─────────────────────────────────────────────────────────────
# CONFIGURATION FROM SECURE ENVIROMENT
# ─────────────────────────────────────────────────────────────
ODOO_URL      = os.environ.get("ODOO_URL")
ODOO_DB       = os.environ.get("ODOO_DB")
ODOO_USER     = os.environ.get("ODOO_USER")
ODOO_PASSWORD = os.environ.get("ODOO_PASSWORD")
LOW_STOCK_THRESHOLD = 5

QTY_FIELD_CANDIDATES = [
    "x_avl_custom",
    "x_studio_related_field_6v_1jolles4p",
    "qty_available",
]

print("🟢 Initializing Cloud Data Engine via Odoo API...", flush=True)

# Connect to Odoo Server
try:
    common = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/common")
    uid = common.authenticate(ODOO_DB, ODOO_USER, ODOO_PASSWORD, {})
    models = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/object")
except Exception as e:
    print(f"❌ Odoo API connection error: {e}")
    sys.exit(1)

# Check which field is active in your database fields list
fields_info = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'product.product', 'fields_get', [], {'attributes': ['string']})
qty_field = next((f for f in QTY_FIELD_CANDIDATES if f in fields_info), "qty_available")

# Fetch all items matching stock boundaries
all_products = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'product.product', 'search_read', 
    [[[qty_field, '<', LOW_STOCK_THRESHOLD]]], 
    {'fields': ['id', 'name', 'default_code', 'categ_id', qty_field], 'limit': 2500}
)

# 🗺️ MAP DATA ARRAYS INTO HIGH-PERFORMANCE DATA OBJECTS
web_products = []
for p in all_products:
    qty = float(p.get(qty_field) or 0)
    if qty == 0:
        status, color_cls = "OUT OF STOCK", "bg-red-950/60 text-red-400 border-red-800/60"
        is_archived = True
    elif qty <= 2:
        status, color_cls = f"{qty:g} CRITICAL", "bg-orange-950/60 text-orange-400 border-orange-800/60"
        is_archived = False
    else:
        status, color_cls = f"{qty:g} LOW STOCK", "bg-amber-950/60 text-amber-500 border-amber-800/60"
        is_archived = False
        
    full_path = p["categ_id"][1] if p.get("categ_id") else "General"
    image_url = f"{ODOO_URL}/web/image/product.product/{p['id']}/image_128"
    product_link = f"{ODOO_URL}/web#id={p['id']}&model=product.product&view_type=form"

    web_products.append({
        "id": p["id"],
        "name": p["name"] or "Unnamed Product",
        "sku": p.get("default_code") or "N/A",
        "qty": qty,
        "status": status,
        "colorClass": color_cls,
        "category": full_path,
        "image": image_url,
        "link": product_link,
        "archived": is_archived
    })

json_products = json.dumps(web_products)
generated_at = datetime.now(timezone.utc).strftime("%d %b %Y %H:%M UTC")

# 📄 BUILD FRONTEND APP ENVELOPE (Tailwind Engine + AlpineJS View Control)
html_dashboard = f"""<!DOCTYPE html>
<html lang="en" class="h-full bg-[#04040a] text-slate-100">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elite Dashboard — Live Stock</title>
    <script src="https://tailwindcss.com"></script>
    <script defer src="https://jsdelivr.net"></script>
</head>
<body class="h-full font-sans antialiased bg-[#04040a]">
    <div class="min-h-full flex flex-col" x-data="{{ 
        products: {json_products},
        currentTab: 'all',
        searchQuery: '',
        categoryFilter: 'all',
        get filteredProducts() {{
            return this.products.filter(p => {{
                const matchesSearch = p.name.toLowerCase().includes(this.searchQuery.toLowerCase()) || p.sku.toLowerCase().includes(this.searchQuery.toLowerCase());
                const matchesCat = this.categoryFilter === 'all' || p.category === this.categoryFilter;
                let matchesTab = true;
                if (this.currentTab === 'low') matchesTab = (p.qty > 0);
                else if (this.currentTab === 'archived') matchesTab = (p.archived === true);
                return matchesSearch && matchesCat && matchesTab;
            }});
        }},
        get uniqueCategories() {{ return [...new Set(this.products.map(p => p.category))].sort(); }},
        get counts() {{
            return {{ all: this.products.length, low: this.products.filter(p => p.qty > 0).length, archived: this.products.filter(p => p.archived).length }};
        }}
    }}">
        <header class="border-b border-[#c9a84c]/20 bg-[#0d0d1a]/80 backdrop-blur sticky top-0 z-50 px-4 py-4">
            <div class="max-w-7xl mx-auto flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
                <div>
                    <h1 class="text-xl font-bold tracking-wider text-[#f0e6c8] uppercase">🔱 Elite Dashboard</h1>
                    <p class="text-[11px] text-slate-400 mt-1">Synced: {generated_at} • System Limit: &lt; {LOW_STOCK_THRESHOLD} Units</p>
                </div>
                <div class="flex flex-wrap items-center gap-3 w-full lg:w-auto">
                    <input type="text" x-model="searchQuery" placeholder="Search SKU or Name..." class="bg-[#04040c] border border-[#c9a84c]/20 px-3 py-2 rounded-lg text-xs" />
                    <select x-model="categoryFilter" class="bg-[#04040c] border border-[#c9a84c]/20 px-3 py-2 rounded-lg text-xs text-slate-300">
                        <option value="all">All Categories</option>
                        <template x-for="cat in uniqueCategories" :key="cat"><option :value="cat" x-text="cat"></option></template>
                    </select>
                </div>
            </div>
            <div class="max-w-7xl mx-auto mt-4 flex border-b border-slate-800 text-xs">
                <button @click="currentTab = 'all'" :class="currentTab === 'all' ? 'border-[#c9a84c] text-[#e8c96d]' : 'border-transparent text-slate-400'" class="py-2 px-4 border-b-2">All Alerts (<span x-text="counts.all"></span>)</button>
                <button @click="currentTab = 'low'" :class="currentTab === 'low' ? 'border-[#c9a84c] text-[#e8c96d]' : 'border-transparent text-slate-400'" class="py-2 px-4 border-b-2">Active Low Stock (<span x-text="counts.low"></span>)</button>
                <button @click="currentTab = 'archived'" :class="currentTab === 'archived' ? 'border-[#c9a84c] text-[#e8c96d]' : 'border-transparent text-slate-400'" class="py-2 px-4 border-b-2">Archived / Out (<span x-text="counts.archived"></span>)</button>
            </div>
        </header>
        <main class="flex-1 max-w-7xl w-full mx-auto px-4 py-6">
            <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-6 gap-4">
                <template x-for="product in filteredProducts" :key="product.id">
                    <div class="rounded-xl border border-slate-900 bg-[#08080f] p-3 flex flex-col hover:border-[#c9a84c]/40 transition-all">
                        <div class="aspect-square bg-[#0a0a12] rounded-lg flex items-center justify-center overflow-hidden">
                            <img :src="product.image" loading="lazy" class="h-full w-full object-contain" @error="$el.style.display='none'; $el.nextElementSibling.style.display='flex';" />
                            <div style="display:none;" class="w-full h-full items-center justify-center bg-slate-900 text-amber-500 font-bold" x-text="product.name.charAt(0)"></div>
                        </div>
                        <div class="flex flex-col flex-1 mt-2">
                            <p class="text-[9px] text-slate-500 font-mono font-bold" x-text="product.sku"></p>
                            <h3 class="text-xs font-semibold text-slate-200 truncate" x-text="product.name"></h3>
                            <p class="text-[10px] text-[#c9a84c]/60 truncate" x-text="product.category"></p>
                            <div class="mt-auto pt-2 flex items-center justify-between border-t border-slate-900">
                                <span class="rounded-full border px-2 py-0.5 text-[8px] font-bold" :class="product.colorClass" x-text="product.status"></span>
                                <a :href="product.link" target="_blank" class="text-[10px] text-[#e8c96d] font-bold">Odoo ↗</a>
                            </div>
                        </div>
                    </div>
                </template>
            </div>
        </main>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_dashboard)
print("✅ Dashboard index.html updated successfully.")
