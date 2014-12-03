__author__ = 'Paul Dapolito'

from source.ir.easytex_element import EasyTeXElement
from source.errors.ir.problem_sets.school_error import SchoolError


class School(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise SchoolError("EasyTeX schools cannot be empty!")

    def __eq__(self, other):
        return self.text == other.text

