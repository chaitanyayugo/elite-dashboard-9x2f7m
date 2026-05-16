import os
import sys
import json
import base64
import requests
from datetime import datetime, timezone

# ─────────────────────────────────────────────────────────────
#  ELITE GITHUB PAGES CONFIGURATION
# ─────────────────────────────────────────────────────────────
# Ensure GITHUB_TOKEN is set in your environment variables.
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO  = "elite-dashboard-9x2f7m"
# Extract owner dynamically from user environment or token profile if needed, 
# or set an explicit fallback environment variable.
GITHUB_OWNER = os.environ.get("GITHUB_OWNER", "your-github-username")
GITHUB_BRANCH = os.environ.get("GITHUB_BRANCH", "main")

# [The connection to Odoo and initial data filtering loops from lines 770-828 remain intact]

print("📊 Transitioning to Elite Dashboard pipeline...", flush=True)

# 🗺️ 1. CONVERT DATA ARRAYS INTO HIGH-PERFORMANCE DATA OBJECTS
web_products = []
for p in all_products:
    qty = float(p.get(qty_field) or 0)
    
    # Process distinct operational indicators and color states
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
    
    # Isolate subcategory structure cleanly using your regex mapping definitions
    sub_name = subcateg_name(p) or "General"
    
    # Live Image Controller Links — Bypasses Base64 binary attachment loads
    image_url = f"{ODOO_URL}/web/image/product.product/{p['id']}/image_128"
    product_link = f"{ODOO_URL}/web#id={p['id']}&model=product.product&view_type=form"

    web_products.append({
        "id": p["id"],
        "name": p["name"] or "Unnamed Product",
        "sku": p.get("default_code") or "N/A",
        "qty": qty,
        "status": status,
        "colorClass": color_cls,
        "category": sub_name,
        "image": image_url,
        "link": product_link,
        "archived": is_archived
    })

json_products = json.dumps(web_products)
generated_at = datetime.now(timezone.utc).strftime("%d %b %Y %H:%M UTC")

