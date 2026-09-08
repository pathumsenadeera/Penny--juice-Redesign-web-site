for path in ['site/public/shop.html', '.stitch/designs/shop.html']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Add filter-btn class to filter buttons
    c = c.replace(
        '<button class="font-label-sm text-label-sm px-4 py-2 rounded-full bg-primary-container text-on-primary transition-colors shadow-sm">All</button>',
        '<button class="filter-btn font-label-sm text-label-sm px-4 py-2 rounded-full bg-primary-container text-on-primary transition-colors shadow-sm">All</button>'
    )
    c = c.replace(
        '<button class="font-label-sm text-label-sm px-4 py-2 rounded-full bg-surface-container-high text-on-surface-variant hover:bg-surface-variant transition-colors border border-outline-variant/20">Green</button>',
        '<button class="filter-btn font-label-sm text-label-sm px-4 py-2 rounded-full bg-surface-container-high text-on-surface-variant hover:bg-surface-variant transition-colors border border-outline-variant/20">Green</button>'
    )
    c = c.replace(
        '<button class="font-label-sm text-label-sm px-4 py-2 rounded-full bg-surface-container-high text-on-surface-variant hover:bg-surface-variant transition-colors border border-outline-variant/20">Citrus</button>',
        '<button class="filter-btn font-label-sm text-label-sm px-4 py-2 rounded-full bg-surface-container-high text-on-surface-variant hover:bg-surface-variant transition-colors border border-outline-variant/20">Citrus</button>'
    )
    c = c.replace(
        '<button class="font-label-sm text-label-sm px-4 py-2 rounded-full bg-surface-container-high text-on-surface-variant hover:bg-surface-variant transition-colors border border-outline-variant/20">Tropical</button>',
        '<button class="filter-btn font-label-sm text-label-sm px-4 py-2 rounded-full bg-surface-container-high text-on-surface-variant hover:bg-surface-variant transition-colors border border-outline-variant/20">Tropical</button>'
    )
    c = c.replace(
        '<button class="font-label-sm text-label-sm px-4 py-2 rounded-full bg-surface-container-high text-on-surface-variant hover:bg-surface-variant transition-colors border border-outline-variant/20">Berry</button>',
        ''
    )
                  
    script = '''
<script>
document.addEventListener('DOMContentLoaded', () => {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cards = Array.from(document.querySelectorAll('.product-card'));
  const grid = document.querySelector('.grid.grid-cols-1');
  const sortSelect = document.querySelector('select');

  function applyFilter(category) {
    cards.forEach(card => {
      const cardCat = card.getAttribute('data-category');
      if (category === 'All' || cardCat === category) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.className = 'filter-btn font-label-sm text-label-sm px-4 py-2 rounded-full bg-surface-container-high text-on-surface-variant hover:bg-surface-variant transition-colors border border-outline-variant/20';
      });
      btn.className = 'filter-btn font-label-sm text-label-sm px-4 py-2 rounded-full bg-primary-container text-on-primary transition-colors shadow-sm';
      applyFilter(btn.textContent.trim());
    });
  });

  if (sortSelect && grid) {
    sortSelect.addEventListener('change', () => {
      const val = sortSelect.value;
      const sorted = [...cards];
      if (val.includes('Low to High')) {
        sorted.sort((a, b) => parseFloat(a.dataset.price) - parseFloat(b.dataset.price));
      } else if (val.includes('High to Low')) {
        sorted.sort((a, b) => parseFloat(b.dataset.price) - parseFloat(a.dataset.price));
      } else {
        sorted.sort((a, b) => a.dataset.title.localeCompare(b.dataset.title));
      }
      sorted.forEach(c => grid.appendChild(c));
    });
  }
});
</script>
'''
    if 'applyFilter' not in c:
        c = c.replace('</body>', script + '\n</body>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated interactive shop features in:', path)
