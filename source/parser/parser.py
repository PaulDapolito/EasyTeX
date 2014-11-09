__author__ = 'Paul Dapolito'

from pyparsing import Word, Literal, Optional, ZeroOrMore, OneOrMore, ParseException, delimitedList

from ir.problem_sets.school import School
from errors.parser.problem_sets.parse_school_error import ParseSchoolError
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
from errors.parser.shared.parse_text_error import ParseTextError



# Terminals
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
digits = "0123456789"
symbols = "[]{}()<>\'\"=|.,;\/:-$?!*_+"
whitespace = "\s \t \r"

# Grammar
text = ZeroOrMore(Word(caps + lowers + digits + symbols + whitespace))

solution = Literal("solution:\n") + text
statement = Literal("statement: ") + text
label = Literal("label: ") + text
problem = Literal("problem:\n") + Optional(label) + statement + solution  # TODO: Spacing

due_date = Literal("due_date: ") + text
course = Literal("course: ") + text
school = Literal("school: ") + text

subtitle = Literal("subtitle: ") + text
title = Literal("title: ") + text
date = Literal("date: ") + text
collaborators = Literal("collaborators: ") + delimitedList(text, delim=",", combine=True)
author = Literal("author: ") + text

content = Literal("content:\n") + Literal("\t") + text
section = Literal("section:\n") + Literal("\t") + title + Literal("\n") + content

problem_set = Literal("problem_set:\n") + Literal("\n") + Literal("\t") + author + ZeroOrMore(collaborators) \
                                        + Optional(due_date) + Optional(title) + Optional(course) + Optional(school) \
                                        + OneOrMore(problem)

memorandum = Literal("memorandum:\n") + Literal("\n") + Literal("\t") + author + ZeroOrMore(collaborators) \
                                      + Optional(date) + title + Optional(subtitle) + OneOrMore(section)

document = memorandum | problem_set


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
    def parse_solution(input_string):
        try:
            parsed_solution = solution.parseString(input_string)
        except ParseException as pex:
            raise ParseSolutionError("Error parsing solution: {}. Exception raised: {}".format(input_string, pex))

        if parsed_solution[1]:
            return Solution(parsed_solution[1])
        else:
            raise ParseSolutionError("Error parsing solution: {}".format(input_string))

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
    def parse_label(input_string):
        try:
            parsed_label = label.parseString(input_string)
        except ParseException as pex:
            raise ParseLabelError("Error parsing label: {}. Exception raised: {}".format(input_string, pex))
        if parsed_label[1]:
            return Label(parsed_label[1])
        else:
            raise ParseLabelError("Error parsing label: {}".format(input_string))

    # TODO
    @staticmethod
    def parse_problem(input_string):
        return None

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
    def parse_school(input_string):
        try:
            parsed_school = school.parseString(input_string)
        except ParseException as pex:
            raise ParseSchoolError("Error parsing school: {}. Exception raised: {}".format(input_string, pex))

        if parsed_school[1]:
            return School(parsed_school[1])
        else:
            raise ParseSchoolError("Error parsing school: {}".format(input_string))

    # TODO
    @staticmethod
    def parse_subtitle(input_string):
        return None

    # TODO
    @staticmethod
    def parse_title(input_string):
        return None

    # TODO
    @staticmethod
    def parse_date(input_string):
        return None

    # TODO
    @staticmethod
    def parse_collaborators(input_string):
        return None

    # TODO
    @staticmethod
    def parse_author(input_string):
        return None

    # TODO
    @staticmethod
    def parse_content(input_string):
        return None

    # TODO
    @staticmethod
    def parse_section(input_string):
        return None

    # TODO
    @staticmethod
    def parse_problem_set(input_string):
        return None

    # TODO
    @staticmethod
    def parse_memorandum(input_string):
        return None

    # TODO
    @staticmethod
    def parse_document(input_string):
        return None