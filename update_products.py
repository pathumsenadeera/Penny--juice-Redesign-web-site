import re

PRODUCTS = [
    {
        "id": "kiwi-vitality",
        "name": "Kiwi Vitality",
        "ingredients": "Kiwi, Apple, Lime, Ginger",
        "price": "$8.99",
        "raw_price": "8.99",
        "image": "images/kiwi-vitality.jpeg",
        "rating": "4.9",
        "badge": "Best Seller",
        "badge_color": "bg-[#7CB342]",
        "tags": "kiwi apple lime ginger green cold-pressed bestseller organic vitality",
        "category": "Green"
    },
    {
        "id": "pineapple-pulse",
        "name": "Pineapple Pulse",
        "ingredients": "Pineapple, Orange, Turmeric, Coconut Water",
        "price": "$8.99",
        "raw_price": "8.99",
        "image": "images/pineapple-pulse.jpeg",
        "rating": "4.8",
        "badge": "Popular",
        "badge_color": "bg-[#F9A602]",
        "tags": "pineapple orange turmeric coconut water citrus immunity popular tropical",
        "category": "Citrus"
    },
    {
        "id": "green-glow",
        "name": "Green Glow",
        "ingredients": "Spinach, Kale, Green Apple, Cucumber, Lemon",
        "price": "$9.49",
        "raw_price": "9.49",
        "image": "images/green-glow.jpeg",
        "rating": "4.9",
        "badge": "Organic",
        "badge_color": "bg-[#2E7D32]",
        "tags": "spinach kale green apple cucumber lemon green detox superfood glow",
        "category": "Green"
    },
    {
        "id": "zen-pear",
        "name": "Zen Pear",
        "ingredients": "Pear, Ginger, Lemon, Apple",
        "price": "$8.99",
        "raw_price": "8.99",
        "image": "images/zen-pear.jpeg",
        "rating": "4.7",
        "badge": "Refreshing",
        "badge_color": "bg-[#8BC34A]",
        "tags": "pear ginger lemon apple refreshing calming digestive zen",
        "category": "Citrus"
    },
    {
        "id": "golden-aura",
        "name": "Golden Aura",
        "ingredients": "Carrot, Orange, Turmeric, Pineapple",
        "price": "$8.49",
        "raw_price": "8.49",
        "image": "images/golden-aura.jpeg",
        "rating": "4.8",
        "badge": "Bestseller",
        "badge_color": "bg-[#FF9800]",
        "tags": "carrot orange turmeric pineapple citrus glow vitamin c aura golden",
        "category": "Citrus"
    },
    {
        "id": "lemon-lift",
        "name": "Lemon Lift",
        "ingredients": "Lemon, Ginger, Honey, Apple",
        "price": "$7.99",
        "raw_price": "7.99",
        "image": "images/lemon-lift.jpeg",
        "rating": "4.9",
        "badge": "Customer Fav",
        "badge_color": "bg-[#FBC02D]",
        "tags": "lemon ginger honey apple energy boost citrus immunity lift",
        "category": "Citrus"
    },
    {
        "id": "tropical-harmony",
        "name": "Tropical Harmony",
        "ingredients": "Mango, Passion Fruit, Pineapple, Coconut",
        "price": "$9.99",
        "raw_price": "9.99",
        "image": "images/tropical-harmony.jpeg",
        "rating": "5.0",
        "badge": "Tropical",
        "badge_color": "bg-[#FF5722]",
        "tags": "mango passion fruit pineapple coconut tropical exotic sweet harmony",
        "category": "Tropical"
    },
    {
        "id": "emerald-energy",
        "name": "Emerald Energy",
        "ingredients": "Celery, Green Apple, Spinach, Lime",
        "price": "$8.99",
        "raw_price": "8.99",
        "image": "images/emerald-energy.jpeg",
        "rating": "4.8",
        "badge": "Vitality",
        "badge_color": "bg-[#00897B]",
        "tags": "celery green apple spinach lime green cleanse vitality emerald energy",
        "category": "Green"
    }
]

