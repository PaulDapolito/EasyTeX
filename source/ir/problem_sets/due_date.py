__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.ir.problem_sets.due_date_error import DueDateError


class DueDate(EasyTeXElement):
    def __init__(self, date_string):
        self.date_string = date_string

        if self.date_string == "":
            raise DueDateError("EasyTeX due dates cannot be empty!")

    def __eq__(self, other):
        return self.date_string == other.date_string
