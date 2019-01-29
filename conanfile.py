#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostRangeConan(base.BoostBaseConan):
    name = "boost_range"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_range"
    lib_short_names = ["range"]
    header_only_libs = ["range"]
    cycle_group = "boost_cycle_group_a"
    b2_requires = ["boost_cycle_group_a"]