def generate_card(p):
    return f'''      <!-- Product Card: {p["name"]} -->
      <div class="product-card group relative bg-white rounded-3xl p-4 border border-slate-100 shadow-[0_4px_20px_rgba(0,0,0,0.05)] hover:shadow-[0_16px_35px_rgba(249,166,2,0.18)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between" data-title="{p['name']}" data-category="{p['category']}" data-tags="{p['tags']}" data-price="{p['raw_price']}">
        <!-- Top Left: Add to Cart Icon Button -->
        <button type="button" aria-label="Add {p['name']} to cart" class="add-to-cart-btn absolute top-4 left-4 z-20 w-10 h-10 rounded-full bg-white/95 backdrop-blur shadow-md border border-slate-100 flex items-center justify-center text-[#1A1A2E] hover:bg-[#F9A602] hover:text-white hover:border-[#F9A602] hover:scale-110 active:scale-95 transition-all duration-200 cursor-pointer" title="Add to Cart" onclick="event.preventDefault(); event.stopPropagation(); window.pjAddToCart && window.pjAddToCart('{p['name']}');">
          <span class="material-symbols-outlined text-[20px]">shopping_cart</span>
        </button>

        <!-- Top Right: Badge -->
        <div class="absolute top-4 right-4 z-20">
          <span class="inline-block {p['badge_color']} text-white text-[10px] font-extrabold px-3 py-1 rounded-full uppercase tracking-wider shadow-xs">{p['badge']}</span>
        </div>

        <!-- Card Body: Image & Details -->
        <a href="product-detail.html" class="block focus:outline-none flex-grow">
          <div class="relative w-full aspect-square bg-gradient-to-b from-slate-50 to-white rounded-2xl p-4 flex items-center justify-center overflow-hidden mb-4 group-hover:bg-[#FFFDF7] transition-colors">
            <img alt="{p['name']}" class="w-full h-full object-contain drop-shadow-md group-hover:scale-105 transition-transform duration-500" src="{p['image']}"/>
          </div>
          
          <div class="px-1 text-left">
            <div class="flex items-center justify-between mb-1">
              <h3 class="font-bold text-lg text-[#1A1A2E] group-hover:text-[#F9A602] transition-colors leading-snug">{p['name']}</h3>
              <div class="flex items-center text-[#F9A602] text-xs font-bold gap-0.5">
                <span class="material-symbols-outlined text-[14px]" style="font-variation-settings: 'FILL' 1;">star</span>
                <span>{p['rating']}</span>
              </div>
            </div>
            <p class="text-xs text-gray-500 line-clamp-1 mb-4">{p['ingredients']}</p>
          </div>
        </a>

        <!-- Card Footer: Price & Buy Button -->
        <div class="mt-auto px-1 pt-3 border-t border-slate-100 flex items-center justify-between gap-3">
          <div>
            <span class="text-[10px] text-gray-400 block font-semibold uppercase tracking-wider leading-none mb-1">Price</span>
            <span class="text-xl font-extrabold text-[#1A1A2E]">{p['price']}</span>
          </div>
          <a href="product-detail.html" class="flex-1 max-w-[125px] py-2.5 px-4 bg-[#F9A602] hover:bg-[#E09400] text-white font-bold text-xs uppercase tracking-wider rounded-full shadow-sm hover:shadow-md transition-all flex items-center justify-center gap-1.5 active:scale-95 text-center">
            <span>Buy</span>
            <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
          </a>
        </div>
      </div>'''

ALL_CARDS_HTML = "\n".join([generate_card(p) for p in PRODUCTS])

