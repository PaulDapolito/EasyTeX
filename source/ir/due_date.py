__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.due_date_error import DueDateError


class DueDate(EasyTeXElement):
    def __init__(self, date_string):
        self.date_string = date_string

        if self.date_string == "":
            raise DueDateError("EasyTeX due dates cannot be empty!")

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass
