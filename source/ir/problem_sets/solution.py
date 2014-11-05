__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.problem_sets.solution_error import SolutionError


class Solution(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise SolutionError("EasyTeX solutions cannot be empty!")

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass
