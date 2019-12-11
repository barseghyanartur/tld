import os
import sys
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
    readme = ''

version = '0.11.2'

py_requires = ">=3.6, <4"
py_classifiers = [
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]
py_where = './src'
py_package_dir = 'src'
try:
    if sys.argv[-2] == '--python-tag' and sys.argv[-1] == 'py35':
        py_requires = ">=3.5, <3.6"
        py_classifiers = [
            "Programming Language :: Python :: 3.5",
        ]
        py_where = './src_py35'
        py_package_dir = 'src_py35'
        if sys.argv[1] == 'develop':
            sys.argv.pop(-1)
            sys.argv.pop(-1)
except Exception as err:
    pass

py_classifiers.extend([
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Development Status :: 5 - Production/Stable",
    "Topic :: Internet",
    "License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)",
    "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    "License :: OSI Approved :: GNU Lesser General Public License v2 or "
    "later (LGPLv2+)",
])
setup(
    name='tld',
    version=version,
    description="Extract the top-level domain (TLD) from the URL given.",
    long_description=readme,
    classifiers=py_classifiers,
    python_requires=py_requires,
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
    license='MPL-1.1 OR GPL-2.0-only OR LGPL-2.0-or-later',
    install_requires=[],
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
