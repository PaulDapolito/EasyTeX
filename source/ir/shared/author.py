__author__ = 'Paul Dapolito'

from source.ir.easytex_element import EasyTeXElement
from source.errors.ir.shared.author_error import AuthorError


class Author(EasyTeXElement):
    def __init__(self, name):
        self.name = name

        if self.name == "":
            raise AuthorError("EasyTeX authors cannot be empty!")

    def __eq__(self, other):
        return self.name == other.name
