with open('static/website1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the literal backslashes that were injected before the class closing quotes
html = html.replace('\\" data-aos=', '" data-aos=')

with open('static/website1.html', 'w', encoding='utf-8') as f:
    f.write(html)
