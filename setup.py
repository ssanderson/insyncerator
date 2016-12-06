from setuptools import setup, find_packages
import sys

long_description = ''

if 'upload' in sys.argv:
    with open('README.rst') as f:
        long_description = f.read()


def extras_require():
    return {
        'test': [
            'tox>=2.0',
            'pytest>=2.8.5',
            'pytest-cov>=1.8.1',
            'pytest-pep8>=1.0.6',
        ],
    }


setup(
    name='insyncerator',
    version='1.0',
    description="Easily use asynchronous code synchronously.",
    author="Scott Sanderson",
    author_email="scott.b.sanderson90@gmail.com",
    packages=find_packages(),
    long_description=long_description,
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    url='https://github.com/ssanderson/insyncerator',
    install_requires=[],
    extras_require=extras_require(),
)