# 📄 2. CORE INTERFACE ARCHITECTURE (Tailwind Engine + AlpineJS View Control)
html_dashboard = f"""<!DOCTYPE html>
<html lang="en" class="h-full bg-[#04040a] text-slate-100">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elite Dashboard — Live Stock</title>
    <script src="https://tailwindcss.com"></script>
    <script defer src="https://jsdelivr.net"></script>
    <style>
        .custom-scrollbar::-webkit-scrollbar {{ width: 6px; height: 6px; }}
        .custom-scrollbar::-webkit-scrollbar-track {{ background: #04040a; }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{ background: #1e1e2f; border-radius: 4px; }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{ background: #c9a84c; }}
    </style>
</head>
<body class="h-full font-sans antialiased custom-scrollbar">

    <div class="min-h-full flex flex-col" x-data="{{ 
        products: {json_products},
        currentTab: 'all',
        searchQuery: '',
        categoryFilter: 'all',
        
        get filteredProducts() {{
            return this.products.filter(p => {{
                const matchesSearch = p.name.toLowerCase().includes(this.searchQuery.toLowerCase()) || 
                                     p.sku.toLowerCase().includes(this.searchQuery.toLowerCase());
                const matchesCat = this.categoryFilter === 'all' || p.category === this.categoryFilter;
                
                let matchesTab = true;
                if (this.currentTab === 'low') {{
                    matchesTab = (p.qty > 0);
                }} else if (this.currentTab === 'archived') {{
                    matchesTab = (p.archived === true);
                }}
                
                return matchesSearch && matchesCat && matchesTab;
            }});
        }},
        
        get uniqueCategories() {{
            return [...new Set(this.products.map(p => p.category))].sort();
        }},
        
        get counts() {{
            return {{
                all: this.products.length,
                low: this.products.filter(p => p.qty > 0).length,
                archived: this.products.filter(p => p.archived).length
            }};
        }}
    }}">
        
        <!-- LUXURY DASHBOARD HEADER -->
        <header class="border-b border-[#c9a84c]/20 bg-[#0d0d1a]/80 backdrop-blur sticky top-0 z-50 px-4 py-4 sm:px-6 lg:px-8">
            <div class="max-w-7xl mx-auto flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
                <div>
                    <div class="flex items-center gap-3">
                        <div class="w-8 h-8 rounded-full bg-gradient-to-br from-[#1a1400] to-[#0a0a0f] border border-[#c9a84c]/60 flex items-center justify-center text-[#c9a84c] font-serif text-sm font-bold">🔱</div>
                        <h1 class="text-xl font-bold tracking-wider text-[#f0e6c8] font-serif uppercase">Elite Dashboard</h1>
                    </div>
                    <p class="text-[11px] text-slate-400 mt-1 font-mono">Synced: {generated_at} • System Limit: &lt; {LOW_STOCK_THRESHOLD} Units</p>
                </div>
                
                <!-- FILTERING MATRICES AND WORKSPACE INPUTS -->
                <div class="flex flex-wrap items-center gap-3 w-full lg:w-auto">
                    <div class="relative flex-1 min-w-[200px] lg:w-64">
                        <input type="text" x-model="searchQuery" placeholder="Search product name or SKU..." class="w-full bg-[#04040c] border border-[#c9a84c]/20 px-3 py-2 rounded-lg text-xs focus:outline-none focus:border-[#c9a84c] text-slate-200 placeholder-slate-500" />
                    </div>
                    
                    <select x-model="categoryFilter" class="bg-[#04040c] border border-[#c9a84c]/20 px-3 py-2 rounded-lg text-xs text-slate-300 focus:outline-none focus:border-[#c9a84c] max-w-[200px]">
                        <option value="all">All Categories</option>
                        <template x-for="cat in uniqueCategories" :key="cat">
                            <option :value="cat" x-text="cat"></option>
                        </template>
                    </select>
                </div>
            </div>
            
            <!-- SEGMENTED NAVIGATION TABS -->
            <div class="max-w-7xl mx-auto mt-4 flex border-b border-slate-800 text-xs">
                <button @click="currentTab = 'all'" :class="currentTab === 'all' ? 'border-[#c9a84c] text-[#e8c96d] font-bold' : 'border-transparent text-slate-400 hover:text-slate-200'" class="py-2.5 px-4 border-b-2 font-medium transition-all duration-150 flex items-center gap-2">
                    All Alerts <span class="bg-slate-900 px-1.5 py-0.5 rounded text-[10px] text-slate-400" x-text="counts.all"></span>
                </button>
                <button @click="currentTab = 'low'" :class="currentTab === 'low' ? 'border-[#c9a84c] text-[#e8c96d] font-bold' : 'border-transparent text-slate-400 hover:text-slate-200'" class="py-2.5 px-4 border-b-2 font-medium transition-all duration-150 flex items-center gap-2">
                    🔥 Active Low Stock <span class="bg-amber-950/40 px-1.5 py-0.5 rounded text-[10px] text-amber-400" x-text="counts.low"></span>
                </button>
                <button @click="currentTab = 'archived'" :class="currentTab === 'archived' ? 'border-[#c9a84c] text-[#e8c96d] font-bold' : 'border-transparent text-slate-400 hover:text-slate-200'" class="py-2.5 px-4 border-b-2 font-medium transition-all duration-150 flex items-center gap-2">
                    📁 Archived / Out of Stock <span class="bg-red-950/40 px-1.5 py-0.5 rounded text-[10px] text-red-400" x-text="counts.archived"></span>
                </button>
            </div>
        </header>

        <!-- HIGH-DENSITY CARD LAYOUT GRID -->
        <main class="flex-1 max-w-7xl w-full mx-auto px-4 py-6 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4">
                <template x-for="product in filteredProducts" :key="product.id">
                    <div class="group relative flex flex-col overflow-hidden rounded-xl border border-slate-900 bg-[#08080f] p-3 hover:border-[#c9a84c]/40 transition-all duration-200">
                        
                        <!-- Image Element + Lazy Loader Logic -->
                        <div class="aspect-square w-full overflow-hidden rounded-lg bg-[#0a0a12] border border-[#c9a84c]/10 flex items-center justify-center relative">
                            <img :src="product.image" loading="lazy" class="h-full w-full object-contain object-center group-hover:scale-105 transition-transform duration-200" @error="$el.style.display='none'; $el.nextElementSibling.style.display='flex';" />
                            <!-- Dynamic Initials Avatar Mode if Image Fails to Resolve -->
                            <div style="display:none;" class="absolute inset-0 flex items-center justify-center bg-gradient-to-br from-[#12121a] to-[#04040a] text-[#e8c96d] font-bold font-serif text-lg tracking-wider" x-text="product.name.charAt(0).toUpperCase()"></div>
                        </div>
                        
                        <!-- Metadata Fields Matrix -->
                        <div class="flex flex-1 flex-col mt-3">
                            <p class="text-[9px] font-mono font-bold tracking-wider text-slate-500 uppercase" x-text="product.sku"></p>
                            <h3 class="text-xs font-semibold text-slate-200 truncate mt-0.5" :title="product.name" x-text="product.name"></h3>
                            <p class="text-[10px] text-[#c9a84c]/60 mt-1 truncate font-mono" x-text="product.category"></p>
                            
                            <!-- Actionable Stock Pill Matrix -->
                            <div class="mt-auto pt-3 flex items-center justify-between gap-2 border-t border-slate-900">
                                <span class="inline-flex items-center rounded-full border px-2 py-0.5 text-[8px] font-bold font-mono tracking-wide" :class="product.colorClass" x-text="product.status"></span>
                                <a :href="product.link" target="_blank" class="text-[10px] text-[#e8c96d] hover:text-[#c9a84c] hover:underline font-bold shrink-0 transition-colors">Odoo ↗</a>
                            </div>
                        </div>
                    </div>
                </template>
            </div>
            
            <!-- Exception UI Layer for Null Query Evaluations -->
            <div x-show="filteredProducts.length === 0" class="text-center py-20 border border-dashed border-slate-900 rounded-xl mt-4">
                <p class="text-xs text-slate-500 font-mono tracking-wide">No tracking exceptions matching selection parameters.</p>
            </div>
        </main>
    </div>

</body>
</html>
"""

