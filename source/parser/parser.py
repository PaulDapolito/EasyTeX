__author__ = 'Paul Dapolito'

from pyparsing import *

from errors.parser.parse_document_error import ParseDocumentError
from errors.parser.parse_text_error import ParseTextError
from ir.shared.author import Author
from ir.shared.collaborator import Collaborator
from ir.memorandums.date import Date
from ir.shared.title import Title
from ir.memorandums.subtitle import Subtitle
from ir.problem_sets.school import School
from ir.problem_sets.course import Course
from ir.problem_sets.due_date import DueDate
from ir.problem_sets.label import Label
from ir.problem_sets.statement import Statement
from ir.problem_sets.solution import Solution
from ir.problem_sets.problem import Problem
from ir.memorandums.content import Content
from ir.memorandums.section import Section
from ir.problem_sets.problem_set import ProblemSet
from ir.memorandums.memorandum import Memorandum

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

## Date [Optional]
optional_date = Optional(Suppress(Literal("date:") + White(space)) + restOfLine + Suppress(LineEnd()), default='')

## Title
title = Suppress(Literal("title:") + White(space)) + restOfLine + Suppress(LineEnd())

## Title [Optional]
optional_title = Optional(title, default='')

## Subtitle [Optional]
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
section = Group(Suppress(Literal("section:") + LineEnd()) + title + content)

## Problem Set
problem_set_identifier = Literal("problem_set")
problem_set_ignored = Suppress(Literal(":") + LineEnd())
problem_set_contents = author + optional_collaborators + optional_due_date + optional_title + optional_course + optional_school
problem_set_problems = Group(OneOrMore(problem))
problem_set = problem_set_identifier + problem_set_ignored + problem_set_contents + problem_set_problems

## Memorandum
memorandum_header = Literal("memorandum")
memorandum_ignored = Suppress(Literal(":") + LineEnd())
memorandum_contents = author + optional_collaborators + optional_date + title + optional_subtitle + Group(OneOrMore(section))
memorandum = memorandum_header + memorandum_ignored + memorandum_contents

## Document
document = problem_set | memorandum


# Parser Implementation
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

    @staticmethod
    def parse_memorandum(parsed_block):
        author = Author(parsed_block[0])

        # Check for collaborators
        if parsed_block[1]:
            collaborators = [Collaborator(collab) for collab in parsed_block[1]]
        else:
            collaborators = None

        # Check for date
        if parsed_block[2]:
            date = Date(parsed_block[2])
        else:
            date = None

        title = Title(parsed_block[3])

        # Check for subtitle
        if parsed_block[4]:
            subtitle = Subtitle(parsed_block[4])
        else:
            subtitle = None

        # Accumulate sections
        sections = list()
        for section in parsed_block[5]:
            section_title = Title(section[0])

            # Strip leftmost whitespace from every line of content
            content_stripped = [line.lstrip() for line in section[1]]
            content_txt = newline.join(content_stripped)
            content = Content(content_txt)

            sections.append(Section(section_title, content))

        # Create and return memorandum
        memorandum = Memorandum(author, collaborators, date, title, subtitle, sections)
        return memorandum

    def parse_document(self, input_string):
        try:
            indented_block = document.parseString(input_string)
        except ParseException as pex:
            raise ParseDocumentError("Error parsing document. Exception raised: '{}'".format(pex))

        if indented_block is None or indented_block[1:] is None:
            raise ParseDocumentError("Error parsing document: found no indented block!".format(input_string))
        elif indented_block[0] == "memorandum":
            return self.parse_memorandum(indented_block[1:])
        elif indented_block[0] == "problem_set":
            return self.parse_problem_set(indented_block[1:])
        else:
            raise ParseDocumentError("Error parsing document: found no indented block!".format(input_string))

