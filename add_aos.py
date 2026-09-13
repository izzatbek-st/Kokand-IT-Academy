import re

with open('static/website1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add AOS CSS
if 'aos.css' not in html:
    html = html.replace('</head>', '    <!-- AOS CSS -->\n    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n</head>')

# Add AOS JS & Init
if 'aos.js' not in html:
    aos_scripts = """    <!-- AOS JS -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({
            once: true,
            duration: 800,
            offset: 100,
        });
    </script>
</body>"""
    html = html.replace('</body>', aos_scripts)

# Add animations to hero section
html = re.sub(r'(<h1 class=\"[^\"]*?)(mb-4 sm:mb-6\">)', r'\1\2 data-aos="fade-up"', html)
html = re.sub(r'(<p class=\"[^\"]*?)(leading-relaxed\">)', r'\1\2 data-aos="fade-up" data-aos-delay="100"', html)
html = re.sub(r'(<div class=\"flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 mb-12\">)', r'\1\n<!--aos-->', html)
html = html.replace('mb-12\">\n<!--aos-->', 'mb-12\" data-aos=\"fade-up\" data-aos-delay=\"200\">')
html = re.sub(r'(<div class=\"grid grid-cols-3 gap-2 sm:gap-4 pt-6 sm:pt-8 border-t border-slate-200 dark:border-slate-800\">)', r'\1\n<!--aos2-->', html)
html = html.replace('dark:border-slate-800\">\n<!--aos2-->', 'dark:border-slate-800\" data-aos=\"fade-up\" data-aos-delay=\"300\">')

# Add animation to hero image
html = re.sub(r'(<div class=\"relative glass-card p-6 sm:p-8 rounded-3xl shadow-2xl border border-slate-200/50 dark:border-slate-700/50)(\">)', r'\1\" data-aos="zoom-in" data-aos-delay="200">', html)

# Add animation to About sections
# The divs are: <div class="p-5 sm:p-8 rounded-2xl...
html = re.sub(r'(<div class=\"p-5 sm:p-8 rounded-2xl sm:rounded-3xl bg-slate-50 dark:bg-slate-800 border border-slate-100 dark:border-slate-700/50 hover:shadow-xl transition-all)(\">)', r'\1\" data-aos="fade-up">', html)

# Add animations to Courses
html = re.sub(r'(<div class=\"course-card[^\"]*?)(\">)', r'\1\" data-aos="fade-up">', html)

# Add animations to Teachers
# The teacher cards are: <div class="text-center group"> inside <div class="grid grid-cols-2 lg:grid-cols-4...
html = re.sub(r'(<div class=\"text-center group)(\">)', r'\1\" data-aos="fade-up">', html)

# Add animations to Contact info
html = re.sub(r'(<div class=\"lg:col-span-5)(\">)', r'\1\" data-aos="fade-right">', html)
html = re.sub(r'(<div class=\"lg:col-span-7)(\">)', r'\1\" data-aos="fade-left">', html)

with open('static/website1.html', 'w', encoding='utf-8') as f:
    f.write(html)
