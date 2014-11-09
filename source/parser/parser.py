__author__ = 'Paul Dapolito'

from ir.problem_sets.school import School
from errors.parser.parse_school_error import ParseSchoolError

from ir.problem_sets.course import Course
from errors.parser.parse_course_error import ParseCourseError

from ir.problem_sets.due_date import DueDate
from errors.parser.parse_due_date_error import ParseDueDateError

from ir.problem_sets.label import Label
from errors.parser.parse_label_error import ParseLabelError

from ir.problem_sets.statement import Statement
from errors.parser.parse_statement_error import ParseStatementError

from ir.problem_sets.solution import Solution
from errors.parser.parse_solution_error import ParseSolutionError

from errors.parser.parse_text_error import ParseTextError

from pyparsing import Word, Literal, Optional, ZeroOrMore, Group, OneOrMore, ParseException, delimitedList


# Terminals
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
digits = "0123456789"
symbols = "[]{}()<>\'\"=|.,;\/:-$?!*_+"
whitespace = " \t \r"

# Grammar
text = ZeroOrMore(Word(caps + lowers + digits + symbols + whitespace))

school = Literal("school: ") + text
course = Literal("course: ") + text
due_date = Literal("due_date: ") + text

label = Literal("label: ") + text
statement = Literal("statement: ") + text
solution = Literal("solution: ") + text
problem = Literal("problem: ") + Optional(label) + statement + solution


class EasyTeXParser(object):
    @staticmethod
    def parse_text(input_string):
        try:
            parsed_text = text.parseString(input_string)
        except ParseException as pex:
            raise ParseTextError("Error parsing text: {}. Exception raised: {}".format(input_string, pex))

        if parsed_text[0]:
            return parsed_text[0]
        else:
            raise ParseTextError("Error parsing text: {}".format(input_string))

    @staticmethod
    def parse_school(input_string):
        try:
            parsed_school = school.parseString(input_string)
        except ParseException as pex:
            raise ParseSchoolError("Error parsing school: {}. Exception raised: {}".format(input_string, pex))

        if parsed_school[1]:
            return School(parsed_school[1])
        else:
            raise ParseSchoolError("Error parsing school: {}".format(input_string))

    @staticmethod
    def parse_course(input_string):
        try:
            parsed_course = course.parseString(input_string)
        except ParseException as pex:
            raise ParseCourseError("Error parsing course: {}. Exception raised: {}".format(input_string, pex))

        if parsed_course[1]:
            return Course(parsed_course[1])
        else:
            raise ParseCourseError("Error parsing course: {}".format(input_string))

    @staticmethod
    def parse_due_date(input_string):
        try:
            parsed_due_date = due_date.parseString(input_string)
        except ParseException as pex:
            raise ParseDueDateError("Error parsing due date: {}. Exception raised: {}".format(input_string, pex))

        if parsed_due_date[1]:
            return DueDate(parsed_due_date[1])
        else:
            raise ParseDueDateError("Error parsing due date: {}".format(input_string))


    # TODO
    @staticmethod
    def parse_problem(input_string):
        return None

    @staticmethod
    def parse_label(input_string):
        try:
            parsed_label = label.parseString(input_string)
        except ParseException as pex:
            raise ParseLabelError("Error parsing label: {}. Exception raised: {}".format(input_string, pex))
        if parsed_label[1]:
            return Label(parsed_label[1])
        else:
            raise ParseLabelError("Error parsing label: {}".format(input_string))

    @staticmethod
    def parse_statement(input_string):
        try:
            parsed_statement = statement.parseString(input_string)
        except ParseException as pex:
            raise ParseStatementError("Error parsing statement: {}. Exception raised: {}". format(input_string, pex))

        if parsed_statement[1]:
            return Statement(parsed_statement[1])
        else:
            raise ParseStatementError("Error parsing statement: {}".format(input_string))

    @staticmethod
    def parse_solution(input_string):
        try:
            parsed_solution = solution.parseString(input_string)
        except ParseException as pex:
            raise ParseSolutionError("Error parsing solution: {}. Exception raised: {}".format(input_string, pex))

        if parsed_solution[1]:
            return Solution(parsed_solution[1])
        else:
            raise ParseSolutionError("Error parsing solution: {}".format(input_string))
