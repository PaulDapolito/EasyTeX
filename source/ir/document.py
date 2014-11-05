__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from exceptions.document_exception import DocumentError


class Document(EasyTeXElement):
    def __init__(self, problem_set=None, memorandum=None):
        self.problem_set = problem_set
        self.memorandum = memorandum

        # EasyTeX document can be either a problem set OR a memorandum, but not both
        if self.problem_set and self.memorandum:
            raise DocumentError("EasyTeX document cannot be BOTH a problem set and a memorandum")

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass