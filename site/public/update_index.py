import os

html_content = """<!-- FULL-WIDTH LANDING HERO -->
<section class="w-full relative min-h-[700px] flex items-center overflow-hidden">
  <!-- Split Background -->
  <div class="absolute inset-0 flex flex-col z-0">
    <div class="flex-1 bg-white"></div>
    <div class="flex-1 bg-[#F9A602]"></div>
  </div>
  
  <div class="max-w-[1280px] mx-auto w-full relative z-10 px-6 sm:px-8 grid grid-cols-1 md:grid-cols-3 gap-8 items-center pt-10 pb-20">
    <!-- Left Text Content -->
    <div class="flex flex-col gap-6 order-2 md:order-1 z-20">
      <div class="text-[#1A1A2E]">
        <h1 class="text-5xl lg:text-7xl font-extrabold leading-tight tracking-tight">
          Pure.<br/>Natural.<br/>Refreshing.
        </h1>
        <p class="text-sm text-gray-500 font-medium uppercase tracking-wider mt-4">100% Pure Organic Cold-Pressed</p>
      </div>
      <div class="mt-8">
        <a href="shop.html" class="inline-block px-8 py-4 bg-white text-[#F9A602] border-2 border-[#F9A602] font-bold text-sm rounded-full shadow-lg hover:bg-[#F9A602] hover:text-white transition-all tracking-wide">
          SHOP ALL JUICES
        </a>
      </div>
      <div class="mt-20 md:mt-32 text-white/90 text-sm max-w-[200px] font-medium leading-relaxed">
        For distribution and make a new cooperation &ndash; write to us
      </div>
    </div>
    
    <!-- Center Bottle -->
    <div class="relative h-[500px] md:h-[700px] flex items-center justify-center order-1 md:order-2 z-10 -my-10">
      <img alt="Penny Juice Bottle" class="w-full h-full object-contain drop-shadow-2xl hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCuupm__mltgZ0sjvDm9fGM3ruKRJ5MdAt8mQbOZE9MYauPkNk5QvvIpa6vOdxrCBv-aMe2Yc0wrlgwzNF850mo1-xKdD6dPKbCH8V9Z-pGw2WWtxdMklhsakYjH7D36MrbDodtXcs0W0eQuyRPj7yJRzdAqSm7tLB2IeYGDUQU0s5sdTLEFg6rJn3sH4q-uytMm5LVuIYDkEJfwek3MtFKvcXWeCVgohWsUPxPzRUiQCSnKP2ZOou2vzBXk2R2tr_aCsm-w5QGtaI"/>
    </div>
    
    <!-- Right Text Content -->
    <div class="flex flex-col gap-6 order-3 md:order-3 z-20 md:text-right">
      <div class="text-[#1A1A2E]">
        <p class="text-xs text-gray-400 font-bold uppercase tracking-widest mb-2">Ingredients</p>
        <p class="text-lg font-bold leading-snug">
          Organic plant-based juices crafted for your daily wellness journey.
        </p>
        <div class="flex gap-2 mt-4 md:justify-end">
          <span class="px-4 py-1.5 bg-[#FFF7E6] text-[#F9A602] rounded-full text-xs font-bold">330 ml</span>
          <span class="px-4 py-1.5 bg-[#FFF7E6] text-[#F9A602] rounded-full text-xs font-bold">500 ml</span>
        </div>
      </div>
      <div class="mt-20 md:mt-40 text-white/90 text-sm max-w-[250px] md:ml-auto font-medium leading-relaxed">
        Sourced fresh from sustainable family farms with zero additives. Good for you and good for the planet.
      </div>
    </div>
  </div>
</section>

<main class="flex-grow w-full">
<!-- Most Popular Flavors -->
<section class="py-24 bg-white w-full overflow-hidden text-center">
  <div class="max-w-[1280px] mx-auto px-6">
    <p class="text-xs text-[#F9A602] font-bold uppercase tracking-widest mb-2">MOST POPULAR</p>
    <h2 class="text-4xl font-extrabold text-[#1A1A2E] mb-4">Most Popular Flavors</h2>
    <p class="text-gray-500 max-w-lg mx-auto mb-16">Our customers' top-rated cold-pressed blends, crafted fresh with real fruits and 100% organic ingredients.</p>
    
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
      <!-- Product Card: Kiwi Vitality -->
      <div class="product-card group relative bg-white rounded-3xl p-4 border border-slate-100 shadow-[0_4px_20px_rgba(0,0,0,0.05)] hover:shadow-[0_16px_35px_rgba(249,166,2,0.18)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between" data-title="Kiwi Vitality" data-category="Green" data-tags="kiwi apple lime ginger green cold-pressed bestseller organic vitality" data-price="8.99">
        <!-- Top Left: Add to Cart Icon Button -->
        <button type="button" aria-label="Add Kiwi Vitality to cart" class="add-to-cart-btn absolute top-4 left-4 z-20 w-10 h-10 rounded-full bg-white/95 backdrop-blur shadow-md border border-slate-100 flex items-center justify-center text-[#1A1A2E] hover:bg-[#F9A602] hover:text-white hover:border-[#F9A602] hover:scale-110 active:scale-95 transition-all duration-200 cursor-pointer" title="Add to Cart" onclick="event.preventDefault(); event.stopPropagation(); window.pjAddToCart && window.pjAddToCart('Kiwi Vitality');">
          <span class="material-symbols-outlined text-[20px]">shopping_cart</span>
        </button>

        <!-- Top Right: Badge -->
        <div class="absolute top-4 right-4 z-20">
          <span class="inline-block bg-[#7CB342] text-white text-[10px] font-extrabold px-3 py-1 rounded-full uppercase tracking-wider shadow-xs">Best Seller</span>
        </div>

        <!-- Card Body: Image & Details -->
        <a href="product-detail.html" class="block focus:outline-none flex-grow">
          <div class="relative w-full aspect-square bg-gradient-to-b from-slate-50 to-white rounded-2xl p-4 flex items-center justify-center overflow-hidden mb-4 group-hover:bg-[#FFFDF7] transition-colors">
            <img alt="Kiwi Vitality" class="w-full h-full object-contain drop-shadow-md group-hover:scale-105 transition-transform duration-500" src="images/kiwi-vitality.jpeg"/>
          </div>
          
          <div class="px-1 text-left">
            <div class="flex items-center justify-between mb-1">
              <h3 class="font-bold text-lg text-[#1A1A2E] group-hover:text-[#F9A602] transition-colors leading-snug">Kiwi Vitality</h3>
              <div class="flex items-center text-[#F9A602] text-xs font-bold gap-0.5">
                <span class="material-symbols-outlined text-[14px]" style="font-variation-settings: 'FILL' 1;">star</span>
                <span>4.9</span>
              </div>
            </div>
            <p class="text-xs text-gray-500 line-clamp-1 mb-4">Kiwi, Apple, Lime, Ginger</p>
          </div>
        </a>

        <!-- Card Footer: Price & Buy Button -->
        <div class="mt-auto px-1 pt-3 border-t border-slate-100 flex items-center justify-between gap-3">
          <div>
            <span class="text-[10px] text-gray-400 block font-semibold uppercase tracking-wider leading-none mb-1">Price</span>
            <span class="text-xl font-extrabold text-[#1A1A2E]">$8.99</span>
          </div>
          <a href="product-detail.html" class="flex-1 max-w-[125px] py-2.5 px-4 bg-[#F9A602] hover:bg-[#E09400] text-white font-bold text-xs uppercase tracking-wider rounded-full shadow-sm hover:shadow-md transition-all flex items-center justify-center gap-1.5 active:scale-95 text-center">
            <span>Buy</span>
            <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
          </a>
        </div>
      </div>
      <!-- Product Card: Pineapple Pulse -->
      <div class="product-card group relative bg-white rounded-3xl p-4 border border-slate-100 shadow-[0_4px_20px_rgba(0,0,0,0.05)] hover:shadow-[0_16px_35px_rgba(249,166,2,0.18)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between" data-title="Pineapple Pulse" data-category="Citrus" data-tags="pineapple orange turmeric coconut water citrus immunity popular tropical" data-price="8.99">
        <!-- Top Left: Add to Cart Icon Button -->
        <button type="button" aria-label="Add Pineapple Pulse to cart" class="add-to-cart-btn absolute top-4 left-4 z-20 w-10 h-10 rounded-full bg-white/95 backdrop-blur shadow-md border border-slate-100 flex items-center justify-center text-[#1A1A2E] hover:bg-[#F9A602] hover:text-white hover:border-[#F9A602] hover:scale-110 active:scale-95 transition-all duration-200 cursor-pointer" title="Add to Cart" onclick="event.preventDefault(); event.stopPropagation(); window.pjAddToCart && window.pjAddToCart('Pineapple Pulse');">
          <span class="material-symbols-outlined text-[20px]">shopping_cart</span>
        </button>

        <!-- Top Right: Badge -->
        <div class="absolute top-4 right-4 z-20">
          <span class="inline-block bg-[#F9A602] text-white text-[10px] font-extrabold px-3 py-1 rounded-full uppercase tracking-wider shadow-xs">Popular</span>
        </div>

        <!-- Card Body: Image & Details -->
        <a href="product-detail.html" class="block focus:outline-none flex-grow">
          <div class="relative w-full aspect-square bg-gradient-to-b from-slate-50 to-white rounded-2xl p-4 flex items-center justify-center overflow-hidden mb-4 group-hover:bg-[#FFFDF7] transition-colors">
            <img alt="Pineapple Pulse" class="w-full h-full object-contain drop-shadow-md group-hover:scale-105 transition-transform duration-500" src="images/pineapple-pulse.jpeg"/>
          </div>
          
          <div class="px-1 text-left">
            <div class="flex items-center justify-between mb-1">
              <h3 class="font-bold text-lg text-[#1A1A2E] group-hover:text-[#F9A602] transition-colors leading-snug">Pineapple Pulse</h3>
              <div class="flex items-center text-[#F9A602] text-xs font-bold gap-0.5">
                <span class="material-symbols-outlined text-[14px]" style="font-variation-settings: 'FILL' 1;">star</span>
                <span>4.8</span>
              </div>
            </div>
            <p class="text-xs text-gray-500 line-clamp-1 mb-4">Pineapple, Orange, Turmeric, Coconut Water</p>
          </div>
        </a>

        <!-- Card Footer: Price & Buy Button -->
        <div class="mt-auto px-1 pt-3 border-t border-slate-100 flex items-center justify-between gap-3">
          <div>
            <span class="text-[10px] text-gray-400 block font-semibold uppercase tracking-wider leading-none mb-1">Price</span>
            <span class="text-xl font-extrabold text-[#1A1A2E]">$8.99</span>
          </div>
          <a href="product-detail.html" class="flex-1 max-w-[125px] py-2.5 px-4 bg-[#F9A602] hover:bg-[#E09400] text-white font-bold text-xs uppercase tracking-wider rounded-full shadow-sm hover:shadow-md transition-all flex items-center justify-center gap-1.5 active:scale-95 text-center">
            <span>Buy</span>
            <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
          </a>
        </div>
      </div>
      <!-- Product Card: Green Glow -->
      <div class="product-card group relative bg-white rounded-3xl p-4 border border-slate-100 shadow-[0_4px_20px_rgba(0,0,0,0.05)] hover:shadow-[0_16px_35px_rgba(249,166,2,0.18)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between" data-title="Green Glow" data-category="Green" data-tags="spinach kale green apple cucumber lemon green detox superfood glow" data-price="9.49">
        <!-- Top Left: Add to Cart Icon Button -->
        <button type="button" aria-label="Add Green Glow to cart" class="add-to-cart-btn absolute top-4 left-4 z-20 w-10 h-10 rounded-full bg-white/95 backdrop-blur shadow-md border border-slate-100 flex items-center justify-center text-[#1A1A2E] hover:bg-[#F9A602] hover:text-white hover:border-[#F9A602] hover:scale-110 active:scale-95 transition-all duration-200 cursor-pointer" title="Add to Cart" onclick="event.preventDefault(); event.stopPropagation(); window.pjAddToCart && window.pjAddToCart('Green Glow');">
          <span class="material-symbols-outlined text-[20px]">shopping_cart</span>
        </button>

        <!-- Top Right: Badge -->
        <div class="absolute top-4 right-4 z-20">
          <span class="inline-block bg-[#2E7D32] text-white text-[10px] font-extrabold px-3 py-1 rounded-full uppercase tracking-wider shadow-xs">Organic</span>
        </div>

        <!-- Card Body: Image & Details -->
        <a href="product-detail.html" class="block focus:outline-none flex-grow">
          <div class="relative w-full aspect-square bg-gradient-to-b from-slate-50 to-white rounded-2xl p-4 flex items-center justify-center overflow-hidden mb-4 group-hover:bg-[#FFFDF7] transition-colors">
            <img alt="Green Glow" class="w-full h-full object-contain drop-shadow-md group-hover:scale-105 transition-transform duration-500" src="images/green-glow.jpeg"/>
          </div>
          
          <div class="px-1 text-left">
            <div class="flex items-center justify-between mb-1">
              <h3 class="font-bold text-lg text-[#1A1A2E] group-hover:text-[#F9A602] transition-colors leading-snug">Green Glow</h3>
              <div class="flex items-center text-[#F9A602] text-xs font-bold gap-0.5">
                <span class="material-symbols-outlined text-[14px]" style="font-variation-settings: 'FILL' 1;">star</span>
                <span>4.9</span>
              </div>
            </div>
            <p class="text-xs text-gray-500 line-clamp-1 mb-4">Spinach, Kale, Green Apple, Cucumber, Lemon</p>
          </div>
        </a>

        <!-- Card Footer: Price & Buy Button -->
        <div class="mt-auto px-1 pt-3 border-t border-slate-100 flex items-center justify-between gap-3">
          <div>
            <span class="text-[10px] text-gray-400 block font-semibold uppercase tracking-wider leading-none mb-1">Price</span>
            <span class="text-xl font-extrabold text-[#1A1A2E]">$9.49</span>
          </div>
          <a href="product-detail.html" class="flex-1 max-w-[125px] py-2.5 px-4 bg-[#F9A602] hover:bg-[#E09400] text-white font-bold text-xs uppercase tracking-wider rounded-full shadow-sm hover:shadow-md transition-all flex items-center justify-center gap-1.5 active:scale-95 text-center">
            <span>Buy</span>
            <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
          </a>
        </div>
      </div>
      <!-- Product Card: Golden Aura -->
      <div class="product-card group relative bg-white rounded-3xl p-4 border border-slate-100 shadow-[0_4px_20px_rgba(0,0,0,0.05)] hover:shadow-[0_16px_35px_rgba(249,166,2,0.18)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between" data-title="Golden Aura" data-category="Citrus" data-tags="carrot orange turmeric pineapple citrus glow vitamin c aura golden" data-price="8.49">
        <!-- Top Left: Add to Cart Icon Button -->
        <button type="button" aria-label="Add Golden Aura to cart" class="add-to-cart-btn absolute top-4 left-4 z-20 w-10 h-10 rounded-full bg-white/95 backdrop-blur shadow-md border border-slate-100 flex items-center justify-center text-[#1A1A2E] hover:bg-[#F9A602] hover:text-white hover:border-[#F9A602] hover:scale-110 active:scale-95 transition-all duration-200 cursor-pointer" title="Add to Cart" onclick="event.preventDefault(); event.stopPropagation(); window.pjAddToCart && window.pjAddToCart('Golden Aura');">
          <span class="material-symbols-outlined text-[20px]">shopping_cart</span>
        </button>

        <!-- Top Right: Badge -->
        <div class="absolute top-4 right-4 z-20">
          <span class="inline-block bg-[#FF9800] text-white text-[10px] font-extrabold px-3 py-1 rounded-full uppercase tracking-wider shadow-xs">Bestseller</span>
        </div>

        <!-- Card Body: Image & Details -->
        <a href="product-detail.html" class="block focus:outline-none flex-grow">
          <div class="relative w-full aspect-square bg-gradient-to-b from-slate-50 to-white rounded-2xl p-4 flex items-center justify-center overflow-hidden mb-4 group-hover:bg-[#FFFDF7] transition-colors">
            <img alt="Golden Aura" class="w-full h-full object-contain drop-shadow-md group-hover:scale-105 transition-transform duration-500" src="images/golden-aura.jpeg"/>
          </div>
          
          <div class="px-1 text-left">
            <div class="flex items-center justify-between mb-1">
              <h3 class="font-bold text-lg text-[#1A1A2E] group-hover:text-[#F9A602] transition-colors leading-snug">Golden Aura</h3>
              <div class="flex items-center text-[#F9A602] text-xs font-bold gap-0.5">
                <span class="material-symbols-outlined text-[14px]" style="font-variation-settings: 'FILL' 1;">star</span>
                <span>4.8</span>
              </div>
            </div>
            <p class="text-xs text-gray-500 line-clamp-1 mb-4">Carrot, Orange, Turmeric, Pineapple</p>
          </div>
        </a>

        <!-- Card Footer: Price & Buy Button -->
        <div class="mt-auto px-1 pt-3 border-t border-slate-100 flex items-center justify-between gap-3">
          <div>
            <span class="text-[10px] text-gray-400 block font-semibold uppercase tracking-wider leading-none mb-1">Price</span>
            <span class="text-xl font-extrabold text-[#1A1A2E]">$8.49</span>
          </div>
          <a href="product-detail.html" class="flex-1 max-w-[125px] py-2.5 px-4 bg-[#F9A602] hover:bg-[#E09400] text-white font-bold text-xs uppercase tracking-wider rounded-full shadow-sm hover:shadow-md transition-all flex items-center justify-center gap-1.5 active:scale-95 text-center">
            <span>Buy</span>
            <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
          </a>
        </div>
      </div>
    </div>

    <div class="mt-14 text-center">
      <a href="shop.html" class="inline-flex items-center gap-2 px-8 py-3.5 rounded-full bg-[#1A1A2E] text-white hover:bg-[#F9A602] font-bold text-sm tracking-wide transition-all shadow-md hover:shadow-lg hover:scale-105 active:scale-95">
        <span>View All Flavors</span>
        <span class="material-symbols-outlined text-sm">arrow_forward</span>
      </a>
    </div>
  </div>
</section>

<!-- Ingredients -->
<section class="py-24 bg-[#FFF7E6] w-full">
  <div class="max-w-[1280px] mx-auto px-6 flex flex-col lg:flex-row gap-16 items-center">
    <div class="lg:w-1/3">
      <p class="text-xs text-[#F9A602] font-bold uppercase tracking-widest mb-2">INGREDIENTS</p>
      <h2 class="text-4xl font-extrabold text-[#1A1A2E] mb-4">Pure. Simple.<br/>Effective.</h2>
      <p class="text-gray-600">We use only high-quality ingredients to create a drink that's good for your body and your everyday performance.</p>
    </div>
    
    <div class="lg:w-2/3 grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
      <div class="flex flex-col items-center">
        <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center mb-4 shadow-sm text-[#F9A602]">
          <span class="material-symbols-outlined text-3xl">water_drop</span>
        </div>
        <h4 class="font-bold text-[#1A1A2E] mb-2 text-sm">Mineral Water</h4>
        <p class="text-xs text-gray-500">Hydrating and pure mineral water for maximum absorption.</p>
      </div>
      <div class="flex flex-col items-center">
        <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center mb-4 shadow-sm text-[#F9A602]">
          <span class="material-symbols-outlined text-3xl">nutrition</span>
        </div>
        <h4 class="font-bold text-[#1A1A2E] mb-2 text-sm">Real Fruit Juice</h4>
        <p class="text-xs text-gray-500">Made with real juice for natural flavor and nutrients.</p>
      </div>
      <div class="flex flex-col items-center">
        <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center mb-4 shadow-sm text-[#F9A602]">
          <span class="material-symbols-outlined text-3xl">eco</span>
        </div>
        <h4 class="font-bold text-[#1A1A2E] mb-2 text-sm">100% Organic</h4>
        <p class="text-xs text-gray-500">Sourced directly from sustainable farms with zero pesticides.</p>
      </div>
      <div class="flex flex-col items-center">
        <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center mb-4 shadow-sm text-[#F9A602]">
          <span class="material-symbols-outlined text-3xl">bolt</span>
        </div>
        <h4 class="font-bold text-[#1A1A2E] mb-2 text-sm">Energy Boost</h4>
        <p class="text-xs text-gray-500">Natural ingredients that help you stay active and alert.</p>
      </div>
    </div>
  </div>
</section>

<!-- About Section -->
<section class="py-24 bg-white w-full">
  <div class="max-w-[1280px] mx-auto px-6 flex flex-col md:flex-row gap-16 items-center">
    <div class="md:w-1/2 flex justify-center">
      <img alt="Penny Juice Splash" class="max-h-[500px] object-contain rounded-2xl shadow-sm" src="images/about-cartons.jpg"/>
    </div>
    
    <div class="md:w-1/2">
      <p class="text-xs text-[#F9A602] font-bold uppercase tracking-widest mb-2">ABOUT PENNY JUICE</p>
      <h2 class="text-4xl font-extrabold text-[#1A1A2E] mb-6">Designed for a<br/>Better You.</h2>
      <p class="text-gray-600 mb-10">Penny Juice was created with a simple purpose: to deliver clean, refreshing hydration that supports your active lifestyle. Whether you're at work, in the gym, or on the go &ndash; we keep you sharp, clean, and vital.</p>
      
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
        <div>
          <div class="w-12 h-12 rounded-full border border-[#F9A602]/30 flex items-center justify-center text-[#F9A602] mb-3">
             <span class="material-symbols-outlined text-xl">directions_run</span>
          </div>
          <h4 class="font-bold text-[#1A1A2E] text-sm mb-1">Boosts Energy</h4>
          <p class="text-xs text-gray-500">Natural ingredients for clean vitality.</p>
        </div>
        <div>
          <div class="w-12 h-12 rounded-full border border-[#F9A602]/30 flex items-center justify-center text-[#F9A602] mb-3">
             <span class="material-symbols-outlined text-xl">health_and_safety</span>
          </div>
          <h4 class="font-bold text-[#1A1A2E] text-sm mb-1">Antioxidant Rich</h4>
          <p class="text-xs text-gray-500">Protects cells and supports wellness.</p>
        </div>
        <div>
          <div class="w-12 h-12 rounded-full border border-[#F9A602]/30 flex items-center justify-center text-[#F9A602] mb-3">
             <span class="material-symbols-outlined text-xl">do_not_disturb</span>
          </div>
          <h4 class="font-bold text-[#1A1A2E] text-sm mb-1">Zero Sugar</h4>
          <p class="text-xs text-gray-500">Enjoy the taste without empty calories.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Contact Banner -->
<section class="py-12 bg-[#F9A602] w-full mt-auto">
  <div class="max-w-[1280px] mx-auto px-6 flex flex-col sm:flex-row items-center justify-between gap-6">
    <div class="flex items-center gap-6">
      <div class="w-16 h-16 rounded-full border border-white/40 flex items-center justify-center text-white shrink-0">
        <span class="material-symbols-outlined text-3xl">mail</span>
      </div>
      <p class="text-white text-lg font-medium">For distribution and make<br/>a new cooperation &mdash; write to us</p>
    </div>
    <a href="contact.html" class="px-8 py-3.5 bg-white text-[#F9A602] font-bold rounded-full hover:scale-105 transition-transform shadow-lg whitespace-nowrap">CONTACT US</a>
  </div>
</section>
</main>"""

for root_dir in [r'd:\ICT\UX\Penny-Juice\site\public', r'd:\ICT\UX\Penny-Juice\.stitch\designs']:
    file_path = os.path.join(root_dir, 'index.html')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # find <!-- FULL-WIDTH LANDING HERO --> and </main>
        start_idx = content.find('<!-- FULL-WIDTH LANDING HERO -->')
        end_idx = content.find('</main>')
        
        if start_idx != -1 and end_idx != -1:
            end_idx += len('</main>')
            new_content = content[:start_idx] + html_content + content[end_idx:]
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {file_path}')
        else:
            print(f'Tags not found in {file_path}')