TOAST_SCRIPT = '''
<script>
window.pjAddToCart = function(name) {
  const badge = document.querySelector('.pj-cart');
  if (badge) {
    const match = badge.textContent.match(/\\d+/);
    const count = match ? parseInt(match[0]) + 1 : 1;
    badge.innerHTML = `<span class="material-symbols-outlined">shopping_cart</span> (${count})`;
    badge.classList.add('scale-110');
    setTimeout(() => badge.classList.remove('scale-110'), 250);
  }
  let toast = document.getElementById('pj-cart-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'pj-cart-toast';
    toast.className = 'fixed bottom-6 right-6 z-50 bg-[#1A1A2E] text-white px-5 py-3 rounded-2xl shadow-2xl flex items-center gap-3 transform translate-y-10 opacity-0 transition-all duration-300 font-[\'Poppins\']';
    document.body.appendChild(toast);
  }
  toast.innerHTML = `<span class="material-symbols-outlined text-[#F9A602]">check_circle</span> <span class="text-sm font-semibold">${name} added to cart!</span>`;
  requestAnimationFrame(() => {
    toast.classList.remove('translate-y-10', 'opacity-0');
  });
  clearTimeout(window._pjToastTimeout);
  window._pjToastTimeout = setTimeout(() => {
    toast.classList.add('translate-y-10', 'opacity-0');
  }, 2500);
};
</script>
'''

# 1. Update index.html
INDEX_SECTION = f'''<!-- Find Your Flavor -->
<section class="py-24 bg-white w-full overflow-hidden text-center">
  <div class="max-w-[1280px] mx-auto px-6">
    <p class="text-xs text-[#F9A602] font-bold uppercase tracking-widest mb-2">ALL FLAVORS</p>
    <h2 class="text-4xl font-extrabold text-[#1A1A2E] mb-4">Find Your Flavor</h2>
    <p class="text-gray-500 max-w-lg mx-auto mb-16">Penny Juice comes in a variety of refreshing flavors made with real juice and natural ingredients.</p>
    
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
{ALL_CARDS_HTML}
    </div>
  </div>
</section>'''

def update_index_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Replace Find Your Flavor section
    new_c = re.sub(r'<!-- Find Your Flavor -->.*?</section>', INDEX_SECTION, c, flags=re.DOTALL)
    
    # Add toast script before </body> if not present
    if 'window.pjAddToCart' not in new_c:
        new_c = new_c.replace('</body>', f'{TOAST_SCRIPT}\n</body>')
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Updated {path}")

# 2. Update shop.html
SHOP_GRID = f'''<!-- Products Grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-gutter mb-12">
{ALL_CARDS_HTML}
</div>'''

def update_shop_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    new_c = re.sub(r'<!-- Products Grid -->.*?<!-- Pagination -->', f'{SHOP_GRID}<!-- Pagination -->', c, flags=re.DOTALL)
    
    if 'window.pjAddToCart' not in new_c:
        new_c = new_c.replace('</body>', f'{TOAST_SCRIPT}\n</body>')
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Updated {path}")

# 3. Update search.html
SEARCH_GRID = f'''  <!-- 8 Organic Juices Results Grid -->
  <div id="productGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
{ALL_CARDS_HTML}
  </div>'''

def update_search_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    new_c = re.sub(r'<!-- \d+ Organic Juices Results Grid -->\s*<div id="productGrid".*?</div>\s*<!-- Empty State', f'{SEARCH_GRID}\n\n  <!-- Empty State', c, flags=re.DOTALL)
    new_c = re.sub(r'\d+ flavors found', '8 flavors found', new_c)
    new_c = re.sub(r'Show All \d+ Juices', 'Show All 8 Juices', new_c)
    
    if 'window.pjAddToCart' not in new_c:
        new_c = new_c.replace('</body>', f'{TOAST_SCRIPT}\n</body>')
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Updated {path}")

# Run updates
update_index_file('site/public/index.html')
update_index_file('.stitch/designs/index.html')

update_shop_file('site/public/shop.html')
update_shop_file('.stitch/designs/shop.html')

update_search_file('site/public/search.html')
update_search_file('.stitch/designs/search.html')

print("All files updated successfully!")
