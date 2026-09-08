import filecmp

faq_site = r'd:\ICT\UX\Penny-Juice\site\public\faq.html'
faq_stitch = r'd:\ICT\UX\Penny-Juice\.stitch\designs\faq.html'

simplified_faq_html = """<!DOCTYPE html>
<html class="scroll-smooth" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Frequently Asked Questions - Penny Juice</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script id="tailwind-config">
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "primary": "#F9A602",
        "primary-container": "#F9A602",
        "secondary": "#7CB342",
        "secondary-container": "#7CB342",
        "background": "#F8FAFC",
        "on-background": "#1A1A2E",
        "surface": "#ffffff",
        "surface-variant": "#f1f5f9",
        "on-surface-variant": "#64748B"
      }
    }
  }
}
</script>
<style id="pj-master-style">
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
*{box-sizing:border-box;}
body{font-family:'Poppins',sans-serif!important;background:#F8FAFC;color:#1A1A2E;margin:0;padding:0;overflow-x:hidden;}

/* SINGLE UNIFIED TOP NAVBAR */
.pj-nav{position:sticky;top:0;left:0;right:0;width:100%;z-index:9999;background:#ffffff;border-bottom:1px solid #F1F5F9;box-shadow:0 2px 10px rgba(0,0,0,0.03);height:72px;display:flex;align-items:center;font-family:'Poppins',sans-serif;}
.pj-nav .pj-inner{max-width:1280px;margin:0 auto;width:100%;padding:0 32px;display:flex;align-items:center;justify-content:space-between;}
.pj-logo{font-size:22px;font-weight:800;color:#F9A602;text-decoration:none;display:flex;align-items:center;gap:6px;letter-spacing:-0.5px;transition:transform 0.2s;}
.pj-logo:hover{transform:scale(1.02);}
.pj-logo span{color:#1A1A2E;}
.pj-links{display:flex;align-items:center;gap:6px;list-style:none;margin:0;padding:0;}
.pj-links a{font-size:14px;font-weight:500;color:#64748B;text-decoration:none;padding:8px 16px;border-radius:50px;transition:all 0.2s;}
.pj-links a:hover{color:#F9A602;background:rgba(249,166,2,0.06);}
.pj-links a.active{color:#F9A602;background:#FFF7E6;font-weight:600;}
.pj-icons{display:flex;align-items:center;gap:8px;}
.pj-icons a{font-size:13px;font-weight:500;color:#64748B;text-decoration:none;padding:8px;width:36px;height:36px;justify-content:center;border-radius:50px;transition:all 0.2s;display:flex;align-items:center;gap:6px;}
.pj-icons a.pj-cart{width:auto;padding:8px 16px;}
.pj-icons a:hover{background:#FFF7E6;color:#F9A602;}
.pj-icons a.active{color:#F9A602;background:#FFF7E6;font-weight:600;}
.pj-icons .pj-cart{background:linear-gradient(135deg,#F9A602,#FF7043);color:#ffffff!important;font-weight:600;box-shadow:0 4px 12px rgba(249,166,2,0.25);}
.pj-icons .pj-cart:hover{opacity:0.92;box-shadow:0 6px 18px rgba(249,166,2,0.35);color:#ffffff!important;}
@media(max-width:860px){.pj-links{display:none;}.pj-icons a:not(.pj-cart){display:none;}.pj-nav .pj-inner{padding:0 20px;}}

/* 100% FULL-WIDTH COVER BANNER */
.pj-hero-banner{position:relative;width:100%;min-height:280px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;overflow:hidden;padding:60px 24px;box-sizing:border-box;margin:0;left:0;right:0;}
.pj-hero-banner .pj-hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;z-index:0;}
.pj-hero-banner .pj-hero-overlay{position:absolute;inset:0;z-index:1;}
.pj-hero-banner .pj-hero-content{position:relative;z-index:2;max-width:760px;margin:0 auto;text-align:center;}
.pj-hero-banner .pj-hero-breadcrumb{font-size:12px;font-weight:700;letter-spacing:0.12em;color:#C8E6C9;margin:0 0 10px;text-transform:uppercase;display:inline-block;}
.pj-hero-banner h1{font-size:clamp(30px,4.5vw,48px);font-weight:800;color:#ffffff;line-height:1.15;margin:0 0 12px;text-shadow:0 3px 20px rgba(0,0,0,0.35);letter-spacing:-0.5px;}
.pj-hero-banner p{font-size:16px;color:rgba(255,255,255,0.95);max-width:560px;margin:0 auto;line-height:1.6;text-shadow:0 2px 10px rgba(0,0,0,0.25);}

/* SIMPLE ACCORDION STYLES */
details summary::-webkit-details-marker {
  display: none;
}
details[open] summary .chevron-icon {
  transform: rotate(180deg);
  color: #F9A602;
}
</style>
</head>
<body class="antialiased min-h-screen flex flex-col bg-[#F8FAFC]">

<!-- SINGLE UNIFIED TOP NAVBAR -->
<nav class="pj-nav" id="pj-main-nav">
  <div class="pj-inner">
    <a href="index.html" class="pj-logo">🍊 Penny<span>Juice</span></a>
    <ul class="pj-links">
      <li><a href="shop.html">Shop</a></li>
      <li><a href="learn.html">Learn</a></li>
      <li><a href="ingredients.html">Ingredients</a></li>
      <li><a href="blog.html">Blog</a></li>
      <li><a href="contact.html">Contact</a></li>
      <li><a href="faq.html" class="active">FAQ</a></li>
    </ul>
    <div class="pj-icons">
      <a href="search.html" title="Search"><span class="material-symbols-outlined">search</span></a>
      <a href="login.html" title="Login"><span class="material-symbols-outlined">person</span></a>
      <a href="cart.html" class="pj-cart" title="Cart"><span class="material-symbols-outlined">shopping_cart</span> (3)</a>
    </div>
  </div>
</nav>

<!-- 100% FULL-WIDTH COVER BANNER -->
<div class="pj-hero-banner">
  <div class="pj-hero-bg" style="background-image:url('images/faq-fruits-splash.jpg');"></div>
  <div class="pj-hero-overlay" style="background:linear-gradient(135deg, rgba(26,26,46,0.85) 0%, rgba(124,179,66,0.8) 100%);"></div>
  <div class="pj-hero-content">
    <span class="pj-hero-breadcrumb">HOME › FAQ</span>
    <h1>Frequently Asked Questions</h1>
    <p>Find simple and fast answers to common questions about our organic juices, ingredients, and delivery.</p>
  </div>
</div>

<main class="flex-grow max-w-[860px] mx-auto w-full px-4 sm:px-6 lg:px-8 py-12">

  <!-- SIMPLE 6 QUESTIONS ACCORDION LIST -->
  <div class="space-y-4 mb-16">

    <!-- Question 1 -->
    <details class="group bg-white rounded-2xl border border-slate-100 p-6 shadow-[0_2px_12px_rgba(26,26,46,0.04)] hover:shadow-md transition-all" open>
      <summary class="flex justify-between items-center gap-4 cursor-pointer list-none select-none">
        <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] group-hover:text-[#F9A602] transition-colors">
          Are your juices 100% organic with no added sugar?
        </h3>
        <span class="material-symbols-outlined chevron-icon text-slate-400 text-xl transition-transform duration-200">expand_more</span>
      </summary>
      <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-sm leading-relaxed">
        Yes! All Penny Juice products are made from 100% real fruit juice concentrates and wholesome purees. We never add refined sugars, high-fructose corn syrup, artificial colors, or preservatives.
      </div>
    </details>

    <!-- Question 2 -->
    <details class="group bg-white rounded-2xl border border-slate-100 p-6 shadow-[0_2px_12px_rgba(26,26,46,0.04)] hover:shadow-md transition-all">
      <summary class="flex justify-between items-center gap-4 cursor-pointer list-none select-none">
        <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] group-hover:text-[#F9A602] transition-colors">
          How long do the juices last in the freezer and fridge?
        </h3>
        <span class="material-symbols-outlined chevron-icon text-slate-400 text-xl transition-transform duration-200">expand_more</span>
      </summary>
      <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-sm leading-relaxed space-y-2">
        <p>Unopened concentrate cartons stay fresh for up to <strong>12 months</strong> in the freezer. Once thawed and kept refrigerated unopened, cartons last for <strong>45 days</strong>. Once mixed with water, drink within <strong>5 to 7 days</strong> for best taste.</p>
      </div>
    </details>

    <!-- Question 3 -->
    <details class="group bg-white rounded-2xl border border-slate-100 p-6 shadow-[0_2px_12px_rgba(26,26,46,0.04)] hover:shadow-md transition-all">
      <summary class="flex justify-between items-center gap-4 cursor-pointer list-none select-none">
        <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] group-hover:text-[#F9A602] transition-colors">
          How do I prepare and mix Penny Juice?
        </h3>
        <span class="material-symbols-outlined chevron-icon text-slate-400 text-xl transition-transform duration-200">expand_more</span>
      </summary>
      <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-sm leading-relaxed">
        Thaw the concentrate carton in your refrigerator. Pour the carton into a pitcher, mix with 7 equal parts cold filtered water (7:1 ratio), stir well, and serve chilled!
      </div>
    </details>

    <!-- Question 4 -->
    <details class="group bg-white rounded-2xl border border-slate-100 p-6 shadow-[0_2px_12px_rgba(26,26,46,0.04)] hover:shadow-md transition-all">
      <summary class="flex justify-between items-center gap-4 cursor-pointer list-none select-none">
        <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] group-hover:text-[#F9A602] transition-colors">
          Do you ship nationwide, and how is it kept cold?
        </h3>
        <span class="material-symbols-outlined chevron-icon text-slate-400 text-xl transition-transform duration-200">expand_more</span>
      </summary>
      <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-sm leading-relaxed">
        Yes, we ship across all 50 US states. Orders are shipped in insulated thermal coolers with reusable refrigerant gel packs so your juice arrives icy and fresh in 2–3 business days.
      </div>
    </details>

    <!-- Question 5 -->
    <details class="group bg-white rounded-2xl border border-slate-100 p-6 shadow-[0_2px_12px_rgba(26,26,46,0.04)] hover:shadow-md transition-all">
      <summary class="flex justify-between items-center gap-4 cursor-pointer list-none select-none">
        <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] group-hover:text-[#F9A602] transition-colors">
          Are Penny Juice flavors allergen-free?
        </h3>
        <span class="material-symbols-outlined chevron-icon text-slate-400 text-xl transition-transform duration-200">expand_more</span>
      </summary>
      <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-sm leading-relaxed">
        Yes! All of our juices are 100% gluten-free, peanut-free, tree nut-free, dairy-free, and soy-free. They are safe for children and anyone with common food sensitivities.
      </div>
    </details>

    <!-- Question 6 -->
    <details class="group bg-white rounded-2xl border border-slate-100 p-6 shadow-[0_2px_12px_rgba(26,26,46,0.04)] hover:shadow-md transition-all">
      <summary class="flex justify-between items-center gap-4 cursor-pointer list-none select-none">
        <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] group-hover:text-[#F9A602] transition-colors">
          What is your return and freshness guarantee?
        </h3>
        <span class="material-symbols-outlined chevron-icon text-slate-400 text-xl transition-transform duration-200">expand_more</span>
      </summary>
      <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-sm leading-relaxed">
        We offer a 100% Fresh-Arrival Guarantee. If any carton arrives thawed or damaged during transit, let us know within 48 hours and we will send a free replacement or issue a full refund immediately.
      </div>
    </details>

  </div>

  <!-- SIMPLE "STILL HAVE QUESTIONS?" CARD -->
  <div class="bg-white rounded-3xl p-8 sm:p-10 text-center border border-slate-100 shadow-[0_4px_24px_rgba(26,26,46,0.05)] max-w-xl mx-auto">
    <div class="w-14 h-14 rounded-full bg-amber-50 text-[#F9A602] flex items-center justify-center mx-auto mb-4">
      <span class="material-symbols-outlined text-2xl">help_outline</span>
    </div>
    <h3 class="text-xl font-bold text-[#1A1A2E] mb-2">Still Have Questions?</h3>
    <p class="text-sm text-slate-500 mb-6 leading-relaxed">
      Can't find the answer you're looking for? Our friendly team is ready to help you anytime.
    </p>
    <div class="flex flex-col sm:flex-row items-center justify-center gap-3">
      <a href="contact.html" class="w-full sm:w-auto px-6 py-3 rounded-full bg-[#F9A602] hover:bg-[#e69902] text-white text-xs font-bold shadow-md hover:shadow-lg transition-all flex items-center justify-center gap-2">
        <span class="material-symbols-outlined text-base">mail</span> Send Us a Message
      </a>
      <a href="tel:7025550123" class="w-full sm:w-auto px-6 py-3 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition-all flex items-center justify-center gap-2">
        <span class="material-symbols-outlined text-base">call</span> (702) 555-0123
      </a>
    </div>
  </div>

</main>

<!-- UNIFIED FOOTER -->
<footer class="bg-[#1A1A2E] text-white w-full py-16 mt-auto font-['Poppins']">
  <div class="max-w-[1280px] mx-auto px-6 grid grid-cols-1 md:grid-cols-4 gap-12">
    <div class="flex flex-col gap-4">
      <a href="index.html" class="text-2xl font-black text-[#F9A602] tracking-tight flex items-center gap-2">
        🍊 Penny<span class="text-white">Juice</span>
      </a>
      <p class="text-gray-400 text-sm leading-relaxed max-w-[250px]">
        Vibrant, health-conscious organic juices delivered fresh to your door. Taste the difference of pure nature.
      </p>
      <div class="flex gap-4 mt-2">
        <a href="#" class="text-gray-400 hover:text-[#F9A602] transition-colors">
          <span class="material-symbols-outlined">share</span>
        </a>
        <a href="#" class="text-gray-400 hover:text-[#F9A602] transition-colors">
          <span class="material-symbols-outlined">thumb_up</span>
        </a>
      </div>
    </div>
    <div class="flex flex-col gap-3">
      <h4 class="font-bold text-lg mb-2 text-white">Shop</h4>
      <a class="text-gray-400 hover:text-[#F9A602] transition-colors text-sm" href="shop.html">All Juices</a>
      <a class="text-gray-400 hover:text-[#F9A602] transition-colors text-sm" href="learn.html">Our Process</a>
      <a class="text-gray-400 hover:text-[#F9A602] transition-colors text-sm" href="ingredients.html">Ingredients</a>
    </div>
    <div class="flex flex-col gap-3">
      <h4 class="font-bold text-lg mb-2 text-white">Company</h4>
      <a class="text-gray-400 hover:text-[#F9A602] transition-colors text-sm" href="blog.html">Blog</a>
      <a class="text-gray-400 hover:text-[#F9A602] transition-colors text-sm" href="contact.html">Contact Us</a>
      <a class="text-gray-400 hover:text-[#F9A602] transition-colors text-sm" href="faq.html">FAQ</a>
    </div>
    <div class="flex flex-col gap-3">
      <h4 class="font-bold text-lg mb-2 text-white">Newsletter</h4>
      <p class="text-gray-400 text-sm">Subscribe to get 10% off your first order!</p>
      <div class="flex mt-2">
        <input type="email" placeholder="Your email" class="bg-white/10 text-white px-4 py-2 rounded-l-full outline-none focus:bg-white/20 transition-colors w-full text-sm">
        <button class="bg-gradient-to-r from-[#F9A602] to-[#FF7043] px-4 py-2 rounded-r-full font-bold text-sm hover:opacity-90 transition-opacity whitespace-nowrap text-white">Subscribe</button>
      </div>
    </div>
  </div>
  <div class="max-w-[1280px] mx-auto px-6 mt-16 pt-8 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-4">
    <p class="text-gray-500 text-sm">© 2026 Penny Juice. All rights reserved.</p>
    <div class="flex gap-6">
      <a class="text-gray-500 hover:text-white transition-colors text-sm" href="#">Privacy Policy</a>
      <a class="text-gray-500 hover:text-white transition-colors text-sm" href="#">Terms of Service</a>
      <a class="text-gray-500 hover:text-white transition-colors text-sm" href="#">Shipping Info</a>
    </div>
  </div>
</footer>

</body>
</html>
"""

with open(faq_site, 'w', encoding='utf-8') as f:
    f.write(simplified_faq_html)

with open(faq_stitch, 'w', encoding='utf-8') as f:
    f.write(simplified_faq_html)

print("FAQ files equal:", filecmp.cmp(faq_site, faq_stitch))
print("Successfully simplified faq.html across site and stitch!")
