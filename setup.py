# AUTHOR
# Artur Barseghyan (artur.barseghyan@gmail.com)
# 
# DESCRIPTION
# Extracts the top level domain (TLD) from the URL given. List of TLD names is taken from
# http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/effective_tld_names.dat?raw=1 See "readme.txt" file for
# more.

import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'readme.rst')).read()
except:
    readme = ''

version = '0.3'

data_dir = "src/tld/res"
data = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]

setup(
    name = 'tld',
    version = version,
    description = ("Extracts the top level domain (TLD) from the URL given."),
    long_description = readme,
    classifiers = [
        "Programming Language :: Python",
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = 'tld, top level domain names, python',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://bitbucket.org/barseghyanartur/tld',
    package_dir = {'':'src'},
    packages = find_packages(where='./src'),
    package_data = {'tld': data},
    include_package_data = True,
    license = 'GPL 2.0/LGPL 2.1',
)
