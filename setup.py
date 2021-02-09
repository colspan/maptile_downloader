#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup maptile_downloader
"""

import sys
from setuptools import setup, find_packages

sys.path.append("./test")

setup(
    name="maptile_downloader",
    version="1.0",
    packages=find_packages("src"),
    py_modules=["maptile_downloader"],
    test_suite="foo_test.suite",
    package_dir={"": "src"},
    install_requires=["requests", "luigi", "pillow"],
    entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      maptile_downloader = maptile_downloader:download
      """,
)
