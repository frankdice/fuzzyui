import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fuzzyui",
    version="0.1.0a1",
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
