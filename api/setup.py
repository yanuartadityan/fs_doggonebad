import re
from setuptools import setup, find_packages

PACKAGE_NAME = 'carbon'
SOURCE_DIRECTORY = 'carbon'
SOURCE_PACKAGE_REGEX = re.compile(rf'^{SOURCE_DIRECTORY}')

source_packages = find_packages(include=[SOURCE_DIRECTORY, f'{SOURCE_DIRECTORY}.*'])
proj_packages = [SOURCE_PACKAGE_REGEX.sub(PACKAGE_NAME, name) for name in source_packages]

setup(
    name=PACKAGE_NAME,
    version='0.1.0',
    author='Yanuar Tri Aditya Nugraha',
    author_email='yanuart.adityan@gmail.com',
    description='',
    long_description='',
    url='https://github.com/yanuartadityan/fs_doggonebad.git',
    py_modules=['carbon'],
    packages = proj_packages,
    package_dir={PACKAGE_NAME: SOURCE_DIRECTORY},
    include_package_data=True,
    install_requires = [],
    python_requires='>=3.8'
)   