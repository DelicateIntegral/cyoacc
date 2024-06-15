from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cyoacc',
    version='0.2.0',
    description='A module to invert colors in JSON files produced by ICC',
    author='DelicateIntegral',
    author_email='',
    description="CYOA Color Converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DelicateIntegral/cyoacc",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: AGPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