# 🚀 3. PUSH STATIC INDEX PAYLOAD VIA GITHUB REST COMMIT API
if not GITHUB_TOKEN or GITHUB_OWNER == "your-github-username":
    print("❌ Fatal: GITHUB_TOKEN or GITHUB_OWNER environment parameters are unset. Aborting.", flush=True)
    sys.exit(1)

print("☁️ Processing remote git state mapping configurations...", flush=True)
target_api_url = f"https://github.com{GITHUB_OWNER}/{GITHUB_REPO}/contents/index.html"
request_headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Resolve target item node path schema SHA value to prevent sync overlap drops
remote_blob_sha = None
state_lookup_res = requests.get(target_api_url, headers=request_headers)
if state_lookup_res.status_code == 200:
    remote_blob_sha = state_lookup_res.json().get("sha")

# Assemble binary upload parameters to handle data ingestion safely
commit_payload = {
    "message": f"🔄 Sync: Elite Dashboard Update — {generated_at}",
    "content": base64.b64encode(html_dashboard.encode("utf-8")).decode("utf-8"),
    "branch": GITHUB_BRANCH
}
if remote_blob_sha:
    commit_payload["sha"] = remote_blob_sha

print("🚀 Dispatching payload to GitHub Pages deployment pipeline...", flush=True)
sync_execution_res = requests.put(target_api_url, headers=request_headers, json=commit_payload)

if sync_execution_res.status_code in [200, 201]:
    live_dashboard_url = f"https://{GITHUB_OWNER}.github.io/{GITHUB_REPO}/"
    print(f"✅ Elite Dashboard Successfully Sync'd!", flush=True)
    print(f"🔗 Target Live URL: {live_dashboard_url}", flush=True)
else:
    print(f"❌ Automation Error — GitHub Repository API Refused Write: {sync_execution_res.text}", flush=True)
    sys.exit(1)
