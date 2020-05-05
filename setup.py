import setuptools
import codecs
import os.path

with open("README.md", "r") as fh:
    long_description = fh.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name="fuzzyui",
    version=get_version("fuzzyui/__init__.py"),
    author="Frank Dice",
    author_email="frank.dice@mlb.com",
    description="Command-line fuzzy finder for CLI applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frankdice/fuzzyui",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["blessed", "fuzzywuzzy", "python-Levenshtein"],
    python_requires='>=3.6',
)
