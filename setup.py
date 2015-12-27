import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from wagtailconstance import __version__



os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name="wagtail-constance",
    version=__version__,
    description="django-constance integration for Wagtail CMS",
    long_description=open('README.rst').read(),
    url='http://github.com/MechanisM/wagtail-constance',
    author='Eugene MechanisM',
    author_email='eugene@mechanism.pro',
    license='MIT',
    zip_safe = False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='django, config, constance',
    packages=find_packages(),
    include_package_data=True
)