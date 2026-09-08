import glob

old_html = '''    <div class="pj-icons">
      <a href="search.html">🔍 Search</a>
      <a href="login.html">👤 Login</a>
      <a href="cart.html" class="pj-cart">🛒 Cart (3)</a>
    </div>'''

new_html = '''    <div class="pj-icons">
      <a href="search.html" title="Search"><span class="material-symbols-outlined">search</span></a>
      <a href="login.html" title="Login"><span class="material-symbols-outlined">person</span></a>
      <a href="cart.html" class="pj-cart" title="Cart"><span class="material-symbols-outlined">shopping_cart</span> (3)</a>
    </div>'''

old_css = '''.pj-icons a{font-size:13px;font-weight:500;color:#64748B;text-decoration:none;padding:8px 16px;border-radius:50px;transition:all 0.2s;display:flex;align-items:center;gap:6px;}'''
new_css = '''.pj-icons a{font-size:13px;font-weight:500;color:#64748B;text-decoration:none;padding:8px;width:36px;height:36px;justify-content:center;border-radius:50px;transition:all 0.2s;display:flex;align-items:center;gap:6px;}
.pj-icons a.pj-cart{width:auto;padding:8px 16px;}'''

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_html in content or old_css in content:
        content = content.replace(old_html, new_html)
        content = content.replace(old_css, new_css)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {file}')
