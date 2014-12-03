__author__ = 'Paul Dapolito'

from source.ir.easytex_element import EasyTeXElement
from source.errors.ir.memorandums.content_error import ContentError


class Content(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise ContentError("EasyTeX content cannot be empty!")

    def __eq__(self, other):
        return self.text == other.text
