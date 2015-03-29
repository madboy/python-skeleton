try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Kristofer Lindberg',
        'url': 'https://www.github.com',
        'download_url': 'https://www.github.com',
        'author_email': 'k.lindberg@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'ulan bator'
        }

setup(**config)
