__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.title_error import TitleError


class Title(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise TitleError("EasyTeX titles cannot be empty!")

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass
