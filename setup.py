"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
Autogenerated by poetry-setup:
https://github.com/orsinium/poetry-setup
"""
# IMPORTANT: this file is autogenerated. Do not edit it manually.
# All changes will be lost after `poetry-setup` command execution.
# ----------------------------------------------------------------
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open
here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, ''), encoding='utf-8') as f:
    long_description = f.read()
# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
setup(
    # https://packaging.python.org/specifications/core-metadata/#name
    name='chineseviewer',  # Required
    # https://www.python.org/dev/peps/pep-0440/
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',  # Required
    # https://packaging.python.org/specifications/core-metadata/#summary
    description="ChineseViewer with login, rewritten in Mithril.js",  # Required
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    author="patarapolw",  # Optional
    author_email="patarapolw@gmail.com",  # Optional
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],  # Optional
    packages=find_packages(),  # Required
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'flask (>=1.0,<2.0)',
        'wordfreq (>=2.2,<3.0)',
        'jieba (>=0.39.0,<0.40.0)',
        'pinyin (>=0.4.0,<0.5.0)',
        'gunicorn (>=19.9,<20.0)',
        'python-dotenv (>=0.10.1,<0.11.0)',
        'flask_cors (>=3.0,<4.0)',
        'regex (==2018.02.21)',
        'flask-sqlalchemy (>=2.3,<3.0)',
        'psycopg2-binary (>=2.7,<3.0)',
        'flask-migrate (>=2.3,<3.0)',
    ],  # Optional
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#dependencies-that-aren-t-in-pypi
    dependency_links=[],  # Optional
    # https://stackoverflow.com/a/16576850
    include_package_data=True,
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    project_urls={  # Optional
    },
)
