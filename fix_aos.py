import re

with open('static/website1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix incorrectly placed AOS tags
replacements = [
    ('mb-4 sm:mb-6\"> data-aos=\"fade-up\"', 'mb-4 sm:mb-6\" data-aos=\"fade-up\">'),
    ('leading-relaxed\"> data-aos=\"fade-up\" data-aos-delay=\"100\"', 'leading-relaxed\" data-aos=\"fade-up\" data-aos-delay=\"100\">'),
    ('dark:border-slate-700/50\"> data-aos=\"zoom-in\" data-aos-delay=\"200\"', 'dark:border-slate-700/50\" data-aos=\"zoom-in\" data-aos-delay=\"200\">'),
    ('hover:shadow-xl transition-all\"> data-aos=\"fade-up\"', 'hover:shadow-xl transition-all\" data-aos=\"fade-up\">'),
    ('flex-col\"> data-aos=\"fade-up\"', 'flex-col\" data-aos=\"fade-up\">'),
    ('text-center group\"> data-aos=\"fade-up\"', 'text-center group\" data-aos=\"fade-up\">'),
    ('lg:col-span-5\"> data-aos=\"fade-right\"', 'lg:col-span-5\" data-aos=\"fade-right\">'),
    ('lg:col-span-7\"> data-aos=\"fade-left\"', 'lg:col-span-7\" data-aos=\"fade-left\">')
]

for old, new in replacements:
    html = html.replace(old, new)

with open('static/website1.html', 'w', encoding='utf-8') as f:
    f.write(html)
