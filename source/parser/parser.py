__author__ = 'Paul Dapolito'

from pyparsing import Word, Literal, White, Optional, ZeroOrMore, OneOrMore, ParseException, delimitedList, Combine

from errors.parser.shared.parse_text_error import ParseTextError

from ir.shared.author import Author
from errors.parser.shared.parse_author_error import ParseAuthorError

from ir.shared.collaborator import Collaborator
from errors.parser.shared.parse_collaborators_error import ParseCollaboratorsError

from ir.memorandums.date import Date
from errors.parser.memorandums.parse_date_error import ParseDateError

from ir.shared.title import Title
from errors.parser.shared.parse_title_error import ParseTitleError

from ir.memorandums.subtitle import Subtitle
from errors.parser.memorandums.parse_subtitle_error import ParseSubtitleError

from ir.problem_sets.school import School
from errors.parser.problem_sets.parse_school_error import ParseSchoolError

from ir.problem_sets.course import Course
from errors.parser.problem_sets.parse_course_error import ParseCourseError

from ir.problem_sets.due_date import DueDate
from errors.parser.problem_sets.parse_due_date_error import ParseDueDateError

from ir.problem_sets.label import Label
from errors.parser.problem_sets.parse_label_error import ParseLabelError

from ir.problem_sets.statement import Statement
from errors.parser.problem_sets.parse_statement_error import ParseStatementError

from ir.problem_sets.solution import Solution
from errors.parser.problem_sets.parse_solution_error import ParseSolutionError

from ir.problem_sets.problem import Problem
from errors.parser.problem_sets.parse_problem_error import ParseProblemError

from ir.memorandums.content import Content
from errors.parser.memorandums.parse_content_error import ParseContentError

from ir.memorandums.section import Section
from errors.parser.memorandums.parse_section_error import ParseSectionError

from ir.problem_sets.problem_set import ProblemSet
from errors.parser.problem_sets.parse_problem_set_error import ParseProblemSetError

from ir.memorandums.memorandum import Memorandum
from errors.parser.memorandums.parse_memorandum_error import ParseMemorandumError

from ir.document import Document
from errors.parser.parse_document_error import ParseDocumentError


# Terminals
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
alphas = caps + lowers
digits = "0123456789"
symbols = "[]{}()<>\'\"=|.,;\/:-$?!*_+#"
space = " "
newline = "\n"
tab = space + space + space + space
whitespace = space + newline + tab

text = ZeroOrMore(Word(alphas + digits + symbols + whitespace))

# Grammar
author = Literal("author:") + White(space) + text
collaborator = Word(alphas)
collaborators = Literal("collaborators:") + White(space) + delimitedList(collaborator)
date = Literal("date:") + White(space) + text
title = Literal("title:") + White(space) + text
subtitle = Literal("subtitle:") + White(space) + text

school = Literal("school:") + White(space) + text
course = Literal("course:") + White(space) + text
due_date = Literal("due_date:") + White(space) + text

label = Literal("label:") + White(space) + text
statement = Literal("statement:") + White(space) + Optional(White(newline) + White(tab)) + text
solution = Literal("solution:") + White(newline) + Combine(White(tab) + text)
problem = Literal("problem:") + White(newline) + Optional(White(tab) + label + White("\n")) + statement + newline + solution

content = Literal("content:") + newline + text
section = Literal("section:") + newline + title + newline + content

problem_set = Literal("problem_set:") + newline + author + newline + ZeroOrMore(collaborators) + newline \
                                      + Optional(due_date + newline) + Optional(title + newline) \
                                      + Optional(course + newline) + Optional(school + newline) \
                                      + OneOrMore(problem + newline)

memorandum = Literal("memorandum:") + newline + author + newline + ZeroOrMore(collaborators) + newline \
                                    + Optional(date + newline) + title + Optional(subtitle + newline) \
                                    + OneOrMore(section + newline)

document = memorandum | problem_set


