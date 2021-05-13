from setuptools import setup, find_packages

setup(
    name='Lab2',
    version='2.0',
    url='https://github.com/DmitryMakarich',
    license='',
    author='dmitry',
    author_email='dima.makarich@mail.ru',
    description='serializer',
    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'converter=App.main:main',
        ],
    },
)
