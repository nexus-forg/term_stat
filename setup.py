from setuptools import setup, find_packages

setup(
    name='term-stat',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'psutil>=5.9.0',
        'rich>=13.0.0',
        'click>=8.0.0',
    ],
    entry_points={
        'console_scripts': [
            'term-stat=term_stat.cli:main',
        ],
    },
    author='Ahmad',
    description='Lightweight terminal system monitor',
)
