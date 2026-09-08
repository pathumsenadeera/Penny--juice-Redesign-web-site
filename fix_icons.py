import os
import glob

files = glob.glob('d:/ICT/UX/Penny-Juice/.stitch/designs/*.html')

new_icons = """    <div class="pj-icons">
      <a href="search.html" title="Search"><span class="material-symbols-outlined">search</span></a>
      <a href="login.html" title="Login"><span class="material-symbols-outlined">person</span></a>
      <a href="cart.html" class="pj-cart" title="Cart"><span class="material-symbols-outlined">shopping_cart</span> (3)</a>
    </div>"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '<a href="search.html" class="active">🔍 Search</a>' in content or '<a href="login.html" class="active">👤 Login</a>' in content or '<a href="cart.html" class="active">🛒 Cart' in content or '<a href="search.html">🔍 Search</a>' in content:
        print('Fixing active text icons in', f)
        start = content.find('<div class="pj-icons">')
        if start != -1:
            end = content.find('</div>', start) + 6
            content = content[:start] + new_icons + content[end:]
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
