#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zerohunter',
    version='0.1.0',
    description='Advanced Linux Tool for Zero-Day Attack Detection',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ZeroHunter Team',
    author_email='info@zerohunter.io',
    url='https://github.com/zerohunter/zerohunter',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy>=1.19.0',
        'pandas>=1.1.0',
        'scikit-learn>=0.23.0',
        'tensorflow>=2.3.0',
        'PyQt5>=5.15.0',
        'pypcap>=1.2.3',
        'psutil>=5.7.0',
        'yara-python>=4.0.0',
        'requests>=2.24.0',
        'matplotlib>=3.3.0',
        'seaborn>=0.11.0',
    ],
    entry_points={
        'console_scripts': [
            'zerohunter=zerohunter.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: POSIX :: Linux',
        'Topic :: Security',
    ],
    python_requires='>=3.8',
    license='GPL-3.0',
)
