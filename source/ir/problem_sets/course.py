__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.ir.problem_sets.course_error import CourseError


class Course(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise CourseError("EasyTeX courses cannot be empty!")

    def __eq__(self, other):
        return self.text == other.text
