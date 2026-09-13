import re

with open('static/website1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make courses 2 columns on mobile
html = re.sub(r'grid-cols-1 md:grid-cols-2 lg:grid-cols-3', 'grid-cols-2 lg:grid-cols-3', html)
# Reduce gap for courses
html = re.sub(r'gap-8\" id=\"courseGrid\"', 'gap-3 sm:gap-8\" id=\"courseGrid\"', html)

# Make teacher 2 columns on mobile
html = re.sub(r'grid-cols-1 sm:grid-cols-2 lg:grid-cols-4', 'grid-cols-2 lg:grid-cols-4', html)
# Reduce gap for teachers
html = re.sub(r'lg:grid-cols-4 gap-8', 'lg:grid-cols-4 gap-4 sm:gap-8', html)

# Shrink course cards for 2-column mobile
# Padding inside course card
html = re.sub(r'<div class=\"p-5 sm:p-6 flex-1', '<div class=\"p-3 sm:p-6 flex-1', html)
# Number badge
html = re.sub(r'mb-4 px-3 py-1 rounded-full bg-blue-100 text-blue-700 text-xs', 'mb-2 sm:mb-4 px-2 py-0.5 sm:px-3 sm:py-1 rounded-full bg-blue-100 text-blue-700 text-[10px] sm:text-xs', html)
html = re.sub(r'mb-4 px-3 py-1 rounded-full bg-teal-100 text-teal-700 text-xs', 'mb-2 sm:mb-4 px-2 py-0.5 sm:px-3 sm:py-1 rounded-full bg-teal-100 text-teal-700 text-[10px] sm:text-xs', html)
html = re.sub(r'mb-4 px-3 py-1 rounded-full bg-violet-100 text-violet-700 text-xs', 'mb-2 sm:mb-4 px-2 py-0.5 sm:px-3 sm:py-1 rounded-full bg-violet-100 text-violet-700 text-[10px] sm:text-xs', html)
html = re.sub(r'mb-4 px-3 py-1 rounded-full bg-indigo-100 text-indigo-700 text-xs', 'mb-2 sm:mb-4 px-2 py-0.5 sm:px-3 sm:py-1 rounded-full bg-indigo-100 text-indigo-700 text-[10px] sm:text-xs', html)
html = re.sub(r'mb-4 px-3 py-1 rounded-full bg-cyan-100 text-cyan-700 text-xs', 'mb-2 sm:mb-4 px-2 py-0.5 sm:px-3 sm:py-1 rounded-full bg-cyan-100 text-cyan-700 text-[10px] sm:text-xs', html)
html = re.sub(r'mb-4 px-3 py-1 rounded-full bg-red-100 text-red-700 text-xs', 'mb-2 sm:mb-4 px-2 py-0.5 sm:px-3 sm:py-1 rounded-full bg-red-100 text-red-700 text-[10px] sm:text-xs', html)
html = re.sub(r'mb-4 px-3 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs', 'mb-2 sm:mb-4 px-2 py-0.5 sm:px-3 sm:py-1 rounded-full bg-yellow-100 text-yellow-700 text-[10px] sm:text-xs', html)
html = re.sub(r'mb-4 px-3 py-1 rounded-full bg-purple-100 text-purple-700 text-xs', 'mb-2 sm:mb-4 px-2 py-0.5 sm:px-3 sm:py-1 rounded-full bg-purple-100 text-purple-700 text-[10px] sm:text-xs', html)
html = re.sub(r'mb-4 px-3 py-1 rounded-full bg-pink-100 text-pink-700 text-xs', 'mb-2 sm:mb-4 px-2 py-0.5 sm:px-3 sm:py-1 rounded-full bg-pink-100 text-pink-700 text-[10px] sm:text-xs', html)

# Course Title
html = re.sub(r'<h4 class=\"text-lg sm:text-xl font-bold text-slate-900 dark:text-white mb-3\">', '<h4 class=\"text-[13px] sm:text-xl font-bold leading-tight sm:leading-normal text-slate-900 dark:text-white mb-2 sm:mb-3\">', html)
# Course Button
html = re.sub(r'class=\"w-full py-2.5 sm:py-3 rounded-xl bg-slate-900 hover:bg-slate-800 dark:bg-blue-600 dark:hover:bg-blue-700 text-white font-semibold text-sm transition-colors\">', 'class=\"w-full py-1.5 sm:py-3 rounded-lg sm:rounded-xl bg-slate-900 hover:bg-slate-800 dark:bg-blue-600 dark:hover:bg-blue-700 text-white font-semibold text-[11px] sm:text-sm transition-colors\">', html)

# Shrink Teacher cards for 2-column mobile
# Image size
html = re.sub(r'class=\"relative w-32 sm:w-40 h-32 sm:h-40 mx-auto rounded-full overflow-hidden mb-3 sm:mb-4 ring-4', 'class=\"relative w-20 sm:w-40 h-20 sm:h-40 mx-auto rounded-full overflow-hidden mb-2 sm:mb-4 ring-2 sm:ring-4', html)
html = re.sub(r'class=\"text-lg font-bold', 'class=\"text-sm sm:text-lg font-bold', html)
html = re.sub(r'class=\"text-xs text-blue-600 dark:text-blue-400 font-semibold mb-2\">', 'class=\"text-[10px] sm:text-xs text-blue-600 dark:text-blue-400 font-semibold mb-1 sm:mb-2\">', html)
html = re.sub(r'class=\"text-xs text-slate-500 dark:text-slate-400\">', 'class=\"text-[9px] sm:text-xs leading-tight sm:leading-normal text-slate-500 dark:text-slate-400\">', html)

with open('static/website1.html', 'w', encoding='utf-8') as f:
    f.write(html)
