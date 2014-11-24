__author__ = 'Paul Dapolito'

from pyparsing import *

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
symbols = "[]{}()<>\'\"=|.,;\/:-$?!*_+#^`"

space = " "
newline = "\n"
tab = space + space + space + space
whitespace = space + newline + tab

terminals = alphas + digits + symbols + whitespace
text = ZeroOrMore(Word(terminals)).leaveWhitespace()

# Grammar
## Author
author = Suppress(Literal("author:") + White(space)) + restOfLine

## Collaborators [Optional]
collaborator = Word(alphas)
collaborators_group = Group(delimitedList(collaborator))
collaborators_ignored = Suppress(Literal("collaborators:") + White(space))
optional_collaborators = Optional(collaborators_ignored + collaborators_group, default=[])

## Date
date = Suppress(Literal("date:") + White(space)) + restOfLine

## Title
title = Suppress(Literal("title:") + White(space)) + restOfLine

## Title [Optional]
optional_title = Optional(title, default='')

## Optional Subtitle
optional_subtitle = Optional(Suppress(Literal("subtitle:") + White(space)) + restOfLine, default='')

## School [Optional]
optional_school = Optional(Suppress(Literal("school:") + White(space)) + restOfLine, default='')

## Course [Optional]
optional_course = Optional(Suppress(Literal("course:") + White(space)) + restOfLine, default='')

## Due Date [Optional]
optional_due_date = Optional(Suppress(Literal("due_date:") + White(space)) + restOfLine, default='')

## Label [Optional]
optional_label = Optional(Suppress(Literal("label:") + White(space)) + restOfLine + Suppress(LineEnd()), default='')

## Statement
statement_ignored = Suppress(Literal("statement:") + White(newline))
statement_lines = Group(OneOrMore(Regex(ur'\s\s\s\s\s\s\s\s\s\s\s\s(.+)').leaveWhitespace() + Suppress(White(newline))))
statement = statement_ignored + statement_lines

## Solution
solution_ignored = Suppress(Literal("solution:") + White(newline))
solution_lines = Group(OneOrMore(Regex(ur'\s\s\s\s\s\s\s\s\s\s\s\s(.+)').leaveWhitespace() + Suppress(White(newline))))
solution = solution_ignored + solution_lines

## Problem
problem_ignored = Suppress(Literal("problem:") + LineEnd())
problem = problem_ignored + Group(optional_label + statement + solution)

## Content
content_lines = Group(OneOrMore(Regex(ur'\s\s\s\s\s\s\s\s\s\s\s\s(.+)').leaveWhitespace() + Suppress(White(newline))))
content = Suppress(Literal("content:") + White(newline)) + content_lines

## Section
section = Group(Suppress(White(tab) + Literal("section:") + LineEnd()) + title + content)

## Problem Set
problem_set_identifier = Literal("problem_set")
problem_set_ignored = Suppress(Literal(":") + LineEnd())
problem_set_contents = author + optional_collaborators + optional_due_date + optional_title + optional_course + optional_school
problem_set_problems = Group(OneOrMore(problem))
problem_set = problem_set_identifier + problem_set_ignored + problem_set_contents + problem_set_problems

## Memorandum
memorandum_header = Literal("memorandum")
memorandum_ignored = Suppress(Literal(":") + LineEnd())
memorandum_contents = author + optional_collaborators + date + title + optional_subtitle + Group(OneOrMore(section))
memorandum = memorandum_header + memorandum_ignored + memorandum_contents

