from setuptools import setup, find_packages

setup(
    name='cyoacc',
    version='0.1.0',
    description='A module to invert colors in JSON files produced by ICC',
    author='DelicateIntegral',
    author_email='',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'cyoacc=cyoacc.core:main',
        ],
    },
)
