import re

BLOG_MAIN = '''<main class="flex-grow w-full py-10">
  <div class="max-w-[1360px] mx-auto px-4 sm:px-6 lg:px-8">

    <!-- CATEGORY FILTER PILLS -->
    <div class="flex items-center gap-3 overflow-x-auto no-scrollbar pb-6 mb-8 border-b border-slate-200/60">
      <button class="px-6 py-2.5 rounded-full bg-[#1A1A2E] text-white font-bold text-xs uppercase tracking-wider shadow-sm hover:bg-[#F9A602] transition-colors whitespace-nowrap">All Stories</button>
      <button class="px-5 py-2.5 rounded-full bg-white text-gray-600 hover:text-[#F9A602] hover:bg-[#FFF7E6] font-bold text-xs uppercase tracking-wider transition-colors border border-slate-200/80 whitespace-nowrap">Superfoods</button>
      <button class="px-5 py-2.5 rounded-full bg-white text-gray-600 hover:text-[#F9A602] hover:bg-[#FFF7E6] font-bold text-xs uppercase tracking-wider transition-colors border border-slate-200/80 whitespace-nowrap">Nutrition Science</button>
      <button class="px-5 py-2.5 rounded-full bg-white text-gray-600 hover:text-[#F9A602] hover:bg-[#FFF7E6] font-bold text-xs uppercase tracking-wider transition-colors border border-slate-200/80 whitespace-nowrap">Mind & Mood</button>
      <button class="px-5 py-2.5 rounded-full bg-white text-gray-600 hover:text-[#F9A602] hover:bg-[#FFF7E6] font-bold text-xs uppercase tracking-wider transition-colors border border-slate-200/80 whitespace-nowrap">Farm Sourcing</button>
    </div>

    <!-- FEATURED HERO STORY: POWER DUO (KIWIS & PINEAPPLES) -->
    <article class="bg-white rounded-[36px] border border-slate-100 shadow-[0_15px_45px_rgba(0,0,0,0.06)] overflow-hidden mb-16 group hover:shadow-[0_25px_60px_rgba(249,166,2,0.15)] transition-all duration-500">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-0 items-stretch">
        
        <!-- Left Column: Story Content -->
        <div class="lg:col-span-7 p-8 sm:p-12 lg:p-14 flex flex-col justify-between">
          <div>
            <!-- Badges -->
            <div class="flex flex-wrap items-center gap-3 mb-6">
              <span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-[#E8F5E9] text-[#2E7D32] text-xs font-black uppercase tracking-wider border border-[#C8E6C9]">
                <span class="material-symbols-outlined text-[15px]">star</span> Editor\'s Pick
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-amber-50 text-amber-800 text-xs font-bold uppercase tracking-wider border border-amber-200">
                Superfruit Spotlight
              </span>
              <span class="text-gray-400 text-xs font-medium flex items-center gap-1">
                <span class="material-symbols-outlined text-[14px]">calendar_today</span> APRIL 25th, 2025
              </span>
            </div>

            <!-- Title -->
            <h2 class="text-2xl sm:text-3xl lg:text-4xl font-black text-[#1A1A2E] leading-tight mb-5 group-hover:text-[#F9A602] transition-colors">
              Power Duo: Why Kiwis and Pineapples Are the Superfruits You Need
            </h2>

            <!-- Lead Paragraph -->
            <p class="text-gray-600 text-base sm:text-lg leading-relaxed mb-6 font-normal">
              When it comes to bold flavors and vibrant nutrition, few fruits can compete with the dynamic duo of kiwis and pineapples. Both tropical treats are more than just pretty faces in your smoothie—they pack serious health benefits that can boost your energy, digestion, and skin glow.
            </p>

            <!-- Dual Superfruit Benefit Cards -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
              <!-- Kiwi Block -->
              <div class="bg-[#F1F8E9] rounded-2xl p-4 border border-[#DCEDC8]">
                <div class="flex items-center gap-2 mb-2">
                  <span class="w-7 h-7 rounded-full bg-[#7CB342] text-white flex items-center justify-center font-bold text-xs">🥝</span>
                  <h4 class="font-extrabold text-[#2E7D32] text-sm">Kiwi Vitality</h4>
                </div>
                <p class="text-xs text-gray-600 leading-relaxed">
                  With electric green flesh and tiny seeds, kiwis are rich in vitamin C, vitamin K, and fiber. They support immunity, aid digestion, and add tangy sweet punch to bowls and salsas.
                </p>
              </div>

              <!-- Pineapple Block -->
              <div class="bg-[#FFF8E1] rounded-2xl p-4 border border-[#FFE082]">
                <div class="flex items-center gap-2 mb-2">
                  <span class="w-7 h-7 rounded-full bg-[#F9A602] text-white flex items-center justify-center font-bold text-xs">🍍</span>
                  <h4 class="font-extrabold text-[#E65100] text-sm">Pineapple Sunshine</h4>
                </div>
                <p class="text-xs text-gray-600 leading-relaxed">
                  Nature\'s sunshine, loaded with bromelain enzyme for reducing inflammation and aiding digestion. Excellent source of manganese and vitamin B6 for sweet and savory dishes.
                </p>
              </div>
            </div>
          </div>

          <!-- Author Footnote & Action -->
          <div class="pt-6 border-t border-slate-100 flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
              <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-[#F9A602] to-[#FF7043] flex items-center justify-center text-white font-extrabold text-sm shadow-sm">
                L
              </div>
              <div>
                <p class="font-bold text-sm text-[#1A1A2E]">Written by LUIS</p>
                <p class="text-xs text-gray-400">Wellness & Nutrition Editor • 5 min read</p>
              </div>
            </div>
            <a href="shop.html" class="inline-flex items-center gap-2 px-6 py-2.5 rounded-full bg-[#1A1A2E] text-white font-bold text-xs uppercase tracking-wider hover:bg-[#F9A602] transition-colors shadow-sm">
              <span>Taste Both</span>
              <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
            </a>
          </div>
        </div>

        <!-- Right Column: Hero Visual Image -->
        <div class="lg:col-span-5 relative min-h-[380px] lg:min-h-full overflow-hidden bg-slate-100">
          <img src="images/blog-kiwi-pineapple.jpg" alt="Splashing Kiwis and Pineapples" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"/>
          <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent lg:hidden"></div>
          <div class="absolute top-4 right-4 bg-white/90 backdrop-blur-md px-3 py-1.5 rounded-full text-xs font-extrabold text-[#1A1A2E] shadow-sm flex items-center gap-1.5">
            <span class="material-symbols-outlined text-sm text-[#7CB342]">auto_awesome</span> Superfood Duo
          </div>
        </div>

      </div>
    </article>

    <!-- SECTION TITLE: RECENT DISPATCHES -->
    <div class="flex flex-col sm:flex-row sm:items-end justify-between mb-10">
      <div>
        <span class="text-xs font-extrabold text-[#F9A602] uppercase tracking-widest block mb-1">FRESH PERSPECTIVES</span>
        <h3 class="text-2xl sm:text-3xl font-black text-[#1A1A2E] tracking-tight">Essential Juice Wisdom</h3>
      </div>
      <p class="text-gray-500 text-sm max-w-md mt-2 sm:mt-0">
        Science-backed wellness, botanical breakdowns, and tips to elevate your vitality.
      </p>
    </div>

    <!-- 3 USER SPOTLIGHT ARTICLES (COLD PRESSED, MOOD BOOSTERS, MANGO MAGIC) -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-20">
      
      <!-- Article 1: Cold-Pressed Gold Standard -->
      <article class="bg-white rounded-3xl overflow-hidden border border-slate-100 shadow-[0_8px_30px_rgba(0,0,0,0.04)] hover:shadow-[0_16px_40px_rgba(249,166,2,0.15)] hover:-translate-y-2 transition-all duration-300 flex flex-col justify-between group">
        <div>
          <!-- Thumbnail -->
          <div class="relative w-full aspect-[16/10] overflow-hidden">
            <img src="images/blog-cold-pressed.jpg" alt="Cold-Pressed Juicing" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
            <span class="absolute top-4 left-4 bg-white/90 backdrop-blur-md px-3 py-1 rounded-full text-[11px] font-extrabold text-amber-900 shadow-xs uppercase tracking-wider">
              🍋 Science of Juicing
            </span>
          </div>
          <!-- Body -->
          <div class="p-7">
            <div class="flex items-center gap-2 text-xs text-gray-400 font-medium mb-3">
              <span>Nutrition Standard</span> • <span>4 min read</span>
            </div>
            <h3 class="text-xl font-extrabold text-[#1A1A2E] mb-3 group-hover:text-[#F9A602] transition-colors leading-snug">
              🍋 Why Cold-Pressed is the Gold Standard
            </h3>
            <p class="text-gray-600 text-sm leading-relaxed mb-4">
              Cold-pressed juice preserves more nutrients, flavor, and life-force from fruits. Learn how hydraulic extraction keeps enzymes intact so your body can truly <em class="text-[#1A1A2E] font-medium">absorb the good stuff</em> without heat degradation.
            </p>
          </div>
        </div>
        <!-- Footer -->
        <div class="px-7 pb-7 pt-0">
          <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs">
            <span class="font-bold text-gray-500">By Dr. Elena</span>
            <span class="font-bold text-[#F9A602] group-hover:translate-x-1 transition-transform flex items-center gap-1">Read Article <span class="material-symbols-outlined text-sm">arrow_forward</span></span>
          </div>
        </div>
      </article>

      <!-- Article 2: Top 5 Ingredients That Boost Your Mood -->
      <article class="bg-white rounded-3xl overflow-hidden border border-slate-100 shadow-[0_8px_30px_rgba(0,0,0,0.04)] hover:shadow-[0_16px_40px_rgba(46,125,50,0.15)] hover:-translate-y-2 transition-all duration-300 flex flex-col justify-between group">
        <div>
          <!-- Thumbnail -->
          <div class="relative w-full aspect-[16/10] overflow-hidden">
            <img src="images/blog-mood-boosters.jpg" alt="Botanicals Mood Boosters" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
            <span class="absolute top-4 left-4 bg-white/90 backdrop-blur-md px-3 py-1 rounded-full text-[11px] font-extrabold text-emerald-900 shadow-xs uppercase tracking-wider">
              🌱 Mood & Mind
            </span>
          </div>
          <!-- Body -->
          <div class="p-7">
            <div class="flex items-center gap-2 text-xs text-gray-400 font-medium mb-3">
              <span>Botanical Wellness</span> • <span>5 min read</span>
            </div>
            <h3 class="text-xl font-extrabold text-[#1A1A2E] mb-3 group-hover:text-[#2E7D32] transition-colors leading-snug">
              🌱 Top 5 Ingredients That Boost Your Mood
            </h3>
            <p class="text-gray-600 text-sm leading-relaxed mb-4">
              From invigorating lemon zest to soothing fresh spearmint, nature provides potent biochemical mood-lifters. Here’s our definitive list of juice-friendly botanicals that brighten your day and restore mental clarity.
            </p>
          </div>
        </div>
        <!-- Footer -->
        <div class="px-7 pb-7 pt-0">
          <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs">
            <span class="font-bold text-gray-500">By Petunia</span>
            <span class="font-bold text-[#2E7D32] group-hover:translate-x-1 transition-transform flex items-center gap-1">Read Article <span class="material-symbols-outlined text-sm">arrow_forward</span></span>
          </div>
        </div>
      </article>

      <!-- Article 3: A Deep Dive Into Mango Magic -->
      <article class="bg-white rounded-3xl overflow-hidden border border-slate-100 shadow-[0_8px_30px_rgba(0,0,0,0.04)] hover:shadow-[0_16px_40px_rgba(255,112,67,0.15)] hover:-translate-y-2 transition-all duration-300 flex flex-col justify-between group">
        <div>
          <!-- Thumbnail -->
          <div class="relative w-full aspect-[16/10] overflow-hidden">
            <img src="images/blog-mango-magic.jpg" alt="Mango Magic" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
            <span class="absolute top-4 left-4 bg-white/90 backdrop-blur-md px-3 py-1 rounded-full text-[11px] font-extrabold text-orange-900 shadow-xs uppercase tracking-wider">
              🥭 Flavor Spotlight
            </span>
          </div>
          <!-- Body -->
          <div class="p-7">
            <div class="flex items-center gap-2 text-xs text-gray-400 font-medium mb-3">
              <span>Fruit Spotlight</span> • <span>6 min read</span>
            </div>
            <h3 class="text-xl font-extrabold text-[#1A1A2E] mb-3 group-hover:text-[#FF7043] transition-colors leading-snug">
              🥭 A Deep Dive Into Mango Magic
            </h3>
            <p class="text-gray-600 text-sm leading-relaxed mb-4">
              Mango isn’t just a summer favorite—it’s overflowing with cellular antioxidants and skin-glowing beta-carotene. Discover why this luscious fruit stars centrally in our customer-favorite <span class="text-[#1A1A2E] font-semibold">Golden Aura</span> blend.
            </p>
          </div>
        </div>
        <!-- Footer -->
        <div class="px-7 pb-7 pt-0">
          <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs">
            <span class="font-bold text-gray-500">By Luis</span>
            <span class="font-bold text-[#FF7043] group-hover:translate-x-1 transition-transform flex items-center gap-1">Read Article <span class="material-symbols-outlined text-sm">arrow_forward</span></span>
          </div>
        </div>
      </article>

    </div>


  </div>
</main>'''

for path in ['site/public/blog.html', '.stitch/designs/blog.html']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Replace the banner title and subtitle
    c = c.replace('<h1>Juice Journal</h1>', '<h1>Fresh Sips & Juice Wisdom</h1>')
    c = c.replace('<p>Health tips, recipes, and wellness insights from our nutrition experts.</p>',
                  '<p>Explore the vibrant world of organic juices, wellness, and nature’s best-kept secrets.</p>')
    c = c.replace('<title>Penny Juice - Blog</title>', '<title>Fresh Sips & Juice Wisdom - Penny Juice</title>')
    
    # Replace <main> ... </main>
    new_c = re.sub(r'<main.*?</main>', BLOG_MAIN, c, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Updated {path}")

print("Blog page updated successfully!")
