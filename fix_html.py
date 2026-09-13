import re

with open('static/website1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the inline-flex rounded-full blocks for courses
html = re.sub(r'\s*<div class=\"inline-flex items-center rounded-full[^\"]+\">[^<]+</div>', '', html)

# Make course cards more compact on mobile
# p-6 -> p-5 sm:p-6 inside course-card
html = re.sub(r'<div class=\"p-6 flex-1 flex flex-col justify-between\">', '<div class=\"p-5 sm:p-6 flex-1 flex flex-col justify-between\">', html)

# text-xl font-bold -> text-lg sm:text-xl font-bold
html = re.sub(r'<h4 class=\"text-xl font-bold text-slate-900 dark:text-white mb-2\">', '<h4 class=\"text-lg sm:text-xl font-bold text-slate-900 dark:text-white mb-3\">', html)

# button py-3 -> py-2.5 sm:py-3
html = re.sub(r'class=\"w-full py-3 rounded-xl', 'class=\"w-full py-2.5 sm:py-3 rounded-xl', html)

with open('static/website1.html', 'w', encoding='utf-8') as f:
    f.write(html)
