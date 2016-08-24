# -*- encoding: utf-8 -*-

from distutils.core import setup

setup(
    name='rosettxta',
    version='0.0.0.20160520.1',
    author='Luis López',
    author_email='ldotlopez@gmail.com',
    packages=['rosettxta'],
    scripts=[],
    url='https://github.com/ldotlopez/rosettxta',
    license='LICENSE.txt',
    description=(
        'Automatically rename subtitles (and text files) based on the '
        'language of its contents'
    ),
    long_description=open('README').read(),
    install_requires=[
        "babelfish",
        "chardet",
        "langdetect"
    ],
)
