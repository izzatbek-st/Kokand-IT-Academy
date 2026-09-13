import re

with open('static/website1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Director
director_old = """            <div class="text-center group mb-12">
                <div class="relative w-40 h-40 mx-auto rounded-full overflow-hidden mb-4 ring-4 ring-blue-500/20 group-hover:ring-blue-500 transition-all">
                    <img src="images/Direktor.jpg" alt="Ta'lim markazi direktori" class="w-full h-full object-cover">
                </div>
                <h4 class="text-sm sm:text-lg font-bold text-slate-900 dark:text-white">Direktor</h4>
                <p class="text-[10px] sm:text-xs text-blue-600 dark:text-blue-400 font-semibold mb-1 sm:mb-2">Ta'lim markazi rahbari</p>"""

director_new = """            <div class="text-center group mb-8 sm:mb-12">
                <div class="relative w-24 sm:w-40 h-24 sm:h-40 mx-auto rounded-full overflow-hidden mb-3 sm:mb-4 ring-2 sm:ring-4 ring-blue-500/20 group-hover:ring-blue-500 transition-all">
                    <img src="images/Direktor.jpg" alt="Erkinov Jasurbek" class="w-full h-full object-cover">
                </div>
                <h4 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white">Erkinov Jasurbek</h4>
                <p class="text-xs text-blue-600 dark:text-blue-400 font-semibold mb-1 sm:mb-2">Direktor</p>"""

html = html.replace(director_old, director_new)

# 2. Update About section
html = html.replace('p-8 rounded-3xl bg-slate-50', 'p-5 sm:p-8 rounded-2xl sm:rounded-3xl bg-slate-50')
html = html.replace('w-14 h-14 rounded-2xl', 'w-10 sm:w-14 h-10 sm:h-14 rounded-xl sm:rounded-2xl')
html = html.replace('text-2xl mb-6', 'text-lg sm:text-2xl mb-3 sm:mb-6')
html = html.replace('text-xl font-bold mb-3', 'text-[15px] sm:text-xl font-bold mb-1.5 sm:mb-3 leading-tight sm:leading-normal')
html = html.replace('text-sm leading-relaxed', 'text-[11px] sm:text-sm leading-relaxed')

# 3. Update Contact info items
html = html.replace('space-y-6', 'space-y-4 sm:space-y-6')
html = html.replace('w-12 h-12 rounded-xl bg-blue-100', 'w-10 sm:w-12 h-10 sm:h-12 rounded-lg sm:rounded-xl bg-blue-100')
html = html.replace('w-12 h-12 rounded-xl bg-indigo-100', 'w-10 sm:w-12 h-10 sm:h-12 rounded-lg sm:rounded-xl bg-indigo-100')
html = html.replace('w-12 h-12 rounded-xl bg-purple-100', 'w-10 sm:w-12 h-10 sm:h-12 rounded-lg sm:rounded-xl bg-purple-100')
html = html.replace('text-lg\">\n                                <i', 'text-base sm:text-lg\">\n                                <i')

# 4. Form area
html = html.replace('p-8 rounded-3xl shadow-xl', 'p-5 sm:p-8 rounded-2xl sm:rounded-3xl shadow-xl')
html = html.replace('text-xl font-bold text-slate-900 dark:text-white mb-6', 'text-lg sm:text-xl font-bold text-slate-900 dark:text-white mb-3 sm:mb-6')
html = html.replace('text-sm text-slate-600 dark:text-slate-300 mb-6', 'text-xs sm:text-sm text-slate-600 dark:text-slate-300 mb-4 sm:mb-6')

# 5. Form inputs
html = html.replace('px-4 py-3 rounded-xl', 'px-3 sm:px-4 py-2 sm:py-3 rounded-lg sm:rounded-xl text-sm sm:text-base')
html = html.replace('py-3.5 rounded-xl bg-blue-600', 'py-2.5 sm:py-3.5 rounded-lg sm:rounded-xl bg-blue-600')

with open('static/website1.html', 'w', encoding='utf-8') as f:
    f.write(html)
