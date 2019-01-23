#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostRangeConan(base.BoostBaseConan):
    name = "boost_range"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_range"
    lib_short_names = ["range"]
    header_only_libs = ["range"]
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_concept_check",
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_detail",
        "boost_iterator",
        "boost_mpl",
        "boost_numeric_conversion",
        "boost_optional",
        "boost_preprocessor",
        "boost_regex",
        "boost_static_assert",
        "boost_tuple",
        "boost_type_traits",
        "boost_utility"
    ]


