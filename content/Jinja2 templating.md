Title: Jinja2 templating
Date: 2023-08-27
Category: Blog



**Tell me about Jinja2 templating**

Certainly!

Jinja2 is a popular text-based templating engine for Python. It allows you to create templates that can be rendered with data to produce text outputs, such as HTML, XML, or any other structured text format.

Here's a brief overview:

### Basic Syntax:

1. **Variables**: You can insert variables into your templates using the double curly braces, `{{ }}`.

   ```jinja2
   Hello, {{ name }}!
   ```

2. **Control Structures**: Jinja2 supports control structures, which are wrapped in `{% %}`.

   - **For loops**:
     ```jinja2
     <ul>
     {% for item in list %}
         <li>{{ item }}</li>
     {% endfor %}
     </ul>
     ```

   - **If statements**:
     ```jinja2
     {% if user_is_logged_in %}
         Welcome back, {{ user_name }}!
     {% else %}
         Please log in.
     {% endif %}
     ```

### Filters:

Filters are used to transform the output. They are separated from the variable by a pipe `|`.

   ```jinja2
   {{ name|upper }}  # Outputs the value of name in uppercase
   ```

Some common filters include `lower`, `upper`, `trim`, `default`, and many others.

### Macros:

Macros are similar to functions in Python. They allow for reusable components in the template.

```jinja2
{% macro input(name, value='', type='text') %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}"/>
{% endmacro %}
```

### Template Inheritance:

Jinja2 supports inheritance, which allows you to define a base template and then extend or override parts of it in child templates.

- **Base template (base.html)**:

  ```jinja2
  <html>
    <head>
      <title>{% block title %}Default Title{% endblock %}</title>
    </head>
    <body>
      {% block content %}{% endblock %}
    </body>
  </html>
  ```

- **Child template (child.html)**:

  ```jinja2
  {% extends "base.html" %}
  
  {% block title %}Child Page Title{% endblock %}
  
  {% block content %}
    <p>This is the content of the child page.</p>
  {% endblock %}
  ```

### Integration with Python:

You'll typically render Jinja2 templates in a Python application. Here's a simple example using Flask:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="John")
```

In this case, the `index.html` template would be a Jinja2 template, and the `render_template` function would process it with the provided data (`name="John"`).

Given your proficiency in Python, you might find Jinja2 very intuitive and straightforward to use, especially when combined with frameworks like Flask or Django, which heavily utilize templating for web page generation.