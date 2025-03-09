"""Python setup.py for crab_moe package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("crab_moe", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="crab_moe",
    version=read("crab_moe", "VERSION"),
    description="Awesome crab_moe created by gloomyglyph",
    url="https://github.com/gloomyglyph/CRAB-MOE/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="gloomyglyph",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["crab_moe = crab_moe.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
