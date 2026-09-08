import os, shutil, filecmp

# Paths
contact_site = r'd:\ICT\UX\Penny-Juice\site\public\contact.html'
contact_stitch = r'd:\ICT\UX\Penny-Juice\.stitch\designs\contact.html'
faq_site = r'd:\ICT\UX\Penny-Juice\site\public\faq.html'
faq_stitch = r'd:\ICT\UX\Penny-Juice\.stitch\designs\faq.html'

# 1. GENERATE CONTACT HTML
contact_html = """<!DOCTYPE html>
<html class="scroll-smooth" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Contact Us & Juicery Lounge - Penny Juice</title>
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
.pj-hero-banner{position:relative;width:100%;min-height:340px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;overflow:hidden;padding:70px 24px;box-sizing:border-box;margin:0;left:0;right:0;}
.pj-hero-banner .pj-hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;z-index:0;transform:scale(1.03);transition:transform 6s ease-out;}
.pj-hero-banner:hover .pj-hero-bg{transform:scale(1.0);}
.pj-hero-banner .pj-hero-overlay{position:absolute;inset:0;z-index:1;}
.pj-hero-banner .pj-hero-content{position:relative;z-index:2;max-width:820px;margin:0 auto;text-align:center;}
.pj-hero-banner .pj-hero-breadcrumb{font-size:12px;font-weight:700;letter-spacing:0.12em;color:#FFE082;margin:0 0 12px;text-transform:uppercase;display:inline-block;}
.pj-hero-banner h1{font-size:clamp(32px,5vw,54px);font-weight:800;color:#ffffff;line-height:1.15;margin:0 0 16px;text-shadow:0 3px 20px rgba(0,0,0,0.35);letter-spacing:-0.5px;}
.pj-hero-banner p{font-size:17px;color:rgba(255,255,255,0.95);max-width:620px;margin:0 auto 20px;line-height:1.65;text-shadow:0 2px 10px rgba(0,0,0,0.25);}

/* CUSTOM TOAST NOTIFICATION */
#contactToast {
  position: fixed;
  bottom: 30px;
  right: 30px;
  z-index: 10000;
  transform: translateY(120%);
  opacity: 0;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
#contactToast.show {
  transform: translateY(0);
  opacity: 1;
}

.topic-btn.active {
  background: #F9A602 !important;
  color: #ffffff !important;
  border-color: #F9A602 !important;
  box-shadow: 0 4px 14px rgba(249,166,2,0.3);
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
      <li><a href="contact.html" class="active">Contact</a></li>
      <li><a href="faq.html">FAQ</a></li>
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
  <div class="pj-hero-bg" style="background-image:url('images/contact-lounge.jpg');"></div>
  <div class="pj-hero-overlay" style="background:linear-gradient(135deg, rgba(26,26,46,0.85) 0%, rgba(249,166,2,0.78) 100%);"></div>
  <div class="pj-hero-content">
    <span class="pj-hero-breadcrumb">HOME › CONTACT & TASTING LOUNGE</span>
    <h1>Let's Pour Fresh Ideas Together</h1>
    <p>Whether you're looking for daycare bulk distribution, have questions about cold-pressed nutrition, or want to visit our Las Vegas tasting lounge—we'd love to connect!</p>
    <div class="inline-flex items-center gap-2.5 px-5 py-2 rounded-full bg-white/20 backdrop-blur-md text-white text-xs font-semibold tracking-wide border border-white/30 shadow-lg">
      <span class="w-2.5 h-2.5 rounded-full bg-[#4ADE80] animate-pulse"></span>
      Care Team Online & Ready • Average Response Time &lt; 2 Hours
    </div>
  </div>
</div>

<main class="flex-grow max-w-[1280px] mx-auto w-full px-4 sm:px-6 lg:px-8 py-12">

  <!-- 4 PRIORITY CONTACT CHANNELS -->
  <section class="mb-14">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
      
      <!-- Card 1: Customer Care -->
      <div class="bg-white rounded-3xl p-6 border border-slate-100 shadow-[0_4px_24px_rgba(26,26,46,0.05)] hover:shadow-[0_12px_32px_rgba(249,166,2,0.12)] hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-amber-50 text-[#F9A602] flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-2xl">support_agent</span>
          </div>
          <span class="text-[11px] font-bold tracking-wider uppercase text-[#F9A602] bg-[#FFF7E6] px-2.5 py-1 rounded-full">General Inquiries</span>
          <h3 class="font-bold text-lg text-[#1A1A2E] mt-3 mb-1">Customer Care</h3>
          <p class="text-xs text-slate-500 mb-3">Live assistance for retail orders, subscriptions, and flavor guides.</p>
          <p class="font-bold text-sm text-[#1A1A2E]">(702) 555-0123</p>
          <p class="text-xs text-slate-400">hello@pennyjuice.com</p>
        </div>
        <div class="mt-5 pt-4 border-t border-slate-100 flex items-center justify-between">
          <span class="text-[11px] text-emerald-600 font-semibold flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span> 9am–6pm PST
          </span>
          <a href="tel:7025550123" class="text-xs font-bold text-[#F9A602] hover:underline flex items-center gap-0.5">Call Now →</a>
        </div>
      </div>

      <!-- Card 2: Daycare & Preschools -->
      <div class="bg-white rounded-3xl p-6 border border-slate-100 shadow-[0_4px_24px_rgba(26,26,46,0.05)] hover:shadow-[0_12px_32px_rgba(124,179,66,0.14)] hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#7CB342] flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-2xl">school</span>
          </div>
          <span class="text-[11px] font-bold tracking-wider uppercase text-[#7CB342] bg-emerald-50 px-2.5 py-1 rounded-full">Childcare Specialists</span>
          <h3 class="font-bold text-lg text-[#1A1A2E] mt-3 mb-1">Daycare & Schools</h3>
          <p class="text-xs text-slate-500 mb-3">CACFP compliant 100% fruit juice program with free mixing dispensers.</p>
          <p class="font-bold text-sm text-[#1A1A2E]">1-800-PENNY-JUICE</p>
          <p class="text-xs text-slate-400">daycare@pennyjuice.com</p>
        </div>
        <div class="mt-5 pt-4 border-t border-slate-100 flex items-center justify-between">
          <span class="text-[11px] text-slate-500 font-medium">Free Samples</span>
          <a href="#contact-form-section" onclick="selectTopic('daycare')" class="text-xs font-bold text-[#7CB342] hover:underline flex items-center gap-0.5">Get Free Kit →</a>
        </div>
      </div>

      <!-- Card 3: Wholesale & Logistics -->
      <div class="bg-white rounded-3xl p-6 border border-slate-100 shadow-[0_4px_24px_rgba(26,26,46,0.05)] hover:shadow-[0_12px_32px_rgba(255,112,67,0.12)] hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-orange-50 text-[#FF7043] flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-2xl">local_shipping</span>
          </div>
          <span class="text-[11px] font-bold tracking-wider uppercase text-[#FF7043] bg-orange-50 px-2.5 py-1 rounded-full">Nationwide B2B</span>
          <h3 class="font-bold text-lg text-[#1A1A2E] mt-3 mb-1">Bulk & Wholesale</h3>
          <p class="text-xs text-slate-500 mb-3">Palletized cold-chain logistics for grocers, gyms, and dining halls.</p>
          <p class="font-bold text-sm text-[#1A1A2E]">(702) 555-0199</p>
          <p class="text-xs text-slate-400">wholesale@pennyjuice.com</p>
        </div>
        <div class="mt-5 pt-4 border-t border-slate-100 flex items-center justify-between">
          <span class="text-[11px] text-slate-500 font-medium">50-State Logistics</span>
          <a href="#contact-form-section" onclick="selectTopic('wholesale')" class="text-xs font-bold text-[#FF7043] hover:underline flex items-center gap-0.5">Inquire →</a>
        </div>
      </div>

      <!-- Card 4: Media & Partnerships -->
      <div class="bg-white rounded-3xl p-6 border border-slate-100 shadow-[0_4px_24px_rgba(26,26,46,0.05)] hover:shadow-[0_12px_32px_rgba(99,102,241,0.12)] hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-indigo-50 text-indigo-600 flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-2xl">volunteer_activism</span>
          </div>
          <span class="text-[11px] font-bold tracking-wider uppercase text-indigo-600 bg-indigo-50 px-2.5 py-1 rounded-full">Community First</span>
          <h3 class="font-bold text-lg text-[#1A1A2E] mt-3 mb-1">Press & Collabs</h3>
          <p class="text-xs text-slate-500 mb-3">Brand partnerships, wellness events, organic farm initiatives, and media.</p>
          <p class="font-bold text-sm text-[#1A1A2E]">community@pennyjuice.com</p>
          <p class="text-xs text-slate-400">Media kit available upon request</p>
        </div>
        <div class="mt-5 pt-4 border-t border-slate-100 flex items-center justify-between">
          <span class="text-[11px] text-slate-500 font-medium">Press Kit</span>
          <a href="#contact-form-section" onclick="selectTopic('partnership')" class="text-xs font-bold text-indigo-600 hover:underline flex items-center gap-0.5">Connect →</a>
        </div>
      </div>

    </div>
  </section>

  <!-- MAIN CONTACT EXPERIENCE: INTERACTIVE FORM + FLAGSHIP JUICERY LOUNGE -->
  <section class="mb-16" id="contact-form-section">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
      
      <!-- Left Column: Interactive Form Studio (7 cols) -->
      <div class="lg:col-span-7 bg-white rounded-3xl p-8 sm:p-10 border border-slate-100 shadow-[0_8px_30px_rgba(26,26,46,0.06)]">
        <div class="flex items-center gap-3 mb-4">
          <span class="w-8 h-8 rounded-full bg-[#FFF7E6] text-[#F9A602] flex items-center justify-center font-bold text-sm">✍️</span>
          <span class="text-xs font-bold uppercase tracking-wider text-[#F9A602]">Quick Response Studio</span>
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-[#1A1A2E] mb-2">Send Us a Direct Message</h2>
        <p class="text-sm text-slate-500 mb-8 leading-relaxed">Tell us how we can brighten your day. Select an inquiry type below to ensure your message routes directly to the right specialist.</p>

        <!-- Topic Selector Pills -->
        <div class="mb-6">
          <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2.5">Select Your Inquiry Category</label>
          <div class="flex flex-wrap gap-2.5" id="topicButtons">
            <button type="button" onclick="selectTopic('general')" class="topic-btn active text-xs font-semibold px-4 py-2 rounded-full border border-slate-200 text-slate-600 hover:border-[#F9A602] transition-all flex items-center gap-1.5">
              <span>🥤</span> General Question
            </button>
            <button type="button" onclick="selectTopic('daycare')" class="topic-btn text-xs font-semibold px-4 py-2 rounded-full border border-slate-200 text-slate-600 hover:border-[#F9A602] transition-all flex items-center gap-1.5">
              <span>🏫</span> Daycare / Bulk Samples
            </button>
            <button type="button" onclick="selectTopic('orders')" class="topic-btn text-xs font-semibold px-4 py-2 rounded-full border border-slate-200 text-slate-600 hover:border-[#F9A602] transition-all flex items-center gap-1.5">
              <span>📦</span> Order & Delivery
            </button>
            <button type="button" onclick="selectTopic('wholesale')" class="topic-btn text-xs font-semibold px-4 py-2 rounded-full border border-slate-200 text-slate-600 hover:border-[#F9A602] transition-all flex items-center gap-1.5">
              <span>🌱</span> Wholesale / B2B
            </button>
          </div>
          <input type="hidden" id="selectedTopic" value="general"/>
        </div>

        <form id="contactForm" onsubmit="handleContactSubmit(event)" class="space-y-5">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2" for="fullName">Your Name *</label>
              <div class="relative">
                <span class="material-symbols-outlined absolute left-4 top-3.5 text-slate-400 text-lg">person</span>
                <input required class="w-full bg-[#F8FAFC] border border-slate-200 rounded-2xl pl-11 pr-4 py-3.5 text-sm text-slate-800 placeholder-slate-400 focus:bg-white focus:border-[#F9A602] focus:ring-2 focus:ring-[#F9A602]/20 focus:outline-none transition-all" id="fullName" placeholder="e.g. Sarah Jenkins" type="text"/>
              </div>
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2" for="emailAddress">Email Address *</label>
              <div class="relative">
                <span class="material-symbols-outlined absolute left-4 top-3.5 text-slate-400 text-lg">mail</span>
                <input required class="w-full bg-[#F8FAFC] border border-slate-200 rounded-2xl pl-11 pr-4 py-3.5 text-sm text-slate-800 placeholder-slate-400 focus:bg-white focus:border-[#F9A602] focus:ring-2 focus:ring-[#F9A602]/20 focus:outline-none transition-all" id="emailAddress" placeholder="sarah@example.com" type="email"/>
              </div>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2" for="phoneNumber">Phone Number (Optional)</label>
              <div class="relative">
                <span class="material-symbols-outlined absolute left-4 top-3.5 text-slate-400 text-lg">call</span>
                <input class="w-full bg-[#F8FAFC] border border-slate-200 rounded-2xl pl-11 pr-4 py-3.5 text-sm text-slate-800 placeholder-slate-400 focus:bg-white focus:border-[#F9A602] focus:ring-2 focus:ring-[#F9A602]/20 focus:outline-none transition-all" id="phoneNumber" placeholder="(555) 000-0000" type="tel"/>
              </div>
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2" for="facilityType">Organization Type</label>
              <div class="relative">
                <span class="material-symbols-outlined absolute left-4 top-3.5 text-slate-400 text-lg">business</span>
                <select class="w-full bg-[#F8FAFC] border border-slate-200 rounded-2xl pl-11 pr-4 py-3.5 text-sm text-slate-800 focus:bg-white focus:border-[#F9A602] focus:ring-2 focus:ring-[#F9A602]/20 focus:outline-none transition-all appearance-none cursor-pointer" id="facilityType">
                  <option value="individual">Individual Customer / Home</option>
                  <option value="daycare">Childcare / Daycare Center</option>
                  <option value="preschool">Preschool / Kindergarten</option>
                  <option value="school">Elementary / High School</option>
                  <option value="gym">Gym / Wellness Studio</option>
                  <option value="distributor">Retailer / Wholesale Distributor</option>
                </select>
              </div>
            </div>
          </div>

          <div>
            <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2" for="messageText">How Can We Help You? *</label>
            <div class="relative">
              <textarea required rows="4" class="w-full bg-[#F8FAFC] border border-slate-200 rounded-2xl p-4 text-sm text-slate-800 placeholder-slate-400 focus:bg-white focus:border-[#F9A602] focus:ring-2 focus:ring-[#F9A602]/20 focus:outline-none transition-all resize-none" id="messageText" placeholder="Share your questions, requested flavors, center location, or any details..."></textarea>
            </div>
          </div>

          <div class="flex items-center gap-3 p-3 bg-amber-50/60 rounded-xl border border-amber-100">
            <input type="checkbox" id="sampleKitCheck" class="w-4 h-4 text-[#F9A602] rounded border-slate-300 focus:ring-[#F9A602]">
            <label for="sampleKitCheck" class="text-xs text-slate-700 select-none cursor-pointer font-medium">
              🎁 <strong>Yes, send me a free flavor sampler kit!</strong> (Available for childcare directors & facility managers)
            </label>
          </div>

          <button id="submitBtn" type="submit" class="w-full bg-gradient-to-r from-[#F9A602] via-[#F57C00] to-[#FF7043] text-white font-bold py-4 rounded-full shadow-[0_6px_20px_rgba(249,166,2,0.35)] hover:shadow-[0_8px_25px_rgba(249,166,2,0.45)] hover:scale-[1.01] active:scale-[0.99] transition-all duration-200 flex items-center justify-center gap-2 text-sm tracking-wide">
            <span class="material-symbols-outlined text-lg">send</span> Send Message Directly
          </button>

          <div class="flex items-center justify-between text-[11px] text-slate-400 pt-2 px-1">
            <span class="flex items-center gap-1"><span class="material-symbols-outlined text-xs text-emerald-600">verified_user</span> 256-Bit SSL Encrypted</span>
            <span class="flex items-center gap-1"><span class="material-symbols-outlined text-xs text-[#F9A602]">bolt</span> Zero Spam Policy</span>
          </div>
        </form>
      </div>

      <!-- Right Column: Flagship Juicery & Tasting Lounge (5 cols) -->
      <div class="lg:col-span-5 space-y-6">
        
        <!-- Flagship Store Showcase Card -->
        <div class="bg-white rounded-3xl overflow-hidden border border-slate-100 shadow-[0_8px_30px_rgba(26,26,46,0.06)] group">
          <div class="relative h-64 overflow-hidden">
            <img src="images/contact-flagship.jpg" alt="Penny Juice Flagship Juicery & Tasting Lounge" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
            <div class="absolute top-4 left-4">
              <span class="bg-[#F9A602] text-white text-[11px] font-extrabold uppercase px-3 py-1 rounded-full shadow-md flex items-center gap-1">
                <span class="material-symbols-outlined text-xs">local_cafe</span> Tasting Lounge Open
              </span>
            </div>
            <div class="absolute bottom-4 left-4 right-4 text-white">
              <span class="text-xs font-semibold text-amber-300 uppercase tracking-widest block mb-0.5">Flagship Location</span>
              <h3 class="text-xl font-black leading-tight">Las Vegas Juicery Lab & Bar</h3>
            </div>
          </div>

          <div class="p-6 sm:p-7 space-y-5">
            <div class="flex items-start gap-3.5">
              <span class="material-symbols-outlined text-[#7CB342] text-xl mt-0.5">location_on</span>
              <div>
                <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-0.5">Address & Neighborhood</h4>
                <p class="text-sm font-semibold text-[#1A1A2E]">123 Wellness Ave, Suite 100</p>
                <p class="text-xs text-slate-500">Downtown Arts District, Las Vegas, NV 89101</p>
              </div>
            </div>

            <div class="flex items-start gap-3.5">
              <span class="material-symbols-outlined text-[#F9A602] text-xl mt-0.5">schedule</span>
              <div class="w-full">
                <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Tasting Bar Hours</h4>
                <div class="space-y-1 text-xs">
                  <div class="flex justify-between text-slate-700">
                    <span>Monday – Friday</span>
                    <span class="font-bold text-[#1A1A2E]">8:00 AM – 7:00 PM</span>
                  </div>
                  <div class="flex justify-between text-slate-700">
                    <span>Saturday – Sunday</span>
                    <span class="font-bold text-[#1A1A2E]">9:00 AM – 5:00 PM</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Free Tasting Callout Box -->
            <div class="p-4 rounded-2xl bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-100 flex items-start gap-3">
              <span class="text-xl">🍹</span>
              <div>
                <h5 class="text-xs font-bold text-[#F9A602] uppercase tracking-wider mb-0.5">Daily Free Tasting Flights</h5>
                <p class="text-xs text-slate-600 leading-relaxed">Stop by between <strong>2:00 PM – 4:00 PM</strong> every day to sample all 8 of our signature cold-pressed organic juice concentrates on tap.</p>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-3 pt-2">
              <a href="https://maps.google.com" target="_blank" class="px-4 py-3 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold flex items-center justify-center gap-1.5 transition-colors">
                <span class="material-symbols-outlined text-base text-[#F9A602]">directions</span> Directions
              </a>
              <a href="tel:7025550123" class="px-4 py-3 rounded-xl bg-[#FFF7E6] hover:bg-[#FFECC7] text-[#F9A602] text-xs font-bold flex items-center justify-center gap-1.5 transition-colors">
                <span class="material-symbols-outlined text-base">call</span> Call Store
              </a>
            </div>
          </div>
        </div>

        <!-- Founder & Juicer Guarantee Card -->
        <div class="bg-gradient-to-br from-[#1A1A2E] to-[#2E2E50] rounded-3xl p-6 text-white shadow-xl relative overflow-hidden">
          <div class="absolute -right-8 -bottom-8 w-32 h-32 bg-[#F9A602]/10 rounded-full blur-2xl"></div>
          <div class="flex items-center gap-4 mb-3">
            <div class="w-12 h-12 rounded-full overflow-hidden border-2 border-[#F9A602]">
              <img src="images/learn-owner-hd.jpg" alt="Petunia - Founder" class="w-full h-full object-cover"/>
            </div>
            <div>
              <h4 class="text-sm font-bold text-white">Petunia & The Care Team</h4>
              <p class="text-xs text-amber-300">Co-Founder & Chief Juicer</p>
            </div>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed italic mb-3">
            "Every single email, call, and daycare question is treated like family. We started Penny Juice to bring wholesome sunshine into every child's day—and that begins with listening to you."
          </p>
          <div class="flex items-center gap-2 text-[11px] text-amber-400/90 font-medium">
            <span class="material-symbols-outlined text-sm">verified</span> Direct response commitment guaranteed
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- QUICK FAQ ACCORDION TEASER ON CONTACT PAGE -->
  <section class="mb-14">
    <div class="text-center max-w-2xl mx-auto mb-8">
      <span class="text-xs font-bold text-[#F9A602] uppercase tracking-wider">Fast Answers</span>
      <h2 class="text-2xl sm:text-3xl font-extrabold text-[#1A1A2E] mt-1">Common Questions Before Reaching Out</h2>
      <p class="text-xs sm:text-sm text-slate-500 mt-1">Save time with instant answers to our most popular questions.</p>
    </div>

    <div class="max-w-3xl mx-auto space-y-3">
      
      <details class="group bg-white rounded-2xl border border-slate-100 p-5 shadow-sm hover:shadow-md transition-all">
        <summary class="flex justify-between items-center font-bold text-sm text-[#1A1A2E] cursor-pointer list-none select-none">
          <span>🚚 How fast does shipping take, and do you deliver nationwide?</span>
          <span class="material-symbols-outlined text-[#F9A602] transition-transform duration-200 group-open:rotate-180">expand_more</span>
        </summary>
        <p class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
          Yes! We ship across all 50 US states using insulated cold-chain packaging. Most orders arrive within 2–3 business days. All bulk and daycare subscriptions enjoy 100% free expedited shipping.
        </p>
      </details>

      <details class="group bg-white rounded-2xl border border-slate-100 p-5 shadow-sm hover:shadow-md transition-all">
        <summary class="flex justify-between items-center font-bold text-sm text-[#1A1A2E] cursor-pointer list-none select-none">
          <span>👶 How do daycares and preschools order Penny Juice?</span>
          <span class="material-symbols-outlined text-[#F9A602] transition-transform duration-200 group-open:rotate-180">expand_more</span>
        </summary>
        <p class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
          Simply select "Daycare / Preschool" in our message form above or call 1-800-PENNY-JUICE. We provide customized recurring deliveries, free mixing dispensers, and CACFP compliant serving documentation.
        </p>
      </details>

      <details class="group bg-white rounded-2xl border border-slate-100 p-5 shadow-sm hover:shadow-md transition-all">
        <summary class="flex justify-between items-center font-bold text-sm text-[#1A1A2E] cursor-pointer list-none select-none">
          <span>❄️ How long do unopened concentrates last in the freezer?</span>
          <span class="material-symbols-outlined text-[#F9A602] transition-transform duration-200 group-open:rotate-180">expand_more</span>
        </summary>
        <p class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
          Our cold-pressed concentrates maintain peak flavor and nutrients for up to 12 months frozen. Once thawed in the refrigerator, unopened cartons stay fresh for 45 days.
        </p>
      </details>

    </div>

    <div class="text-center mt-6">
      <a href="faq.html" class="inline-flex items-center gap-2 text-xs font-bold text-[#F9A602] hover:text-[#e69902] transition-colors">
        Browse All 12 Frequently Asked Questions <span class="material-symbols-outlined text-sm">arrow_forward</span>
      </a>
    </div>
  </section>

</main>

<!-- TOAST CONFIRMATION -->
<div id="contactToast" class="bg-[#1A1A2E] text-white px-6 py-4 rounded-2xl shadow-2xl border border-white/20 flex items-center gap-3">
  <span class="w-8 h-8 rounded-full bg-emerald-500 text-white flex items-center justify-center font-bold text-sm">✓</span>
  <div>
    <h4 class="font-bold text-sm text-white" id="toastTitle">Message Sent!</h4>
    <p class="text-xs text-slate-300" id="toastDesc">Our care team will reach out to you within 2 hours.</p>
  </div>
</div>

<script>
function selectTopic(topic) {
  document.getElementById('selectedTopic').value = topic;
  const buttons = document.querySelectorAll('.topic-btn');
  buttons.forEach(btn => btn.classList.remove('active'));
  
  const targetMap = {
    'general': 0,
    'daycare': 1,
    'orders': 2,
    'wholesale': 3,
    'partnership': 3
  };
  const idx = targetMap[topic] !== undefined ? targetMap[topic] : 0;
  if(buttons[idx]) buttons[idx].classList.add('active');

  const facilitySelect = document.getElementById('facilityType');
  if(topic === 'daycare') {
    facilitySelect.value = 'daycare';
    document.getElementById('sampleKitCheck').checked = true;
  } else if(topic === 'wholesale') {
    facilitySelect.value = 'distributor';
  }
}

function handleContactSubmit(e) {
  e.preventDefault();
  const btn = document.getElementById('submitBtn');
  const originalHtml = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = '<span class="material-symbols-outlined text-lg animate-spin">refresh</span> Sending...';

  setTimeout(() => {
    btn.disabled = false;
    btn.innerHTML = originalHtml;
    
    // Show toast
    const toast = document.getElementById('contactToast');
    toast.classList.add('show');
    
    // Reset form
    document.getElementById('contactForm').reset();
    document.getElementById('selectedTopic').value = 'general';
    selectTopic('general');

    setTimeout(() => {
      toast.classList.remove('show');
    }, 4500);
  }, 1000);
}
</script>

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

# 2. GENERATE FAQ HTML
faq_html = """<!DOCTYPE html>
<html class="scroll-smooth" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Frequently Asked Questions & Help Center - Penny Juice</title>
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
.pj-hero-banner{position:relative;width:100%;min-height:360px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;overflow:hidden;padding:72px 24px 80px;box-sizing:border-box;margin:0;left:0;right:0;}
.pj-hero-banner .pj-hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;z-index:0;transform:scale(1.02);transition:transform 6s ease-out;}
.pj-hero-banner:hover .pj-hero-bg{transform:scale(1.0);}
.pj-hero-banner .pj-hero-overlay{position:absolute;inset:0;z-index:1;}
.pj-hero-banner .pj-hero-content{position:relative;z-index:2;max-width:840px;margin:0 auto;text-align:center;}
.pj-hero-banner .pj-hero-breadcrumb{font-size:12px;font-weight:700;letter-spacing:0.12em;color:#C8E6C9;margin:0 0 12px;text-transform:uppercase;display:inline-block;}
.pj-hero-banner h1{font-size:clamp(32px,5vw,52px);font-weight:800;color:#ffffff;line-height:1.15;margin:0 0 16px;text-shadow:0 3px 20px rgba(0,0,0,0.35);letter-spacing:-0.5px;}
.pj-hero-banner p{font-size:17px;color:rgba(255,255,255,0.95);max-width:640px;margin:0 auto 24px;line-height:1.65;text-shadow:0 2px 10px rgba(0,0,0,0.25);}

/* CATEGORY TAB ACTIVE STYLING */
.faq-tab.active {
  background: #7CB342 !important;
  color: #ffffff !important;
  box-shadow: 0 4px 14px rgba(124,179,66,0.35);
}

/* ACCORDION DETAILS TRANSITION */
details summary::-webkit-details-marker {
  display: none;
}
details[open] summary .faq-chevron {
  transform: rotate(180deg);
  background: #FFF7E6;
  color: #F9A602;
}

.faq-feedback-btn.active {
  background: #1A1A2E;
  color: #ffffff;
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

<!-- 100% FULL-WIDTH COVER BANNER WITH SEARCH -->
<div class="pj-hero-banner">
  <div class="pj-hero-bg" style="background-image:url('images/faq-fruits-splash.jpg');"></div>
  <div class="pj-hero-overlay" style="background:linear-gradient(135deg, rgba(26,26,46,0.85) 0%, rgba(124,179,66,0.8) 100%);"></div>
  <div class="pj-hero-content">
    <span class="pj-hero-breadcrumb">HOME › KNOWLEDGE BASE & FAQ</span>
    <h1>Got Questions? We've Got Fresh Answers.</h1>
    <p>Everything you need to know about our 100% real fruit juice concentrates, cold-pressing, daycare CACFP standards, shelf life, and nationwide insulated delivery.</p>
    
    <!-- LIVE INTERACTIVE SEARCH INPUT -->
    <div class="max-w-xl mx-auto relative mt-2">
      <div class="relative flex items-center bg-white rounded-full shadow-[0_8px_30px_rgba(0,0,0,0.25)] p-1.5 pl-5 border-2 border-white/60 focus-within:border-[#F9A602] transition-all">
        <span class="material-symbols-outlined text-[#7CB342] text-2xl mr-2">search</span>
        <input id="faqSearchInput" oninput="filterFaqs()" type="text" placeholder="Search questions (e.g., organic, shelf life, daycare, allergies)..." class="w-full bg-transparent text-slate-800 placeholder-slate-400 text-sm font-medium focus:outline-none pr-4"/>
        <button onclick="clearSearch()" id="clearSearchBtn" class="hidden mr-2 w-6 h-6 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500 flex items-center justify-center text-xs font-bold">✕</button>
      </div>
      <div id="searchCounter" class="mt-2.5 text-xs text-white/90 font-medium">
        Showing all <span class="font-bold text-amber-300">12</span> verified answers
      </div>
    </div>
  </div>
</div>

<main class="flex-grow max-w-[1080px] mx-auto w-full px-4 sm:px-6 lg:px-8 py-12">

  <!-- CATEGORY PILLS & EXPAND ALL CONTROLS -->
  <div class="flex flex-col sm:flex-row items-center justify-between gap-4 mb-10 pb-6 border-b border-slate-200">
    <div class="flex flex-wrap items-center gap-2" id="categoryTabs">
      <button onclick="filterCategory('all', this)" class="faq-tab active px-5 py-2 rounded-full text-xs font-bold bg-white text-slate-700 border border-slate-200 hover:border-[#7CB342] transition-all shadow-sm flex items-center gap-1.5">
        <span>✨</span> All Questions (12)
      </button>
      <button onclick="filterCategory('ingredients', this)" class="faq-tab px-5 py-2 rounded-full text-xs font-bold bg-white text-slate-700 border border-slate-200 hover:border-[#7CB342] transition-all shadow-sm flex items-center gap-1.5">
        <span>🍎</span> Juices & Nutrition (4)
      </button>
      <button onclick="filterCategory('storage', this)" class="faq-tab px-5 py-2 rounded-full text-xs font-bold bg-white text-slate-700 border border-slate-200 hover:border-[#7CB342] transition-all shadow-sm flex items-center gap-1.5">
        <span>❄️</span> Freshness & Storage (3)
      </button>
      <button onclick="filterCategory('shipping', this)" class="faq-tab px-5 py-2 rounded-full text-xs font-bold bg-white text-slate-700 border border-slate-200 hover:border-[#7CB342] transition-all shadow-sm flex items-center gap-1.5">
        <span>🚚</span> Shipping & Delivery (3)
      </button>
      <button onclick="filterCategory('daycare', this)" class="faq-tab px-5 py-2 rounded-full text-xs font-bold bg-white text-slate-700 border border-slate-200 hover:border-[#7CB342] transition-all shadow-sm flex items-center gap-1.5">
        <span>🏫</span> Daycare & CACFP (2)
      </button>
    </div>

    <!-- Toggle Expand / Collapse All -->
    <button onclick="toggleAllAccordions()" id="toggleAllBtn" class="text-xs font-bold text-[#F9A602] hover:text-[#e69902] flex items-center gap-1.5 px-3 py-1.5 rounded-lg hover:bg-amber-50 transition-colors whitespace-nowrap">
      <span class="material-symbols-outlined text-sm">unfold_more</span> Expand All
    </button>
  </div>

  <!-- FAQ LIST -->
  <div class="space-y-4" id="faqListContainer">

    <!-- QUESTION 1: Real Fruit & No Sugar -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="ingredients" data-keywords="100% real fruit juice no added sugar sweeteners high fructose corn syrup preservatives organic pure ingredients">
      <details class="group p-6 sm:p-7" open>
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-[#7CB342] bg-emerald-50 px-2.5 py-0.5 rounded-full">🍎 Juices & Nutrition</span>
              <span class="text-[11px] font-semibold text-slate-400">100% Fruit Concentrates</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              Are Penny Juice products 100% real fruit juice with no added sugar or high-fructose corn syrup?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>
            <strong>Yes, absolutely 100%!</strong> Every bottle and carton of Penny Juice is crafted entirely from premium fruit juice concentrates and luscious purees. We never add granulated cane sugar, high-fructose corn syrup, artificial sweeteners (like sucralose or aspartame), or chemical coloring agents.
          </p>
          <p>
            All natural sweetness and vibrant colors come directly from sun-ripened organic fruits—apples, kiwis, pineapples, lemons, mangoes, and pears.
          </p>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

    <!-- QUESTION 2: Allergens & Child Safety -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="ingredients" data-keywords="allergy allergen peanut tree nut gluten free dairy egg school lunch safety dietary">
      <details class="group p-6 sm:p-7">
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-[#7CB342] bg-emerald-50 px-2.5 py-0.5 rounded-full">🍎 Juices & Nutrition</span>
              <span class="text-[11px] font-semibold text-emerald-600">Top-8 Allergen Free</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              Are your juices allergen-free and safe for children with severe food allergies?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>
            Yes! Penny Juice is formulated specifically with childcare safety in mind. Our juices are <strong>100% peanut-free, tree nut-free, gluten-free, dairy-free, egg-free, fish-free, shellfish-free, and soy-free</strong>.
          </p>
          <p>
            They are processed in certified dedicated lines under strict sanitation protocols, preventing cross-contamination and providing teachers and parents complete peace of mind.
          </p>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

    <!-- QUESTION 3: Cold Pressed vs Thermal Heat -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="ingredients" data-keywords="cold pressed hydraulic extraction vitamins enzymes nutrient preservation heat pasteurization">
      <details class="group p-6 sm:p-7">
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-[#7CB342] bg-emerald-50 px-2.5 py-0.5 rounded-full">🍎 Juices & Nutrition</span>
              <span class="text-[11px] font-semibold text-[#F9A602]">Cold-Pressed Science</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              What is cold-pressed extraction and why does it preserve more vitamins than grocery store juice?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>
            Standard mass-market juices utilize high-speed centrifugal metal blades and harsh heat pasteurization that literally boils the juice. This thermal exposure destroys fragile Vitamin C, breaks down bromelain enzymes, and degrades crisp fruit aromas.
          </p>
          <p>
            <strong>Our cold-press method:</strong> We use gentle hydraulic pressure without friction or heat. This squeezes out every drop of pure fruit nectar, keeping raw cellular enzymes alive and preserving up to 5x more micronutrients.
          </p>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

    <!-- QUESTION 4: Pasteurization & FDA Safety -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="ingredients" data-keywords="pasteurized fda safe safety bacteria flash pasteurization uv cold purification">
      <details class="group p-6 sm:p-7">
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-[#7CB342] bg-emerald-50 px-2.5 py-0.5 rounded-full">🍎 Juices & Nutrition</span>
              <span class="text-[11px] font-semibold text-slate-400">Child Safety Standards</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              Are Penny Juice concentrates pasteurized for food safety?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>
            Yes. To guarantee 100% microbiological safety for toddlers, preschoolers, and nursing mothers, our concentrates undergo a rapid <strong>flash-pasteurization process</strong> that eliminates any potential harmful pathogens while safeguarding live flavors and nutrients.
          </p>
          <p>
            Our facility meets and exceeds all FDA Juice HACCP regulations and state health department sanitation codes.
          </p>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

    <!-- QUESTION 5: Shelf Life & Storage -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="storage" data-keywords="shelf life expire expiration date freezer frozen refrigerator fridge thaw days months">
      <details class="group p-6 sm:p-7">
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-[#F9A602] bg-amber-50 px-2.5 py-0.5 rounded-full">❄️ Freshness & Storage</span>
              <span class="text-[11px] font-semibold text-slate-400">Freezer & Fridge Guidelines</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              How long do the concentrates last in the freezer, and how long once mixed with water?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>Here is our recommended storage timeline:</p>
          <ul class="list-disc list-inside space-y-1 pl-1">
            <li><strong>Frozen in the Freezer:</strong> Unopened cartons remain fresh for up to <strong>12 full months</strong> without any loss of vitamin potency.</li>
            <li><strong>Thawed in the Refrigerator (Unopened):</strong> Keep refrigerated for up to <strong>45 days</strong>.</li>
            <li><strong>Mixed with Water in Pitcher / Dispenser:</strong> Best enjoyed within <strong>5 to 7 days</strong> when refrigerated below 40°F.</li>
          </ul>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

    <!-- QUESTION 6: Thawing and Mixing Ratios -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="storage" data-keywords="how to mix thaw dilution ratio parts water dispenser pitcher prep directions instructions">
      <details class="group p-6 sm:p-7">
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-[#F9A602] bg-amber-50 px-2.5 py-0.5 rounded-full">❄️ Freshness & Storage</span>
              <span class="text-[11px] font-semibold text-slate-400">7:1 Dilution Ratio</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              How do I properly thaw and blend Penny Juice concentrates with water?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>
            Preparation takes under 60 seconds! Transfer the concentrate carton from the freezer into your refrigerator 24 hours prior to blending.
          </p>
          <ol class="list-decimal list-inside space-y-1 pl-1">
            <li>Pour 1 carton of thawed concentrate into your mixing pitcher or 3-gallon Penny Juice beverage dispenser.</li>
            <li>Add 7 equal parts cold filtered water (exact fill lines are printed directly on our complementary pitchers).</li>
            <li>Stir with a beverage paddle or shake well. Serve chilled over ice!</li>
          </ol>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

    <!-- QUESTION 7: Fruit Popsicles Recipe -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="storage" data-keywords="popsicle ice pop freeze mold kids snack summer treat recipe">
      <details class="group p-6 sm:p-7">
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-[#F9A602] bg-amber-50 px-2.5 py-0.5 rounded-full">❄️ Freshness & Storage</span>
              <span class="text-[11px] font-semibold text-amber-600">Kid-Friendly Ideas</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              Can we freeze mixed Penny Juice into homemade frozen fruit popsicles?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>
            Yes! In fact, it is one of our childcare centers' favorite summertime activities. Because Penny Juice is 100% natural fruit juice without corn syrup or gelatin fillers, it freezes with a soft, sorbet-like consistency that is easy for young teeth to bite.
          </p>
          <p>
            <strong>Pro-tip:</strong> Try blending Kiwi Vitality with sliced strawberries or freezing Pineapple Pulse with fresh blueberries for colorful, antioxidant-rich smoothie pops!
          </p>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

    <!-- QUESTION 8: Shipping Nationwide -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="shipping" data-keywords="shipping delivery states 50 states nationwide insulated dry ice gel packs tracking transit">
      <details class="group p-6 sm:p-7">
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-[#FF7043] bg-orange-50 px-2.5 py-0.5 rounded-full">🚚 Shipping & Delivery</span>
              <span class="text-[11px] font-semibold text-slate-400">All 50 US States</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              Do you ship nationwide across all 50 US states, and how do juices stay cold?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>
            Yes, we proudly ship to all 50 states! To ensure your cartons arrive in pristine frozen or refrigerator-cold condition, all shipments are packed in custom curbside-recyclable thermal insulated boxes equipped with sub-zero non-toxic gel packs.
          </p>
          <p>
            Our intelligent climate packaging maintains sub-40°F internal temperatures for up to 72 hours in transit, even during summer heatwaves.
          </p>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

    <!-- QUESTION 9: Shipping Cost & Speed -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="shipping" data-keywords="shipping cost fee free shipping delivery days business tracking arrival">
      <details class="group p-6 sm:p-7">
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-[#FF7043] bg-orange-50 px-2.5 py-0.5 rounded-full">🚚 Shipping & Delivery</span>
              <span class="text-[11px] font-semibold text-emerald-600">Free Shipping Available</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              How much is shipping, and how many days will delivery take?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>
            <strong>All childcare subscriptions and bulk orders of 2 or more cases qualify for 100% FREE nationwide shipping!</strong> For individual retail orders under $49, standard flat-rate cold shipping is just $7.99.
          </p>
          <p>
            Orders are dispatched within 24 hours on Monday through Wednesday to avoid weekend layovers. Delivery takes <strong>2 to 3 business days</strong> with live tracking alerts sent directly to your phone and email.
          </p>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

    <!-- QUESTION 10: Fresh Arrival Guarantee -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="shipping" data-keywords="damage broken thawed warm refund replacement guarantee warranty policy return">
      <details class="group p-6 sm:p-7">
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-[#FF7043] bg-orange-50 px-2.5 py-0.5 rounded-full">🚚 Shipping & Delivery</span>
              <span class="text-[11px] font-semibold text-[#F9A602]">100% Freshness Guarantee</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              What happens if my delivery arrives delayed, warm, or damaged?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>
            We stand behind every carton with our <strong>No-Hassle Fresh-Arrival Guarantee</strong>. If your shipment is mishandled by the courier, arrives defrosted beyond safe temperatures, or suffers packaging damage:
          </p>
          <p>
            Just take a quick photo and email <em>care@pennyjuice.com</em> or call (702) 555-0123 within 48 hours. We will immediately expedite a replacement order at zero charge or issue a 100% refund. No return shipping required!
          </p>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

    <!-- QUESTION 11: Daycare Bulk Program & Savings -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="daycare" data-keywords="daycare preschool bulk childcare concentrate case pricing savings cups pitchers dispensers free">
      <details class="group p-6 sm:p-7">
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-indigo-600 bg-indigo-50 px-2.5 py-0.5 rounded-full">🏫 Daycare & CACFP</span>
              <span class="text-[11px] font-semibold text-slate-400">Preschool Bulk Concentrates</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              How does the Daycare & Preschool bulk concentrate program work?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>
            Penny Juice was originally created to solve a massive problem for childcare directors: heavy, expensive plastic jugs of juice that clutter storage space and spoil quickly.
          </p>
          <p>
            With our high-yield concentrate system:
          </p>
          <ul class="list-disc list-inside space-y-1 pl-1">
            <li><strong>Saves 85% Storage Space:</strong> A single case of 6 compact cartons yields <strong>over 15 gallons</strong> of delicious, ready-to-serve 100% fruit juice.</li>
            <li><strong>Free Dispensing Equipment:</strong> Every participating center receives free calibrated mixing pitchers, spigots, and portion measurement cups.</li>
            <li><strong>Flexible Recurring Deliveries:</strong> Set your schedule (weekly, bi-weekly, monthly) with zero long-term contracts. Pause or change flavors whenever you like.</li>
          </ul>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

    <!-- QUESTION 12: USDA CACFP Reimbursement Standards -->
    <div class="faq-item bg-white rounded-3xl border border-slate-100 shadow-[0_4px_20px_rgba(26,26,46,0.04)] hover:shadow-[0_8px_30px_rgba(26,26,46,0.08)] transition-all overflow-hidden" data-category="daycare" data-keywords="usda cacfp compliance meal pattern guidelines reimbursement child adult food care nutrition fruit serving">
      <details class="group p-6 sm:p-7">
        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none select-none">
          <div class="space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-indigo-600 bg-indigo-50 px-2.5 py-0.5 rounded-full">🏫 Daycare & CACFP</span>
              <span class="text-[11px] font-semibold text-emerald-600">100% CACFP Compliant</span>
            </div>
            <h3 class="text-base sm:text-lg font-bold text-[#1A1A2E] leading-snug group-hover:text-[#F9A602] transition-colors">
              Does Penny Juice fulfill all USDA CACFP meal reimbursement guidelines for childcare centers?
            </h3>
          </div>
          <div class="faq-chevron w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center flex-shrink-0 transition-all duration-300">
            <span class="material-symbols-outlined text-xl">expand_more</span>
          </div>
        </summary>
        <div class="mt-4 pt-4 border-t border-slate-100 text-slate-600 text-xs sm:text-sm leading-relaxed space-y-3">
          <p>
            <strong>Yes, 100%!</strong> Penny Juice strictly complies with all guidelines established by the <strong>USDA Child and Adult Care Food Program (CACFP)</strong>.
          </p>
          <p>
            Because our juices are certified 100% full-strength fruit juice with zero added sweeteners, a standard 4 oz or 6 oz serving satisfies the complete fruit meal component requirement for federal and state food reimbursement audits. We provide official Child Nutrition (CN) documentation with every bulk invoice.
          </p>
          <div class="pt-2 flex items-center justify-between text-xs border-t border-slate-50">
            <span class="text-slate-400">Was this answer helpful?</span>
            <div class="flex items-center gap-2">
              <button onclick="handleFeedback(this, 'helpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👍 Yes</button>
              <button onclick="handleFeedback(this, 'unhelpful')" class="faq-feedback-btn px-3 py-1 rounded-full border border-slate-200 text-slate-600 hover:border-slate-400 transition-all flex items-center gap-1 text-xs">👎 No</button>
            </div>
          </div>
        </div>
      </details>
    </div>

  </div>

  <!-- NO RESULTS STATE (Hidden by default) -->
  <div id="noResultsBox" class="hidden text-center py-16 px-6 bg-white rounded-3xl border border-slate-200 mt-6">
    <div class="w-16 h-16 rounded-full bg-amber-50 text-[#F9A602] flex items-center justify-center mx-auto mb-4 text-3xl">
      🔍
    </div>
    <h3 class="text-xl font-bold text-[#1A1A2E] mb-2">No matching questions found</h3>
    <p class="text-sm text-slate-500 max-w-md mx-auto mb-6">We couldn't find an answer matching your query. Our juice specialists are standing by to help answer anything!</p>
    <button onclick="clearSearch()" class="px-6 py-2.5 rounded-full bg-[#F9A602] text-white text-xs font-bold shadow-md hover:bg-[#e69902] transition-colors">
      Clear Search Filter
    </button>
  </div>

  <!-- CONCIERGE SUPPORT CALLOUT BANNER -->
  <section class="mt-20">
    <div class="bg-gradient-to-br from-[#1A1A2E] via-[#242442] to-[#1A1A2E] rounded-3xl p-8 sm:p-12 text-white shadow-2xl relative overflow-hidden border border-slate-800">
      <div class="absolute -right-16 -top-16 w-64 h-64 bg-[#7CB342]/15 rounded-full blur-3xl"></div>
      <div class="absolute -left-16 -bottom-16 w-64 h-64 bg-[#F9A602]/15 rounded-full blur-3xl"></div>
      
      <div class="relative z-10 text-center max-w-2xl mx-auto mb-10">
        <span class="text-xs font-extrabold uppercase tracking-widest text-[#FFE082] bg-white/10 px-3.5 py-1.5 rounded-full inline-block mb-3 border border-white/15">Need More Help?</span>
        <h2 class="text-2xl sm:text-4xl font-black mb-3">Still Looking for Answers?</h2>
        <p class="text-sm text-slate-300 leading-relaxed">Our friendly juicing specialists and childcare nutritionists are just a phone call or click away.</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-5 max-w-3xl mx-auto relative z-10 mb-8">
        
        <!-- Support Card 1: Phone -->
        <a href="tel:7025550123" class="bg-white/5 hover:bg-white/10 border border-white/10 rounded-2xl p-5 text-center transition-all hover:scale-[1.02] block">
          <div class="w-11 h-11 rounded-xl bg-[#F9A602] text-white flex items-center justify-center mx-auto mb-3">
            <span class="material-symbols-outlined text-xl">call</span>
          </div>
          <h4 class="font-bold text-sm text-white mb-0.5">Call Our Juicers</h4>
          <p class="text-xs text-amber-300 font-medium mb-1">(702) 555-0123</p>
          <span class="text-[11px] text-slate-400">Mon–Fri 8AM–6PM PST</span>
        </a>

        <!-- Support Card 2: Live Chat / Message -->
        <a href="contact.html" class="bg-white/5 hover:bg-white/10 border border-white/10 rounded-2xl p-5 text-center transition-all hover:scale-[1.02] block">
          <div class="w-11 h-11 rounded-xl bg-[#7CB342] text-white flex items-center justify-center mx-auto mb-3">
            <span class="material-symbols-outlined text-xl">chat</span>
          </div>
          <h4 class="font-bold text-sm text-white mb-0.5">Direct Message Studio</h4>
          <p class="text-xs text-emerald-300 font-medium mb-1">Fast Response</p>
          <span class="text-[11px] text-slate-400">Replies within 2 hours</span>
        </a>

        <!-- Support Card 3: Free Samples -->
        <a href="contact.html" onclick="localStorage.setItem('requestSample', 'true')" class="bg-white/5 hover:bg-white/10 border border-white/10 rounded-2xl p-5 text-center transition-all hover:scale-[1.02] block">
          <div class="w-11 h-11 rounded-xl bg-[#FF7043] text-white flex items-center justify-center mx-auto mb-3">
            <span class="material-symbols-outlined text-xl">redeem</span>
          </div>
          <h4 class="font-bold text-sm text-white mb-0.5">Free Daycare Sampler</h4>
          <p class="text-xs text-orange-300 font-medium mb-1">4 Free Flavors</p>
          <span class="text-[11px] text-slate-400">For verified preschools</span>
        </a>

      </div>

      <div class="text-center relative z-10">
        <a href="contact.html" class="inline-flex items-center gap-2 bg-gradient-to-r from-[#7CB342] to-[#689F38] text-white text-xs font-extrabold uppercase tracking-wider px-8 py-4 rounded-full shadow-lg hover:shadow-xl hover:scale-105 transition-all">
          Open Contact Lounge <span class="material-symbols-outlined text-sm">arrow_forward</span>
        </a>
      </div>

    </div>
  </section>

</main>

<script>
let currentCategory = 'all';

function filterCategory(category, buttonEl) {
  currentCategory = category;
  
  // Update buttons
  const tabs = document.querySelectorAll('.faq-tab');
  tabs.forEach(tab => tab.classList.remove('active'));
  buttonEl.classList.add('active');

  filterFaqs();
}

function filterFaqs() {
  const query = document.getElementById('faqSearchInput').value.toLowerCase().trim();
  const clearBtn = document.getElementById('clearSearchBtn');
  if(query.length > 0) {
    clearBtn.classList.remove('hidden');
  } else {
    clearBtn.classList.add('hidden');
  }

  const items = document.querySelectorAll('.faq-item');
  let visibleCount = 0;

  items.forEach(item => {
    const itemCat = item.getAttribute('data-category');
    const itemKeywords = (item.getAttribute('data-keywords') || '').toLowerCase();
    const itemText = item.innerText.toLowerCase();

    const matchesCat = (currentCategory === 'all' || itemCat === currentCategory);
    const matchesQuery = (query === '' || itemKeywords.includes(query) || itemText.includes(query));

    if(matchesCat && matchesQuery) {
      item.style.display = 'block';
      visibleCount++;
    } else {
      item.style.display = 'none';
    }
  });

  const counter = document.getElementById('searchCounter');
  const noResults = document.getElementById('noResultsBox');

  if(visibleCount === 0) {
    noResults.classList.remove('hidden');
    counter.innerHTML = 'Showing <span class="font-bold text-amber-300">0</span> results';
  } else {
    noResults.classList.add('hidden');
    counter.innerHTML = `Showing <span class="font-bold text-amber-300">${visibleCount}</span> of 12 verified answers`;
  }
}

function clearSearch() {
  document.getElementById('faqSearchInput').value = '';
  filterFaqs();
}

let allExpanded = false;
function toggleAllAccordions() {
  const allDetails = document.querySelectorAll('#faqListContainer details');
  const toggleBtn = document.getElementById('toggleAllBtn');
  allExpanded = !allExpanded;

  allDetails.forEach(detail => {
    detail.open = allExpanded;
  });

  if(allExpanded) {
    toggleBtn.innerHTML = '<span class="material-symbols-outlined text-sm">unfold_less</span> Collapse All';
  } else {
    toggleBtn.innerHTML = '<span class="material-symbols-outlined text-sm">unfold_more</span> Expand All';
  }
}

function handleFeedback(button, type) {
  const parent = button.parentElement;
  const buttons = parent.querySelectorAll('button');
  buttons.forEach(b => b.classList.remove('active'));
  button.classList.add('active');
  
  parent.innerHTML = '<span class="text-xs font-semibold text-emerald-600">✓ Thank you for your feedback!</span>';
}
</script>

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

# WRITE FILES
with open(contact_site, 'w', encoding='utf-8') as f:
    f.write(contact_html)
with open(contact_stitch, 'w', encoding='utf-8') as f:
    f.write(contact_html)

with open(faq_site, 'w', encoding='utf-8') as f:
    f.write(faq_html)
with open(faq_stitch, 'w', encoding='utf-8') as f:
    f.write(faq_html)

print("Contact files equal:", filecmp.cmp(contact_site, contact_stitch))
print("FAQ files equal:", filecmp.cmp(faq_site, faq_stitch))
print("Successfully wrote and synced contact.html and faq.html!")
