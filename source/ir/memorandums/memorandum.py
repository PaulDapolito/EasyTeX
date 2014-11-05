__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.ir.memorandums.memorandum_error import MemorandumError


class Memorandum(EasyTeXElement):
    def __init__(self, author=None, collaborators=None, date=None, title=None,
                 subtitle=None, sections=None):
        self.author = author
        self.collaborators = collaborators
        self.date = date
        self.title = title
        self.subtitle = subtitle
        self.sections = sections

        # EasyTeX memorandums must have an author, a title, and at least one section
        if self.author is None:
            raise MemorandumError("EasyTeX memorandums must have an author!")
        elif self.title is None:
            raise MemorandumError("EasyTeX memorandums must have titles!")
        elif self.sections is None:
            raise MemorandumError("EasyTeX memorandums must have at least one section!")

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass