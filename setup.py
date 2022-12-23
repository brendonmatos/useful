#!/usr/bin/python

import setuptools

with open("requirements.txt") as f:
    required = f.read().splitlines()


setuptools.setup(
    name="brendon-useful",
    version="1.0",
    packages=setuptools.find_packages(),
    install_requires=required,
    entry_points={
        "console_scripts": [
            "useful_renamer = renamer:main",
            "useful_duplicator = duplicator:main",
            "useful_chat = chat:main",
        ],
    },
    include_package_data=True,
)
