__author__ = 'Paul Dapolito'

from source.ir.easytex_element import EasyTeXElement
from source.errors.ir.shared.package_error import PackageError


class Package(EasyTeXElement):
    def __init__(self, name):
        self.name = name

        if self.name == "":
            raise PackageError("EasyTeX packages cannot be empty!")

    def __eq__(self, other):
        return self.name == other.name
