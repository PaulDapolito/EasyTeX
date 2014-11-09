__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.ir.document_error import DocumentError


class Document(EasyTeXElement):
    def __init__(self, problem_set=None, memorandum=None):
        self.problem_set = problem_set
        self.memorandum = memorandum

        # EasyTeX document can be either a problem set or a memorandum, but not both
        if self.problem_set and self.memorandum:
            raise DocumentError("EasyTeX document cannot be BOTH a problem set and a memorandum!")
        elif self.problem_set is None and self.memorandum is None:
            raise DocumentError("EasyTeX document must be a problem set or a memorandum!")

    def __eq__(self, other):
        return self.problem_set == other.problem_set and self.memorandum == other.memorandum

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass