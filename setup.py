import os
import sys
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
    readme = ''

version = '0.12.5'

py_where = './src'
py_package_dir = 'src'
try:
    if sys.argv[-2] == '--python-tag':
        # For Python 3.5
        if sys.argv[-1] == 'py35':
            py_where = './src_py35'
            py_package_dir = 'src_py35'

        # For Python 2.7
        elif sys.argv[-1] == 'py27':
            py_where = './src_py27'
            py_package_dir = 'src_py27'

        # For development mode
        if sys.argv[1] in ('develop', 'install',):
            sys.argv.pop(-1)
            sys.argv.pop(-1)
except Exception as err:
    pass

setup(
    name='tld',
    version=version,
    description="Extract the top-level domain (TLD) from the URL given.",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Internet",
        "License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or "
        "later (LGPLv2+)",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/barseghyanartur/tld/issues",
        "Documentation": "https://tld.readthedocs.io/",
        "Source Code": "https://github.com/barseghyanartur/tld/",
        "Changelog": "https://tld.readthedocs.io/en/latest/changelog.html",
    },
    python_requires=">=2.7, <4",
    keywords='tld, top-level domain names, python',
    author='Artur Barseghyan',
    author_email='artur.barseghyan@gmail.com',
    url='https://github.com/barseghyanartur/tld',
    package_dir={'': py_package_dir},
    packages=find_packages(where=py_where),
    entry_points={
        'console_scripts': [
            'update-tld-names = tld.utils:update_tld_names_cli'
        ]
    },
    include_package_data=True,
    license='MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-or-later',
    install_requires=[
        'six;python_version<="3.5"',  # Used in Python 2.7 and 3.5 dist
        'typing;python_version<"3.5"',  # Used in Python < 3.5 dist
        'backports.functools-lru-cache;python_version<"3.5"',  # For Python 2.7
    ],
    test_suite='tld.tests',
    tests_require=[
        'coverage',
        'factory_boy',
        'Faker',
        'pytest-cov',
        'pytest',
        'tox',
    ]
)
