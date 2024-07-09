#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# auth: Philip J Grabner <grabner@cadit.com>
# date: 2013/10/26
# copy: (C) Copyright 2013 Cadit Health Inc., All Rights Reserved.
# ------------------------------------------------------------------------------

import os
import sys
from setuptools import setup, find_packages

# require python 3.2
ver = sys.version_info
assert ver[0] == 3 and ver[1] >= 2, 'Requires Python 3.2 or later'

heredir = os.path.abspath(os.path.dirname(__file__))


def read(*parts, **kw):
    try:
        return open(os.path.join(heredir, *parts)).read()

    except Exception:
        return kw.get('default', '')


test_dependencies = [
    'nose                 >= 1.3.0',
    'coverage             >= 3.5.3',
]

dependencies = [
]

entrypoints = {
    'console_scripts': [
        'pwm                = passwordmeter.cli:main',
    ],
}

classifiers = [
    'Development Status :: 1 - Planning',
    # 'Development Status :: 4 - Beta',
    # 'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'License :: Public Domain',
]

setup(
    name='passwordmeter',
    version=read('VERSION.txt', default='0.0.1').strip(),
    description='A password strength measuring library.',
    long_description=read('README.rst'),
    classifiers=classifiers,
    author='Philip J Grabner, Cadit Health Inc',
    author_email='oss@cadit.com',
    url='http://github.com/cadithealth/passwordmeter',
    keywords='password strength checker meter',
    packages=find_packages(),
    platforms=['any'],
    include_package_data=True,
    zip_safe=True,
    install_requires=dependencies,
    tests_require=test_dependencies,
    test_suite='passwordmeter',
    entry_points=entrypoints,
    license='MIT (http://opensource.org/licenses/MIT)',
)
