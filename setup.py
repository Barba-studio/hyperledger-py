#!/usr/bin/env python
import os
import sys
from setuptools import setup
from hyperledger import version

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

requirements = [
    'requests >= 2.5.2',
    'six >= 1.4.0',
    'websocket-client >= 0.32.0',
]

extras_require = {
    ':python_version < "3"': 'py2-ipaddress >= 3.4.1',
}

exec(open('hyperledger/version.py').read())

with open('./test-requirements.txt') as test_reqs_txt:
    test_requirements = [line for line in test_reqs_txt]


setup(
    name="hyperledger-py",
    version=version,
    description="Python client for Hyperledger.",
    url='https://github.com/hyperledger/hyperledger-py/',
    packages=[
        'hyperledger', 'hyperledger.api', 'hyperledger.utils',
    ],
    install_requires=requirements,
    tests_require=test_requirements,
    extras_require=extras_require,
    zip_safe=False,
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
    ],
)