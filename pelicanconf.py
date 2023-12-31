AUTHOR = 'Fredrik Skatland'
SITENAME = 'Hello world'
SITEURL = 'https://fredrikskatland.com'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/fredrik-skatland-21b35a6b/'),
          ('GitHub', 'https://github.com/fredrikskatland'),
          ('HuggingFace', 'https://huggingface.co/fredrikskatland'),)


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

THEME = "./themes/mediumfox"

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = 5

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

#AUTHOR_TWITTER = 'your_twitter_username'  # if you have one, otherwise you can comment or skip this line
AUTHOR_LINKEDIN= 'fredrik-skatland-21b35a6b'
AUTHOR_GITHUB = 'fredrikskatland'
AUTHOR_HUGGINGFACE = 'fredrikskatland'
