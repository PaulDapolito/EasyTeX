__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.ir.problem_sets.label_error import LabelError


class Label(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise LabelError("EasyTeX labels cannot be empty!")

    def __eq__(self, other):
        return self.text == other.text
