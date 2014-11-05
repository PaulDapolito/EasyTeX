__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.label_error import LabelError


class Label(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise LabelError("EasyTeX labels cannot be empty!")

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass
