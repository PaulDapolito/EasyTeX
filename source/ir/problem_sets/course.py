__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.problem_sets.course_error import CourseError


class Course(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise CourseError("EasyTeX courses cannot be empty!")

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass
