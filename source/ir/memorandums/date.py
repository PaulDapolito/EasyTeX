__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.ir.memorandums.date_error import DateError


class Date(EasyTeXElement):
    def __init__(self, date_string):
        self.date_string = date_string

        if self.date_string == "":
            raise DateError("EasyTeX dates cannot be empty!")

    def __eq__(self, other):
        return self.date_string == other.date_string

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass
