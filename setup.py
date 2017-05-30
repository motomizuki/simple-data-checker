import os
import os.path
import sys

sys.path.insert(0, os.path.abspath('lib'))

try:
    from setuptools import setup, find_packages
except ImportError:
    sys.exit(1)

install_requires = [
    "click",
    "pyyaml",
]

setup(
    name='simple_data_checker',
    version="0.1.0",
    package_dir={'': 'lib'},
    packages=find_packages('lib'),
    author="Hiroki Mizumoto",
    author_email="shuibenhonggui@gmail.com",
    url="https://github.com/motomizuki/simple-data-checker",
    description="Simple data checker",
    license="MIT License",
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    scripts=[
        'bin/simple-data-checker',
    ],
)