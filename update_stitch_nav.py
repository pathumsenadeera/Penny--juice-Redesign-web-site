import os
import glob
import re

files = glob.glob('d:/ICT/UX/Penny-Juice/.stitch/designs/*.html')

style_block = """<style id="pj-master-style">
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
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
.pj-hero-banner{position:relative;width:100%;min-height:240px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;overflow:hidden;padding:64px 24px;box-sizing:border-box;margin:0;left:0;right:0;}
.pj-hero-banner .pj-hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;z-index:0;}
.pj-hero-banner .pj-hero-overlay{position:absolute;inset:0;z-index:1;}
.pj-hero-banner .pj-hero-content{position:relative;z-index:2;max-width:780px;margin:0 auto;text-align:center;}
.pj-hero-banner .pj-hero-breadcrumb{font-size:12px;font-weight:600;letter-spacing:0.08em;color:rgba(255,255,255,0.85);margin:0 0 10px;text-transform:uppercase;display:inline-block;}
.pj-hero-banner h1{font-size:clamp(30px,4.5vw,50px);font-weight:800;color:#ffffff;line-height:1.15;margin:0 0 12px;text-shadow:0 2px 16px rgba(0,0,0,0.25);}
.pj-hero-banner p{font-size:16px;color:rgba(255,255,255,0.92);max-width:560px;margin:0 auto;line-height:1.6;}
</style>
"""

nav_block = """<nav class="pj-nav" id="pj-main-nav">
  <div class="pj-inner">
    <a href="index.html" class="pj-logo">🍊 Penny<span>Juice</span></a>
    <ul class="pj-links">
      <li><a href="shop.html">Shop</a></li>
      <li><a href="learn.html">Learn</a></li>
      <li><a href="ingredients.html">Ingredients</a></li>
      <li><a href="blog.html">Blog</a></li>
      <li><a href="contact.html">Contact</a></li>
      <li><a href="faq.html">FAQ</a></li>
    </ul>
    <div class="pj-icons">
      <a href="search.html" title="Search"><span class="material-symbols-outlined">search</span></a>
      <a href="login.html" title="Login"><span class="material-symbols-outlined">person</span></a>
      <a href="cart.html" class="pj-cart" title="Cart"><span class="material-symbols-outlined">shopping_cart</span> (3)</a>
    </div>
  </div>
</nav>"""

for f in files:
    # Skip index.html as we already copied it directly
    if f.endswith('index.html'):
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Inject style if not present
    if 'id="pj-master-style"' not in content:
        # inject after <body ...>
        body_match = re.search(r'<body[^>]*>', content)
        if body_match:
            content = content[:body_match.end()] + '\n\n' + style_block + content[body_match.end():]
    
    # 2. Replace the old nav block with new nav block.
    # The old nav blocks look like <nav ...> ... </nav>
    # We want to replace the FIRST <nav> ... </nav> ONLY if it's not our 'pj-nav'
    
    nav_match = re.search(r'<nav[^>]*>.*?</nav>', content, flags=re.DOTALL)
    if nav_match:
        if 'id="pj-main-nav"' not in nav_match.group(0):
            print(f'Replacing nav in {f}')
            content = content[:nav_match.start()] + nav_block + content[nav_match.end():]
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
        else:
            print(f'Nav already updated in {f}')
