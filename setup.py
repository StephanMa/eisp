from configparser import ConfigParser

from setuptools import find_packages, setup
from eisp.utils import defaultconfig
with open('LICENSE') as f: legal = f.read()
with open('README.md') as f: readme = f.read()

config = ConfigParser()
config.read_dict(defaultconfig())

setup(
  author = 'Francisco Mondaca',
  author_email = 'f.mondaca@uni-koeln.de',
  description = config.get('info', 'desc'),
  download_url = config.get('info', 'repo'),
  entry_points = { 'console_scripts': ['eisp = eisp.eisp:main'] },
  license = legal,
  long_description = readme,
  maintainer_email = config.get('info', 'mail'),
  name = config.get('info', 'name'),
  packages = find_packages(),
  platforms = ['linux'],
  url = config.get('info', 'link'),
  version = '0.0.1'
)
