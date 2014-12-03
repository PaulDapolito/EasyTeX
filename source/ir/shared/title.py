__author__ = 'Paul Dapolito'

from source.ir.easytex_element import EasyTeXElement
from source.errors.ir.shared.title_error import TitleError


class Title(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise TitleError("EasyTeX titles cannot be empty!")

    def __eq__(self, other):
        return self.text == other.text
