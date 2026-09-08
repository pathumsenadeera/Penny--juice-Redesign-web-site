import re

INGREDIENTS_CONTENT = '''<main class="flex-grow w-full py-10">

  <!-- HERO INTRO: PENNY JUICE NATURAL INGREDIENTS -->
  <section class="max-w-[1280px] mx-auto px-4 sm:px-6 lg:px-8 mb-20">
    <div class="text-center max-w-3xl mx-auto">
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#E8F5E9] text-[#2E7D32] text-xs font-extrabold uppercase tracking-widest mb-4 shadow-2xs border border-[#C8E6C9]">
        <span class="material-symbols-outlined text-[16px]">verified</span>
        100% Pure Botanical Promise
      </div>
      <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-[#1A1A2E] tracking-tight mb-5">
        Penny Juice <span class="bg-gradient-to-r from-[#F9A602] to-[#FF7043] bg-clip-text text-transparent">Natural Ingredients</span>
      </h2>
      <p class="text-gray-600 text-base sm:text-lg leading-relaxed mb-8">
        Our juices are made with <strong class="text-[#1A1A2E] font-semibold">100% real fruit juice concentrates and purees</strong>, blended with care to keep things fresh, flavorful, and full of life. No artificial colors, sweeteners, or preservatives—ever.
      </p>

      <!-- Purity Badges Pill -->
      <div class="flex flex-wrap items-center justify-center gap-3 sm:gap-4 mb-12">
        <span class="inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-red-50 text-red-700 text-xs font-bold border border-red-200 shadow-2xs">
          <span class="material-symbols-outlined text-[16px]">block</span> No Artificial Colors
        </span>
        <span class="inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-red-50 text-red-700 text-xs font-bold border border-red-200 shadow-2xs">
          <span class="material-symbols-outlined text-[16px]">block</span> No Artificial Sweeteners
        </span>
        <span class="inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-red-50 text-red-700 text-xs font-bold border border-red-200 shadow-2xs">
          <span class="material-symbols-outlined text-[16px]">block</span> No Preservatives Ever
        </span>
        <span class="inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-[#E8F5E9] text-[#2E7D32] text-xs font-bold border border-[#C8E6C9] shadow-2xs">
          <span class="material-symbols-outlined text-[16px]">check_circle</span> 100% Real Fruit
        </span>
      </div>
    </div>

    <!-- Commercial Flatlay Banner Showcase -->
    <div class="relative w-full rounded-[32px] overflow-hidden shadow-[0_15px_40px_rgba(0,0,0,0.08)] border border-slate-100 group">
      <img src="images/ingredients-flatlay.jpg" alt="Penny Juice Fresh Ingredients Flatlay" class="w-full h-80 sm:h-96 md:h-[420px] object-cover group-hover:scale-105 transition-transform duration-700"/>
      <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-black/20 pointer-events-none"></div>
      
      <div class="absolute bottom-6 left-6 right-6 flex flex-col sm:flex-row items-start sm:items-end justify-between gap-4 text-white z-10">
        <div>
          <span class="text-xs font-extrabold uppercase tracking-wider text-[#F9A602] block mb-1">Cold-Pressed Freshness</span>
          <h3 class="text-xl sm:text-2xl font-bold">Uncompromising Quality in Every Drop</h3>
        </div>
        <a href="shop.html" class="px-6 py-2.5 rounded-full bg-white/95 hover:bg-white text-[#1A1A2E] font-bold text-xs uppercase tracking-wider shadow-md hover:scale-105 active:scale-95 transition-all flex items-center gap-2">
          <span>Taste The Ingredients</span>
          <span class="material-symbols-outlined text-sm text-[#F9A602]">arrow_forward</span>
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION: CORE FRUIT INGREDIENTS -->
  <section class="max-w-[1280px] mx-auto px-4 sm:px-6 lg:px-8 mb-24">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12">
      <div>
        <div class="inline-flex items-center gap-2 text-xs font-extrabold text-[#7CB342] uppercase tracking-widest mb-2">
          <span class="w-2 h-2 rounded-full bg-[#7CB342]"></span>
          Foundational Nutrition
        </div>
        <h3 class="text-3xl sm:text-4xl font-black text-[#1A1A2E] tracking-tight">Core Fruit Ingredients</h3>
      </div>
      <p class="text-gray-500 text-sm max-w-md mt-2 md:mt-0 leading-relaxed">
        Sun-drenched whole fruits harvested at peak ripeness for natural sweetness, crisp acidity, and living vitality.
      </p>
    </div>

    <!-- 6 Core Fruits Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
      
      <!-- 1. Green Apple -->
      <div class="bg-white rounded-3xl p-7 border border-slate-100 shadow-[0_8px_30px_rgba(0,0,0,0.04)] hover:shadow-[0_16px_40px_rgba(124,179,66,0.15)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group">
        <div>
          <div class="flex items-center justify-between mb-5">
            <div class="w-14 h-14 rounded-2xl bg-[#E8F5E9] text-[#2E7D32] flex items-center justify-center group-hover:scale-110 group-hover:bg-[#2E7D32] group-hover:text-white transition-all shadow-xs">
              <span class="material-symbols-outlined text-2xl">nutrition</span>
            </div>
            <span class="px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 text-[11px] font-extrabold uppercase tracking-wide border border-emerald-100">
              Crisp & Tart
            </span>
          </div>
          <h4 class="text-2xl font-bold text-[#1A1A2E] mb-2 group-hover:text-[#2E7D32] transition-colors">Green Apple</h4>
          <p class="text-xs font-bold text-[#7CB342] uppercase tracking-wider mb-3">Crisp, tart, hydrating</p>
          <p class="text-gray-600 text-sm leading-relaxed mb-6">
            Brimming with natural malic acid and pectin fiber, crisp green apples deliver instant refreshing hydration and digestive balance.
          </p>
        </div>
        <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-gray-500">
          <span class="flex items-center gap-1 font-semibold text-[#1A1A2E]"><span class="material-symbols-outlined text-[15px] text-[#7CB342]">check</span> High Pectin</span>
          <span class="font-medium">Rich in Vitamin C</span>
        </div>
      </div>

      <!-- 2. Kiwi -->
      <div class="bg-white rounded-3xl p-7 border border-slate-100 shadow-[0_8px_30px_rgba(0,0,0,0.04)] hover:shadow-[0_16px_40px_rgba(124,179,66,0.15)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group">
        <div>
          <div class="flex items-center justify-between mb-5">
            <div class="w-14 h-14 rounded-2xl bg-[#F1F8E9] text-[#7CB342] flex items-center justify-center group-hover:scale-110 group-hover:bg-[#7CB342] group-hover:text-white transition-all shadow-xs">
              <span class="material-symbols-outlined text-2xl">spa</span>
            </div>
            <span class="px-3 py-1 rounded-full bg-lime-50 text-lime-800 text-[11px] font-extrabold uppercase tracking-wide border border-lime-100">
              Superfood
            </span>
          </div>
          <h4 class="text-2xl font-bold text-[#1A1A2E] mb-2 group-hover:text-[#7CB342] transition-colors">Kiwi</h4>
          <p class="text-xs font-bold text-[#7CB342] uppercase tracking-wider mb-3">Tangy, vitamin-rich, fiber-packed</p>
          <p class="text-gray-600 text-sm leading-relaxed mb-6">
            A nutritional powerhouse loaded with more Vitamin C than citrus, dietary fiber, and natural actinidain enzymes for gut health.
          </p>
        </div>
        <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-gray-500">
          <span class="flex items-center gap-1 font-semibold text-[#1A1A2E]"><span class="material-symbols-outlined text-[15px] text-[#7CB342]">check</span> 2x Vitamin C</span>
          <span class="font-medium">Prebiotic Fiber</span>
        </div>
      </div>

      <!-- 3. Pear -->
      <div class="bg-white rounded-3xl p-7 border border-slate-100 shadow-[0_8px_30px_rgba(0,0,0,0.04)] hover:shadow-[0_16px_40px_rgba(249,166,2,0.15)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group">
        <div>
          <div class="flex items-center justify-between mb-5">
            <div class="w-14 h-14 rounded-2xl bg-[#FFF7E6] text-[#F9A602] flex items-center justify-center group-hover:scale-110 group-hover:bg-[#F9A602] group-hover:text-white transition-all shadow-xs">
              <span class="material-symbols-outlined text-2xl">water_drop</span>
            </div>
            <span class="px-3 py-1 rounded-full bg-amber-50 text-amber-800 text-[11px] font-extrabold uppercase tracking-wide border border-amber-100">
              Antioxidant
            </span>
          </div>
          <h4 class="text-2xl font-bold text-[#1A1A2E] mb-2 group-hover:text-[#F9A602] transition-colors">Pear</h4>
          <p class="text-xs font-bold text-[#F9A602] uppercase tracking-wider mb-3">Mellow sweetness, high in antioxidants</p>
          <p class="text-gray-600 text-sm leading-relaxed mb-6">
            Smooth, gentle sweetness that balances bolder notes while delivering essential polyphenols, copper, and soothing alkalinity.
          </p>
        </div>
        <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-gray-500">
          <span class="flex items-center gap-1 font-semibold text-[#1A1A2E]"><span class="material-symbols-outlined text-[15px] text-[#F9A602]">check</span> Low Glycemic</span>
          <span class="font-medium">Rich in Flavonoids</span>
        </div>
      </div>

      <!-- 4. Mango -->
      <div class="bg-white rounded-3xl p-7 border border-slate-100 shadow-[0_8px_30px_rgba(0,0,0,0.04)] hover:shadow-[0_16px_40px_rgba(255,112,67,0.15)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group">
        <div>
          <div class="flex items-center justify-between mb-5">
            <div class="w-14 h-14 rounded-2xl bg-orange-50 text-[#FF7043] flex items-center justify-center group-hover:scale-110 group-hover:bg-[#FF7043] group-hover:text-white transition-all shadow-xs">
              <span class="material-symbols-outlined text-2xl">wb_sunny</span>
            </div>
            <span class="px-3 py-1 rounded-full bg-orange-50 text-orange-800 text-[11px] font-extrabold uppercase tracking-wide border border-orange-100">
              Tropical Sun
            </span>
          </div>
          <h4 class="text-2xl font-bold text-[#1A1A2E] mb-2 group-hover:text-[#FF7043] transition-colors">Mango</h4>
          <p class="text-xs font-bold text-[#FF7043] uppercase tracking-wider mb-3">Tropical, juicy, rich in vitamins A & C</p>
          <p class="text-gray-600 text-sm leading-relaxed mb-6">
            The king of tropical fruits, offering velvety texture and rich beta-carotene to support glowing skin and radiant immunity.
          </p>
        </div>
        <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-gray-500">
          <span class="flex items-center gap-1 font-semibold text-[#1A1A2E]"><span class="material-symbols-outlined text-[15px] text-[#FF7043]">check</span> Beta-Carotene</span>
          <span class="font-medium">Vitamins A & C</span>
        </div>
      </div>

      <!-- 5. Yellow Lemon -->
      <div class="bg-white rounded-3xl p-7 border border-slate-100 shadow-[0_8px_30px_rgba(0,0,0,0.04)] hover:shadow-[0_16px_40px_rgba(251,192,45,0.2)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group">
        <div>
          <div class="flex items-center justify-between mb-5">
            <div class="w-14 h-14 rounded-2xl bg-yellow-50 text-[#FBC02D] flex items-center justify-center group-hover:scale-110 group-hover:bg-[#FBC02D] group-hover:text-[#1A1A2E] transition-all shadow-xs">
              <span class="material-symbols-outlined text-2xl">bolt</span>
            </div>
            <span class="px-3 py-1 rounded-full bg-yellow-50 text-yellow-800 text-[11px] font-extrabold uppercase tracking-wide border border-yellow-200">
              Immunity
            </span>
          </div>
          <h4 class="text-2xl font-bold text-[#1A1A2E] mb-2 group-hover:text-[#FBC02D] transition-colors">Yellow Lemon</h4>
          <p class="text-xs font-bold text-[#FBC02D] uppercase tracking-wider mb-3">Zesty, cleansing, immune-boosting</p>
          <p class="text-gray-600 text-sm leading-relaxed mb-6">
            Pure citrus brilliance packed with bioflavonoids to jumpstart cellular cleansing, awaken digestion, and shield immunity.
          </p>
        </div>
        <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-gray-500">
          <span class="flex items-center gap-1 font-semibold text-[#1A1A2E]"><span class="material-symbols-outlined text-[15px] text-[#FBC02D]">check</span> Bioflavonoids</span>
          <span class="font-medium">Alkalizing Zing</span>
        </div>
      </div>

      <!-- 6. Pineapple -->
      <div class="bg-white rounded-3xl p-7 border border-slate-100 shadow-[0_8px_30px_rgba(0,0,0,0.04)] hover:shadow-[0_16px_40px_rgba(249,166,2,0.15)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group">
        <div>
          <div class="flex items-center justify-between mb-5">
            <div class="w-14 h-14 rounded-2xl bg-[#FFF7E6] text-[#F9A602] flex items-center justify-center group-hover:scale-110 group-hover:bg-[#F9A602] group-hover:text-white transition-all shadow-xs">
              <span class="material-symbols-outlined text-2xl">auto_awesome</span>
            </div>
            <span class="px-3 py-1 rounded-full bg-amber-50 text-amber-800 text-[11px] font-extrabold uppercase tracking-wide border border-amber-100">
              Bromelain
            </span>
          </div>
          <h4 class="text-2xl font-bold text-[#1A1A2E] mb-2 group-hover:text-[#F9A602] transition-colors">Pineapple</h4>
          <p class="text-xs font-bold text-[#F9A602] uppercase tracking-wider mb-3">Bright, sweet-tart, packed with bromelain</p>
          <p class="text-gray-600 text-sm leading-relaxed mb-6">
            Crisp tropical sweetness containing bromelain, a natural proteolytic enzyme renowned for joint health and digestive ease.
          </p>
        </div>
        <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-gray-500">
          <span class="flex items-center gap-1 font-semibold text-[#1A1A2E]"><span class="material-symbols-outlined text-[15px] text-[#F9A602]">check</span> Bromelain Power</span>
          <span class="font-medium">Anti-Inflammatory</span>
        </div>
      </div>

    </div>
  </section>

  <!-- SECTION: OTHER NATURAL ADDITIONS -->
  <section class="max-w-[1280px] mx-auto px-4 sm:px-6 lg:px-8 mb-24">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12">
      <div>
        <div class="inline-flex items-center gap-2 text-xs font-extrabold text-[#F9A602] uppercase tracking-widest mb-2">
          <span class="w-2 h-2 rounded-full bg-[#F9A602]"></span>
          Functional Botanicals & Superfoods
        </div>
        <h3 class="text-3xl sm:text-4xl font-black text-[#1A1A2E] tracking-tight">Other Natural Additions</h3>
      </div>
      <p class="text-gray-500 text-sm max-w-md mt-2 md:mt-0 leading-relaxed">
        Curated herbs, roots, and pure elements that balance sweetness, deliver functional health benefits, and sharpen flavor.
      </p>
    </div>

    <!-- 6 Additions Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      
      <!-- 1. Filtered Water -->
      <div class="bg-gradient-to-br from-white to-[#F0F9FF] rounded-3xl p-6 border border-sky-100 shadow-sm hover:shadow-md transition-all flex items-start gap-4 group">
        <div class="w-12 h-12 rounded-2xl bg-sky-100 text-sky-600 flex items-center justify-center shrink-0 group-hover:scale-110 transition-transform">
          <span class="material-symbols-outlined text-2xl">water_drop</span>
        </div>
        <div>
          <h4 class="font-bold text-lg text-[#1A1A2E] mb-1">Filtered Water</h4>
          <p class="text-xs font-semibold text-sky-600 uppercase tracking-wide mb-2">For a smooth, refreshing base</p>
          <p class="text-gray-600 text-xs sm:text-sm leading-relaxed">
            Multi-stage micro-filtered water ensures crystalline purity and the ideal density to showcase untouched fruit concentrates.
          </p>
        </div>
      </div>

      <!-- 2. Agave or Coconut Nectar -->
      <div class="bg-gradient-to-br from-white to-[#FFFBEB] rounded-3xl p-6 border border-amber-100 shadow-sm hover:shadow-md transition-all flex items-start gap-4 group">
        <div class="w-12 h-12 rounded-2xl bg-amber-100 text-amber-700 flex items-center justify-center shrink-0 group-hover:scale-110 transition-transform">
          <span class="material-symbols-outlined text-2xl">nature</span>
        </div>
        <div>
          <h4 class="font-bold text-lg text-[#1A1A2E] mb-1">Agave or Coconut Nectar</h4>
          <p class="text-xs font-semibold text-amber-700 uppercase tracking-wide mb-2">Optional light natural sweetener</p>
          <p class="text-gray-600 text-xs sm:text-sm leading-relaxed">
            Unrefined, plant-tapped nectars with a low glycemic response for gentle, rounded sweetness without refined sugar spikes.
          </p>
        </div>
      </div>

      <!-- 3. Lime Juice -->
      <div class="bg-gradient-to-br from-white to-[#F7FEE7] rounded-3xl p-6 border border-lime-100 shadow-sm hover:shadow-md transition-all flex items-start gap-4 group">
        <div class="w-12 h-12 rounded-2xl bg-lime-100 text-lime-700 flex items-center justify-center shrink-0 group-hover:scale-110 transition-transform">
          <span class="material-symbols-outlined text-2xl">contrast</span>
        </div>
        <div>
          <h4 class="font-bold text-lg text-[#1A1A2E] mb-1">Lime Juice</h4>
          <p class="text-xs font-semibold text-lime-700 uppercase tracking-wide mb-2">For added brightness & alkalizing effects</p>
          <p class="text-gray-600 text-xs sm:text-sm leading-relaxed">
            Fresh-squeezed lime brings crisp citrus acidity that elevates aroma, balances sweet notes, and promotes healthy alkaline balance.
          </p>
        </div>
      </div>

      <!-- 4. Mint Leaves -->
      <div class="bg-gradient-to-br from-white to-[#ECFDF5] rounded-3xl p-6 border border-emerald-100 shadow-sm hover:shadow-md transition-all flex items-start gap-4 group">
        <div class="w-12 h-12 rounded-2xl bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0 group-hover:scale-110 transition-transform">
          <span class="material-symbols-outlined text-2xl">spa</span>
        </div>
        <div>
          <h4 class="font-bold text-lg text-[#1A1A2E] mb-1">Mint Leaves</h4>
          <p class="text-xs font-semibold text-emerald-700 uppercase tracking-wide mb-2">Cooling and soothing</p>
          <p class="text-gray-600 text-xs sm:text-sm leading-relaxed">
            Fragrant garden-harvested spearmint leaves provide natural menthol cooling, calming digestive relief, and an invigorating finish.
          </p>
        </div>
      </div>

      <!-- 5. Ginger Extract -->
      <div class="bg-gradient-to-br from-white to-[#FFF7ED] rounded-3xl p-6 border border-orange-100 shadow-sm hover:shadow-md transition-all flex items-start gap-4 group">
        <div class="w-12 h-12 rounded-2xl bg-orange-100 text-orange-700 flex items-center justify-center shrink-0 group-hover:scale-110 transition-transform">
          <span class="material-symbols-outlined text-2xl">local_fire_department</span>
        </div>
        <div>
          <h4 class="font-bold text-lg text-[#1A1A2E] mb-1">Ginger Extract</h4>
          <p class="text-xs font-semibold text-orange-700 uppercase tracking-wide mb-2">Spicy kick & anti-inflammatory</p>
          <p class="text-gray-600 text-xs sm:text-sm leading-relaxed">
            Cold-extracted raw ginger root delivers zesty aromatic warmth and active gingerols known for supporting digestion and joint ease.
          </p>
        </div>
      </div>

      <!-- 6. Turmeric Root -->
      <div class="bg-gradient-to-br from-white to-[#FEFCE8] rounded-3xl p-6 border border-yellow-100 shadow-sm hover:shadow-md transition-all flex items-start gap-4 group">
        <div class="w-12 h-12 rounded-2xl bg-yellow-100 text-yellow-700 flex items-center justify-center shrink-0 group-hover:scale-110 transition-transform">
          <span class="material-symbols-outlined text-2xl">hotel_class</span>
        </div>
        <div>
          <h4 class="font-bold text-lg text-[#1A1A2E] mb-1">Turmeric Root</h4>
          <p class="text-xs font-semibold text-yellow-700 uppercase tracking-wide mb-2">Powerful antioxidant & immunity booster</p>
          <p class="text-gray-600 text-xs sm:text-sm leading-relaxed">
            Rich in golden curcumin, turmeric root provides deep cellular defense, supports radiant vitality, and strengthens overall immunity.
          </p>
        </div>
      </div>

    </div>
  </section>

  <!-- SECTION: SOURCING PHILOSOPHY & QUALITY STANDARD -->
  <section class="max-w-[1280px] mx-auto px-4 sm:px-6 lg:px-8 mb-16">
    <div class="bg-gradient-to-br from-[#1A1A2E] to-[#252542] rounded-[36px] p-8 sm:p-12 lg:p-16 text-white shadow-xl relative overflow-hidden">
      <!-- Decorative background circles -->
      <div class="absolute -right-20 -bottom-20 w-80 h-80 bg-[#F9A602]/15 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -left-20 -top-20 w-80 h-80 bg-[#7CB342]/15 rounded-full blur-3xl pointer-events-none"></div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center relative z-10">
        <div class="lg:col-span-6">
          <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white/10 text-[#F9A602] text-xs font-bold uppercase tracking-wider mb-4 border border-white/15">
            <span class="material-symbols-outlined text-[15px]">verified</span> Our Unwavering Standards
          </span>
          <h3 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-5 leading-tight">
            Our Sourcing Philosophy
          </h3>
          <p class="text-gray-300 text-sm sm:text-base leading-relaxed mb-6">
            We believe the best juices start with the best ingredients. That’s why we source only organic, non-GMO produce from certified sustainable farms. We partner directly with growers who share our commitment to quality, nutrition, and environmental stewardship.
          </p>
          <div class="flex gap-4">
            <div class="w-12 h-12 rounded-full bg-white/10 flex items-center justify-center text-[#7CB342] border border-white/15">
              <span class="material-symbols-outlined text-2xl">verified</span>
            </div>
            <div class="w-12 h-12 rounded-full bg-white/10 flex items-center justify-center text-[#F9A602] border border-white/15">
              <span class="material-symbols-outlined text-2xl">nature</span>
            </div>
            <div class="w-12 h-12 rounded-full bg-white/10 flex items-center justify-center text-[#7CB342] border border-white/15">
              <span class="material-symbols-outlined text-2xl">public</span>
            </div>
          </div>
        </div>

        <div class="lg:col-span-6 flex flex-col gap-4">
          <div class="bg-white/10 backdrop-blur-md border border-white/15 p-5 rounded-2xl flex items-start gap-4">
            <span class="material-symbols-outlined text-[#7CB342] text-2xl shrink-0 mt-0.5" style="font-variation-settings: 'FILL' 1;">check_circle</span>
            <div>
              <h4 class="font-bold text-white text-base mb-1">100% Certified Organic</h4>
              <p class="text-gray-300 text-xs sm:text-sm leading-relaxed">Grown without synthetic pesticides or fertilizers, ensuring pure, clean nutrition for growing bodies.</p>
            </div>
          </div>
          <div class="bg-white/10 backdrop-blur-md border border-white/15 p-5 rounded-2xl flex items-start gap-4">
            <span class="material-symbols-outlined text-[#F9A602] text-2xl shrink-0 mt-0.5" style="font-variation-settings: 'FILL' 1;">check_circle</span>
            <div>
              <h4 class="font-bold text-white text-base mb-1">Non-GMO Project Verified</h4>
              <p class="text-gray-300 text-xs sm:text-sm leading-relaxed">Committed to natural agriculture. Our fruits and vegetables are never genetically modified.</p>
            </div>
          </div>
          <div class="bg-white/10 backdrop-blur-md border border-white/15 p-5 rounded-2xl flex items-start gap-4">
            <span class="material-symbols-outlined text-[#7CB342] text-2xl shrink-0 mt-0.5" style="font-variation-settings: 'FILL' 1;">check_circle</span>
            <div>
              <h4 class="font-bold text-white text-base mb-1">Sustainably Sourced</h4>
              <p class="text-gray-300 text-xs sm:text-sm leading-relaxed">We prioritize family-owned farms that practice soil regeneration, water conservation, and renewable energy.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>'''

for path in ['site/public/ingredients.html', '.stitch/designs/ingredients.html']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    new_c = re.sub(r'<main.*?</main>', INGREDIENTS_CONTENT, c, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Updated {path}")

print("Ingredients page updated successfully!")
