from setuptools import setup, find_packages

setup(
    name='Clinique',
    version='0.1.0',
    author='Yanuar Tri Aditya Nugraha',
    author_email='yanuart.adityan@gmail.com',
    description='',
    long_description='',
    url='https://github.com/yanuartadityan/fs_doggonebad.git',
    py_modules=['clinique'],
    package_dir={
        'clinique':'app'
        },
    packages = ['clinique.carbon'],
    include_package_data=False,
    install_requires = [],
    python_requires='>=3.8'
)   