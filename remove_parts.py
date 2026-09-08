import glob
import re

files = sorted(glob.glob('site/public/*.html') + glob.glob('.stitch/designs/*.html'))

# 1. Image 1: Bottom Footer Legal / Copyright Bar
footer_pattern = re.compile(
    r'[ \t]*<div class="max-w-\[1280px\] mx-auto px-6 mt-16 pt-8 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-4">\s*'
    r'<p class="text-gray-500 text-sm">© 2026 Penny Juice\. All rights reserved\.</p>\s*'
    r'<div class="flex gap-6">\s*'
    r'<a class="text-gray-500 hover:text-white transition-colors text-sm" href="#">Privacy Policy</a>\s*'
    r'<a class="text-gray-500 hover:text-white transition-colors text-sm" href="#">Terms of Service</a>\s*'
    r'<a class="text-gray-500 hover:text-white transition-colors text-sm" href="#">Shipping Info</a>\s*'
    r'</div>\s*'
    r'</div>\n?',
    re.DOTALL
)

# 2. Image 2: Filter & Sort Bar in shop.html
shop_filter_pattern = re.compile(
    r'[ \t]*<!-- Filter & Sort Bar \(Sticky\) -->\s*'
    r'<div class="sticky top-20 z-40 bg-surface shadow-soft rounded-xl p-4 flex flex-col md:flex-row justify-between items-center gap-4 border border-outline-variant/30">.*?'
    r'<!-- Products Grid -->',
    re.DOTALL
)

# Shop script for filtering
shop_script_pattern = re.compile(
    r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s*const filterBtns = document\.querySelectorAll\(\'\.filter-btn\'\);.*?</script>\s*',
    re.DOTALL
)

# 3. Image 3: Category Filter Pills in blog.html
blog_pills_pattern = re.compile(
    r'[ \t]*<!-- CATEGORY FILTER PILLS -->\s*'
    r'<div class="flex items-center gap-3 overflow-x-auto no-scrollbar pb-6 mb-8 border-b border-slate-200/60">.*?'
    r'</div>\s*',
    re.DOTALL
)

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    orig_c = c
    
    # Remove footer bar
    c = footer_pattern.sub('', c)
    
    # If shop.html, remove filter & sort bar and its JS
    if 'shop.html' in f:
        c = shop_filter_pattern.sub('<!-- Products Grid -->', c)
        c = shop_script_pattern.sub('', c)
    
    # If blog.html, remove category pills
    if 'blog.html' in f:
        c = blog_pills_pattern.sub('', c)
    
    if c != orig_c:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print(f"Updated {f}")

# Also update update_blog.py so it remains in sync
with open('update_blog.py', 'r', encoding='utf-8') as fp:
    b = fp.read()
b = blog_pills_pattern.sub('', b)
with open('update_blog.py', 'w', encoding='utf-8') as fp:
    fp.write(b)
print("Updated update_blog.py")
