#!/usr/bin/env python3

import os
import ssl

from setuptools import setup

# Ignore ssl if it fails
if not os.environ.get("PYTHONHTTPSVERIFY", "") and getattr(ssl, "_create_unverified_context", None):
    ssl._create_default_https_context = ssl._create_unverified_context

setup(
    author="Mustafa Dağkıranlar",
    author_email="dagkiranlar.m@gmail.com",
    name="web browser",
    version="0.1.0",
    description="Web based file browser",
    license="MIT",
    install_requires=[
        "browsepy==0.5.6",
        "appdirs == 1.4.4"
    ],
)