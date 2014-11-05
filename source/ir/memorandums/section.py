__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.ir.memorandums.section_error import SectionError


class Section(EasyTeXElement):
    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content

        if self.title is None:
            raise SectionError("EasyTeX sections must include titles!")
        elif self.content is None:
            raise SectionError("EasyTeX sections must include content!")

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass
