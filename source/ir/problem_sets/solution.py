__author__ = 'Paul Dapolito'

from source.ir.easytex_element import EasyTeXElement
from source.errors.ir.problem_sets.solution_error import SolutionError


class Solution(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise SolutionError("EasyTeX solutions cannot be empty!")

    def __eq__(self, other):
        return self.text == other.text

