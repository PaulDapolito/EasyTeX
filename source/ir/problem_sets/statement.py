__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.ir.problem_sets.statement_error import StatementError


class Statement(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise StatementError("EasyTeX statements cannot be empty!")

    def __eq__(self, other):
        return self.text == other.text

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass
