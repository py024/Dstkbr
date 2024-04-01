from setuptools import setup

from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.1'
DESCRIPTION = 'A simple library'
LONG_DESCRIPTION = 'Discord'

# Setting up
setup(
    name="Dstkbr",
    version=VERSION,
    author='py24_',
    author_email='py24@sendapp.uk',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
