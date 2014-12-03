__author__ = 'Paul Dapolito'

from source.ir.easytex_element import EasyTeXElement
from source.errors.ir.memorandums.section_error import SectionError


class Section(EasyTeXElement):
    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content

        if self.title is None:
            raise SectionError("EasyTeX sections must include titles!")
        elif self.content is None:
            raise SectionError("EasyTeX sections must include content!")

    def __eq__(self, other):
        return self.title == other.title and self.content == other.content
