__author__ = 'Paul Dapolito'

from source.ir.easytex_element import EasyTeXElement
from source.errors.ir.problem_sets.problem_set_error import ProblemSetError


class ProblemSet(EasyTeXElement):
    def __init__(self, author=None, collaborators=None, due_date=None, title=None,
                 course=None, school=None, problems=None):
        self.author = author
        self.collaborators = collaborators
        self.due_date = due_date
        self.title = title
        self.course = course
        self.school = school
        self.problems = problems

        # EasyTeX problem set must have an author and at least one problem
        if self.author is None:
            raise ProblemSetError("EasyTeX problem sets must have an author!")
        elif self.problems is None:
            raise ProblemSetError("EasyTeX problem sets must have at least one problem!")

    def __eq__(self, other):
        return self.author == other.author and \
               self.collaborators == other.collaborators and \
               self.due_date == other.due_date and \
               self.title == other.title and \
               self.course == other.course and \
               self.school == other.school and \
               self.problems == other.problems
