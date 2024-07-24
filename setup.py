from setuptools import find_packages, setup

setup(
    name="timbos-trie",
    version="0.1.8",
    author="Tim Stewart",
    author_email="tim@texastim.dev",
    description="A Trie data structure implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/timoteostewart/timbos-trie",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
