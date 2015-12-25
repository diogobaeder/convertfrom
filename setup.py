import sys
import os
from setuptools import setup, find_packages


version = '0.1.0'


setup(
    name='convertfrom',
    version=version,
    description="Convert between two units",
    long_description="""\
Convert between two units""",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='conversion converter units celsius fahrenheits metric inches',
    author='Diogo Baeder',
    author_email='diogobaeder@yahoo.com.br',
    url='https://github.com/diogobaeder/convertfrom',
    license='BSD 2-clause',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points={
        'console_scripts': [
            'convertfrom = convertfrom.main:main',
        ],
    },
)
