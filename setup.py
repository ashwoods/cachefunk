import codecs
import os

from setuptools import find_packages, setup


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


setup(
    name="cachefunk",
    version="0.1.0",
    url='https://github.com/ashwoods/cachefunk',
    license='MIT',
    description="Sitemap.xml cache warmer",
    long_description=read('README.rst'),
    author='Ashley Camba Garrido',
    author_email='ashwoods@gmail.com',
    entry_points={
        'console_scripts': [
            'cachefunk = cachefunk.cli:cli',
        ],
    },
    packages=find_packages(exclude=['docs', 'tests*']),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    install_requires=[
        'attrs',
        'cached_property',
        'click',
        'click-log',
        'defusedxml',
        'grequests',
        'requests',
        'structlog',
        'tqdm',
    ],
    zip_safe=False,
)
