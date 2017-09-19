from conans import ConanFile, tools, os

class BoostRangeConan(ConanFile):
    name = "Boost.Range"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-range"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["range"]
    requires =  "Boost.Array/1.65.1@bincrafters/stable", \
                      "Boost.Assert/1.65.1@bincrafters/stable", \
                      "Boost.Concept_Check/1.65.1@bincrafters/stable", \
                      "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Core/1.65.1@bincrafters/stable", \
                      "Boost.Detail/1.65.1@bincrafters/stable", \
                      "Boost.Functional/1.65.1@bincrafters/stable", \
                      "Boost.Iterator/1.65.1@bincrafters/stable", \
                      "Boost.Mpl/1.65.1@bincrafters/stable", \
                      "Boost.Numeric_Conversion/1.65.1@bincrafters/stable", \
                      "Boost.Optional/1.65.1@bincrafters/stable", \
                      "Boost.Preprocessor/1.65.1@bincrafters/stable", \
                      "Boost.Regex/1.65.1@bincrafters/stable", \
                      "Boost.Static_Assert/1.65.1@bincrafters/stable", \
                      "Boost.Tuple/1.65.1@bincrafters/stable", \
                      "Boost.Type_Traits/1.65.1@bincrafters/stable",\
                      "Boost.Utility/1.65.1@bincrafters/stable"

                      #array3 assert1 concept_check5 config0 core2 detail5 functional5 iterator5 mpl5 numeric~conversion6 optional5 preprocessor0 regex6 static_assert1 tuple4 type_traits3 utility5

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()