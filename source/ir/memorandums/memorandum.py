__author__ = 'Paul Dapolito'

from source.ir.easytex_element import EasyTeXElement
from source.errors.ir.memorandums.memorandum_error import MemorandumError


class Memorandum(EasyTeXElement):
    def __init__(self, author=None, collaborators=None, date=None, title=None,
                 subtitle=None, packages=None, sections=None):
        self.author = author
        self.collaborators = collaborators
        self.date = date
        self.title = title
        self.subtitle = subtitle
        self.packages = packages
        self.sections = sections

        # EasyTeX memorandums must have an author, a title, and at least one section
        if self.author is None:
            raise MemorandumError("EasyTeX memorandums must have an author!")
        elif self.title is None:
            raise MemorandumError("EasyTeX memorandums must have titles!")
        elif self.sections is None:
            raise MemorandumError("EasyTeX memorandums must have at least one section!")

    def __eq__(self, other):
        return self.author == other.author and \
               self.collaborators == other.collaborators and \
               self.date == other.date and \
               self.title == other.title and \
               self.subtitle == other.subtitle and \
               self.packages == other.packages and \
               self.sections == other.sections
