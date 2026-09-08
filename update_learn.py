import re

LEARN_SECTION = '''<main class="flex-grow w-full py-8">
  <!-- 4 Pillars Section: Our Mission, Our Owner Petunia, Mood Enhancers, Farm Fresh -->
  <section class="py-16 w-full bg-gradient-to-b from-white via-white to-[#E0F2FE]/50 overflow-hidden">
    <div class="max-w-[1360px] mx-auto px-6">
      
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 xl:gap-10 items-start text-center">
        
        <!-- Column 1: Our Mission -->
        <div class="flex flex-col items-center h-full">
          <div class="inline-block px-8 py-2.5 rounded-full border-2 border-[#2E7D32] bg-white text-[#2E7D32] font-bold text-base md:text-lg mb-8 shadow-xs whitespace-nowrap">
            Our Mission
          </div>
          <p class="text-[#D97706] text-sm md:text-[15px] leading-relaxed mb-8 flex-grow">
            We are committed to providing organic, plant-based juices that refresh, nourish,heal and energize your body. Our mission is to offer high-quality, nutritious drinks that benefit both your health and the planet.
          </p>
          <div class="w-full aspect-[16/10] rounded-3xl overflow-hidden shadow-md group hover:shadow-xl transition-all duration-300 mt-auto">
            <img src="images/learn-mission.jpg" alt="Our Mission Landscape" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
          </div>
        </div>

        <!-- Column 2: Our Owner Petunia -->
        <div class="flex flex-col items-center h-full">
          <div class="inline-block px-8 py-2.5 rounded-full border-2 border-[#2E7D32] bg-white text-[#2E7D32] font-bold text-base md:text-lg mb-8 shadow-xs whitespace-nowrap">
            Our Owner Petunia
          </div>
          <div class="w-full aspect-[16/10] rounded-3xl overflow-hidden shadow-md group hover:shadow-xl transition-all duration-300 mb-8">
            <img src="images/learn-owner.jpg" alt="Our Owner Petunia" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
          </div>
          <p class="text-[#D97706] text-sm md:text-[15px] leading-relaxed flex-grow">
            the heart of Penny Juice, Petunia. a wellness advocate and juice enthusiast who believes that good health starts with simple, natural ingredients. Inspired by her love for fresh fruits, vibrant flavors, and holistic well-being.
          </p>
        </div>

        <!-- Column 3: Mood Enhancers -->
        <div class="flex flex-col items-center h-full">
          <div class="inline-block px-8 py-2.5 rounded-full border-2 border-[#2E7D32] bg-white text-[#2E7D32] font-bold text-base md:text-lg mb-8 shadow-xs whitespace-nowrap">
            Mood Enhancers
          </div>
          <p class="text-[#D97706] text-sm md:text-[15px] leading-relaxed mb-8 flex-grow">
            Our special blends of fruits and vegetables are designed to naturally boost your mood and energy levels while boosting your mood and spirit. Discover the power of organic ingredients that nourish both body and mind.
          </p>
          <div class="w-full aspect-[16/10] rounded-3xl overflow-hidden shadow-md group hover:shadow-xl transition-all duration-300 mt-auto">
            <img src="images/learn-mood.jpg" alt="Mood Enhancers Kiwi" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
          </div>
        </div>

        <!-- Column 4: Farm Fresh -->
        <div class="flex flex-col items-center h-full">
          <div class="inline-block px-8 py-2.5 rounded-full border-2 border-[#2E7D32] bg-white text-[#2E7D32] font-bold text-base md:text-lg mb-8 shadow-xs whitespace-nowrap">
            Farm Fresh
          </div>
          <div class="w-full aspect-[16/10] rounded-3xl overflow-hidden shadow-md group hover:shadow-xl transition-all duration-300 mb-8">
            <img src="images/learn-farm.jpg" alt="Farm Fresh Mangoes" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
          </div>
          <p class="text-[#D97706] text-sm md:text-[15px] leading-relaxed flex-grow">
            We source our ingredients from sustainable farms to ensure every bottle of Penny Juice is fresh, organic, and good for the environment. Learn more about our farm-to-bottle process.
          </p>
        </div>

      </div>

      <!-- Trust Badges Row -->
      <div class="mt-20 grid grid-cols-1 sm:grid-cols-3 gap-6 max-w-4xl mx-auto pt-10 border-t border-slate-200/60">
        <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 text-center">
          <span class="material-symbols-outlined text-[#F9A602] text-4xl mb-2" style="font-variation-settings: 'FILL' 1;">eco</span>
          <h4 class="font-extrabold text-2xl text-[#1A1A2E] mb-1">100%</h4>
          <p class="text-xs text-gray-500 font-bold uppercase tracking-wider">Certified Organic</p>
        </div>
        <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 text-center">
          <span class="material-symbols-outlined text-[#2E7D32] text-4xl mb-2" style="font-variation-settings: 'FILL' 1;">blender</span>
          <h4 class="font-extrabold text-2xl text-[#1A1A2E] mb-1">8 Signature</h4>
          <p class="text-xs text-gray-500 font-bold uppercase tracking-wider">Cold-Pressed Blends</p>
        </div>
        <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 text-center">
          <span class="material-symbols-outlined text-[#F9A602] text-4xl mb-2" style="font-variation-settings: 'FILL' 1;">group</span>
          <h4 class="font-extrabold text-2xl text-[#1A1A2E] mb-1">50,000+</h4>
          <p class="text-xs text-gray-500 font-bold uppercase tracking-wider">Happy Wellness Seekers</p>
        </div>
      </div>

    </div>
  </section>
</main>'''

for path in ['site/public/learn.html', '.stitch/designs/learn.html']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Replace <main> ... </main>
    new_c = re.sub(r'<main.*?</main>', LEARN_SECTION, c, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Updated {path}")

print("Learn page updated successfully!")