## Document
document = problem_set


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

        if parsed_author[0]:
            return Author(parsed_author[0])
        else:
            raise ParseAuthorError("Error parsing author: '{}'".format(input_string))

    @staticmethod
    def parse_collaborators(input_string):
        try:
            parsed_collaborators = optional_collaborators.parseString(input_string)
        except ParseException as pex:
            raise ParseCollaboratorsError("Error parsing collaborators: '{}'. Exception raised: '{}'".format(input_string, pex))

        print parsed_collaborators

        if parsed_collaborators[1:]:
            return [Collaborator(name) for name in parsed_collaborators[1:]]
        else:
            raise ParseCollaboratorsError("Error parsing collaborators: '{}'".format(input_string))

    @staticmethod
    def parse_date(input_string):
        try:
            parsed_date = date.parseString(input_string)
        except ParseException as pex:
            raise ParseDateError("Error parsing date: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_date[0]:
            return Date(parsed_date[0])
        else:
            raise ParseDateError("Error parsing date: '{}'".format(date))

    @staticmethod
    def parse_title(input_string):
        try:
            parsed_title = title.parseString(input_string)
        except ParseException as pex:
            raise ParseTitleError("Error parsing title: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_title[0]:
            return Title(parsed_title[0])
        else:
            raise ParseTitleError("Error parsing title: '{}'".format(input_string))

    @staticmethod
    def parse_subtitle(input_string):
        try:
            parsed_subtitle = optional_subtitle.parseString(input_string)
        except ParseException as pex:
            raise ParseSubtitleError("Error parsing subtitle: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_subtitle[0]:
            return Subtitle(parsed_subtitle[0])
        else:
            raise ParseSubtitleError("Error parsing subtitle: '{}'".format(input_string))

    @staticmethod
    def parse_school(input_string):
        try:
            parsed_school = optional_school.parseString(input_string)
        except ParseException as pex:
            raise ParseSchoolError("Error parsing school: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_school[0]:
            return School(parsed_school[0])
        else:
            raise ParseSchoolError("Error parsing school: '{}'".format(input_string))

    @staticmethod
    def parse_course(input_string):
        try:
            parsed_course = optional_course.parseString(input_string)
        except ParseException as pex:
            raise ParseCourseError("Error parsing course: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_course[0]:
            return Course(parsed_course[0])
        else:
            raise ParseCourseError("Error parsing course: '{}'".format(input_string))

    @staticmethod
    def parse_due_date(input_string):
        try:
            parsed_due_date = optional_due_date.parseString(input_string)
        except ParseException as pex:
            raise ParseDueDateError("Error parsing due date: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_due_date[0]:
            return DueDate(parsed_due_date[0])
        else:
            raise ParseDueDateError("Error parsing due date: '{}'".format(input_string))

    @staticmethod
    def parse_label(input_string):
        try:
            parsed_label = optional_label.parseString(input_string)
        except ParseException as pex:
            raise ParseLabelError("Error parsing label: '{}'. Exception raised: '{}'".format(input_string, pex))

        if parsed_label[0]:
            return Label(parsed_label[0])
        else:
            raise ParseLabelError("Error parsing label: '{}'".format(input_string))

    @staticmethod
    def parse_statement(input_string):
        try:
            indented_block = statement.parseString(input_string)  # Returns list of lists
            unjoined_statement = indented_block[0]
        except ParseException as pex:
            raise ParseStatementError("Error parsing statement: '{}'. Exception raised: '{}'". format(input_string, pex))

        if unjoined_statement:
            joined_statement = newline.join(unjoined_statement)
            parsed_statement = joined_statement
            return Statement(parsed_statement)
        else:
            raise ParseStatementError("Error parsing statement: '{}'".format(input_string))

    @staticmethod
    def parse_solution(input_string):
        try:
            indented_block = solution.parseString(input_string)  # Returns list of lists
            unjoined_solution = indented_block[0]
        except ParseException as pex:
            raise ParseSolutionError("Error parsing solution: '{}'. Exception raised: '{}'".format(input_string, pex))

        if unjoined_solution:
            joined_solution = newline.join(unjoined_solution)
            parsed_solution = joined_solution + "\n"
            return Solution(parsed_solution)
        else:
            raise ParseSolutionError("Error parsing solution: '{}'".format(input_string))

    @staticmethod
    def parse_problem(input_string):
        try:
            indented_block = problem.parseString(input_string)
        except ParseException as pex:
            raise ParseProblemError("Error parsing problem: '{}'. Exception raised: '{}'".format(input_string, pex))

        # TODO: Enforce label as optional
        if indented_block[0] and indented_block[1] and indented_block[2]:
            label = "".join(indented_block[0])
            statement = newline.join(indented_block[1])
            solution = newline.join(indented_block[2]) + "\n"  # TODO: Investigate this
            return Problem(Label(label), Statement(statement), Solution(solution))
        else:
            raise ParseProblemError("Error parsing problem: '{}'".format(input_string))

    @staticmethod
    def parse_content(input_string):
        try:
            indented_block = content.parseString(input_string)
            unjoined_content = indented_block[0]
        except ParseException as pex:
            raise ParseContentError("Error parsing content: '{}'. Exception raised: '{}'".format(input_string, pex))

        if unjoined_content:
            joined_content = newline.join(unjoined_content)
            parsed_content = joined_content + "\n"
            return Content(parsed_content)
        else:
            raise ParseContentError("Error parsing content: '{}'".format(input_string))


    @staticmethod
    def parse_section(input_string):
        try:
            indented_block = section.parseString(input_string)
        except ParseException as pex:
            raise ParseSectionError("Error parsing section: '{}'. Exception raised: '{}'".format(input_string, pex))

        if indented_block[0] and indented_block[1]:
            title = "".join(indented_block[0])
            content = newline.join(indented_block[1]) + "\n"  # TODO: Investigate this
            return Section(Title(title), Content(content))
        else:
            raise ParseSectionError("Error parsing section: '{}'".format(input_string))

    # TODO: Incorporate optionality
    @staticmethod
    def parse_problem_set(parsed_block):
        author = Author(parsed_block[0])

        # Check for collaborators
        if parsed_block[1]:
            collaborators = [Collaborator(collab) for collab in parsed_block[1]]
        else:
            collaborators = None

        # Check for due date
        if parsed_block[2] is not "":
            due_date = DueDate(parsed_block[2])
        else:
            due_date = None

        # Check for title
        if parsed_block[3] is not "":
            title = Title(parsed_block[3])
        else:
            title = None

        # Check for course
        if parsed_block[4] is not "":
            course = Course(parsed_block[4])
        else:
            course = None

        # Check for school
        if parsed_block[5] is not "":
            school = School(parsed_block[5])
        else:
            school = None

        # Accumulate problems
        problems = list()
        for problem in parsed_block[6]:
            # Check for label
            if problem[0] is not "":
                label = Label(problem[0])
            else:
                label = None

            # Strip leftmost whitespace from every line of statement and solution
            statement_stripped = [line.lstrip() for line in problem[1]]
            statement_txt = newline.join(statement_stripped)
            statement = Statement(statement_txt)

            solution_stripped = [line.lstrip() for line in problem[2]]
            solution_txt = newline.join(solution_stripped) + "\n"
            solution = Solution(solution_txt)

            problems.append(Problem(label, statement, solution))

        # Create and return problem set
        problem_set = ProblemSet(author, collaborators, due_date, title, course, school, problems)
        return problem_set

    # TODO: Incorporate optionality
    @staticmethod
    def parse_memorandum(input_string):
        try:
            indented_block = memorandum.parseString(input_string)
        except ParseException as pex:
            raise ParseMemorandumError("Error parsing memorandum: '{}'. Exception raised: '{}'".format(input_string, pex))

        if indented_block:
            author = Author(indented_block[1])
            collaborators = [Collaborator(name) for name in indented_block[3]]
            date = Date(indented_block[4])
            title = Title(indented_block[5])
            subtitle = Subtitle(indented_block[6])

            sections = list()
            for section in indented_block[7]:
                section_title = Title("".join(section[0]))
                content = Content(newline.join(section[1]) + "\n")
                sections.append(Section(section_title, content))

            return Memorandum(author, collaborators, date, title, subtitle, sections)
        else:
            raise ParseMemorandumError("Error parsing memorandum: '{}'".format(input_string))

    def parse_document(self, input_string):
        try:
            indented_block = document.parseString(input_string)
        except ParseException as pex:
            raise ParseDocumentError("Error parsing document. Exception raised: '{}'".format(pex))

        if indented_block is None or indented_block[1:] is None:
            raise ParseDocumentError("Error parsing document: found no indented block!".format(input_string))
        elif indented_block[0] == "memorandum":
            return self.parse_memorandum(input_string)
        elif indented_block[0] == "problem_set":
            return self.parse_problem_set(indented_block[1:])
        else:
            raise ParseDocumentError("Error parsing document: found no indented block!".format(input_string))
