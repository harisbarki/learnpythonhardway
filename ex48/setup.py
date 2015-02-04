try:
	from setuptools import setup
except:
	from distutils.core import setup

config = {
	'description': 'ex47',
	'author': 'w32backdoor',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'ex47'
}

setup(**config)
