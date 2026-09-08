import re
from update_products import PRODUCTS, generate_card, TOAST_SCRIPT

# Select the top 4 most popular flavors:
# 1. Kiwi Vitality, 2. Pineapple Pulse, 3. Green Glow, 4. Golden Aura
POPULAR_PRODUCTS = [PRODUCTS[0], PRODUCTS[1], PRODUCTS[2], PRODUCTS[4]]

POPULAR_CARDS_HTML = "\n".join([generate_card(p) for p in POPULAR_PRODUCTS])

POPULAR_SECTION = f'''<!-- Most Popular Flavors -->
<section class="py-24 bg-white w-full overflow-hidden text-center">
  <div class="max-w-[1280px] mx-auto px-6">
    <p class="text-xs text-[#F9A602] font-bold uppercase tracking-widest mb-2">MOST POPULAR</p>
    <h2 class="text-4xl font-extrabold text-[#1A1A2E] mb-4">Most Popular Flavors</h2>
    <p class="text-gray-500 max-w-lg mx-auto mb-16">Our customers' top-rated cold-pressed blends, crafted fresh with real fruits and 100% organic ingredients.</p>
    
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
{POPULAR_CARDS_HTML}
    </div>

    <div class="mt-14 text-center">
      <a href="shop.html" class="inline-flex items-center gap-2 px-8 py-3.5 rounded-full bg-[#1A1A2E] text-white hover:bg-[#F9A602] font-bold text-sm tracking-wide transition-all shadow-md hover:shadow-lg hover:scale-105 active:scale-95">
        <span>View All Flavors</span>
        <span class="material-symbols-outlined text-sm">arrow_forward</span>
      </a>
    </div>
  </div>
</section>'''

for target_file in ['site/public/index.html', '.stitch/designs/index.html', 'site/public/update_index.py']:
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match existing Find Your Flavor or Most Popular Flavors section
    new_content = re.sub(
        r'<!-- (?:Find Your Flavor|Most Popular Flavors) -->.*?</section>',
        POPULAR_SECTION,
        content,
        flags=re.DOTALL
    )

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {target_file}")

print("Done updating home page popular flavors section!")