class EasyTeXParser(object):
    @staticmethod
    def parse_text(input_string):
        try:
            parsed_text = text.parseString(input_string)
        except ParseException as pex:
            raise ParseTextError("Error parsing text: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_text[0]:
            return parsed_text[0]
        else:
            raise ParseTextError("Error parsing text: '{}'".format(input_string))

    @staticmethod
    def parse_author(input_string):
        try:
            parsed_author = author.parseString(input_string)
        except ParseException as pex:
            raise ParseAuthorError("Error parsing author: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_author[2]:
            return Author(parsed_author[2])
        else:
            raise ParseAuthorError("Error parsing author: '{}'".format(input_string))

    @staticmethod
    def parse_collaborators(input_string):
        try:
            parsed_collaborators = collaborators.parseString(input_string)
        except ParseException as pex:
            raise ParseCollaboratorsError("Error parsing collaborators: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_collaborators[2]:
            return [Collaborator(name) for name in parsed_collaborators[2:]]
        else:
            raise ParseCollaboratorsError("Error parsing collaborators: '{}'".format(input_string))

    @staticmethod
    def parse_date(input_string):
        try:
            parsed_date = date.parseString(input_string)
        except ParseException as pex:
            raise ParseDateError("Error parsing date: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_date[2]:
            return Date(parsed_date[2])
        else:
            raise ParseDateError("Error parsing date: '{}'".format(date))

    @staticmethod
    def parse_title(input_string):
        try:
            parsed_title = title.parseString(input_string)
        except ParseException as pex:
            raise ParseTitleError("Error parsing title: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_title[2]:
            return Title(parsed_title[2])
        else:
            raise ParseTitleError("Error parsing title: '{}'".format(input_string))

    @staticmethod
    def parse_subtitle(input_string):
        try:
            parsed_subtitle = subtitle.parseString(input_string)
        except ParseException as pex:
            raise ParseSubtitleError("Error parsing subtitle: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_subtitle[2]:
            return Subtitle(parsed_subtitle[2])
        else:
            raise ParseSubtitleError("Error parsing subtitle: '{}'".format(input_string))

    @staticmethod
    def parse_school(input_string):
        try:
            parsed_school = school.parseString(input_string)
        except ParseException as pex:
            raise ParseSchoolError("Error parsing school: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_school[2]:
            return School(parsed_school[2])
        else:
            raise ParseSchoolError("Error parsing school: '{}'".format(input_string))

    @staticmethod
    def parse_course(input_string):
        try:
            parsed_course = course.parseString(input_string)
        except ParseException as pex:
            raise ParseCourseError("Error parsing course: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_course[2]:
            return Course(parsed_course[2])
        else:
            raise ParseCourseError("Error parsing course: '{}'".format(input_string))

    @staticmethod
    def parse_due_date(input_string):
        try:
            parsed_due_date = due_date.parseString(input_string)
        except ParseException as pex:
            raise ParseDueDateError("Error parsing due date: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_due_date[2]:
            return DueDate(parsed_due_date[2])
        else:
            raise ParseDueDateError("Error parsing due date: '{}'".format(input_string))

    @staticmethod
    def parse_label(input_string):
        try:
            parsed_label = label.parseString(input_string)
        except ParseException as pex:
            raise ParseLabelError("Error parsing label: '{}'. Exception raised: '{}'".format(input_string, pex))
        if parsed_label[2]:
            return Label(parsed_label[2])
        else:
            raise ParseLabelError("Error parsing label: '{}'".format(input_string))

    @staticmethod
    def parse_statement(input_string):
        try:
            parsed_statement = statement.parseString(input_string)
        except ParseException as pex:
            raise ParseStatementError("Error parsing statement: '{}'. Exception raised: '{}'". format(input_string, pex))

        if parsed_statement[2]:
            return Statement(parsed_statement[2])
        else:
            raise ParseStatementError("Error parsing statement: '{}'".format(input_string))

    @staticmethod
    def parse_solution(input_string):
        try:
            parsed_solution = solution.parseString(input_string)
        except ParseException as pex:
            raise ParseSolutionError("Error parsing solution: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_solution[2]:
            return Solution(parsed_solution[2])
        else:
            raise ParseSolutionError("Error parsing solution: '{}'".format(input_string))

    # TODO
    @staticmethod
    def parse_problem(input_string):
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
