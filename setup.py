#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path, getcwd
from codecs import open
from setuptools import setup, find_packages

with open(path.join(getcwd(), 'README.md')) as f:
    long_description = f.read()

setup(
    name='ontology-dapp-box',
    version='0.0.1',
    description='An DApp template project management tool based on Ontology blockchain.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='NashMiao',
    author_email='wdx7266@outlook.com',
    maintainer='NashMiao',
    maintainer_email='wdx7266@outlook.com',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    packages=find_packages(),
    install_requires=[
        'gitpython'
    ],
    python_requires='>=3.7',
    platforms=["all"],
    url='https://github.com/ontio/ontology-python-sdk',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': 'ontology-dapp-box=box.__main__:run'
    }
)
