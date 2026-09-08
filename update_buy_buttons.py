import re

slug_map = {
    'Kiwi Vitality': 'kiwi-vitality',
    'Pineapple Pulse': 'pineapple-pulse',
    'Green Glow': 'green-glow',
    'Zen Pear': 'zen-pear',
    'Golden Aura': 'golden-aura',
    'Lemon Lift': 'lemon-lift',
    'Tropical Harmony': 'tropical-harmony',
    'Emerald Energy': 'emerald-energy'
}

files_to_update = [
    'd:/ICT/UX/Penny-Juice/site/public/index.html',
    'd:/ICT/UX/Penny-Juice/site/public/shop.html',
    'd:/ICT/UX/Penny-Juice/site/public/search.html',
    'd:/ICT/UX/Penny-Juice/.stitch/designs/index.html',
    'd:/ICT/UX/Penny-Juice/.stitch/designs/shop.html',
    'd:/ICT/UX/Penny-Juice/.stitch/designs/search.html'
]

for fpath in files_to_update:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # First restore card body links to product-detail.html
        content = re.sub(
            r'<a\s+href="checkout\.html\?buy=[^"]*"\s+class="block focus:outline-none flex-grow">',
            '<a href="product-detail.html" class="block focus:outline-none flex-grow">',
            content
        )

        # Now accurately replace each Buy button within its product card
        # We find each product card by data-title and replace only its Buy button
        for name, slug in slug_map.items():
            card_start = f'data-title="{name}"'
            idx = content.find(card_start)
            while idx != -1:
                # Find the next product card or end of section
                next_card = content.find('product-card group relative', idx + len(card_start))
                if next_card == -1:
                    card_chunk = content[idx:idx+4000]
                    end_pos = idx + 4000
                else:
                    card_chunk = content[idx:next_card]
                    end_pos = next_card

                # In this chunk, replace <a href="product-detail.html"...<span>Buy</span>
                new_chunk = re.sub(
                    r'(<a\s+href=")product-detail\.html(" class="[^"]*">\s*<span>Buy</span>)',
                    r'\g<1>checkout.html?buy=' + slug + r'\g<2>',
                    card_chunk,
                    count=1
                )
                content = content[:idx] + new_chunk + content[end_pos:]
                # search for next card with same name if any
                idx = content.find(card_start, idx + len(new_chunk))

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fpath}")
    except Exception as e:
        print(f"Error {fpath}: {e}")
