__author__ = 'Paul Dapolito'

import unittest

from parser.parser import EasyTeXParser

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

from ir.document import Document


class EasyTeXParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = EasyTeXParser()

    def validate_test(self):
        self.assertEqual(1, 1)

    # Text Tests
    def parse_basic_text_test(self):
        input_string = "Basic"
        parsed_string = self.parser.parse_text(input_string)

        self.assertEqual(input_string, parsed_string)

    def parse_text_with_spaces_test(self):
        input_string = "One Space"
        parsed_string = self.parser.parse_text(input_string)

        self.assertEqual(input_string, parsed_string)

    def parse_text_with_symbols_test(self):
        input_string = "\\textbf{Hello World}"
        parsed_string = self.parser.parse_text(input_string)

        self.assertEqual(input_string, parsed_string)

    # Author Tests
    def parse_basic_author_test(self):
        input_string = open("test_text_files/shared/basic_author.txt").read()
        parsed_author = self.parser.parse_author(input_string)
        author_text = open("test_text_files/shared/basic_author.raw").read()

        self.assertEqual(Author(author_text), parsed_author)

    def parse_advanced_author_test(self):
        input_string = open("test_text_files/shared/advanced_author.txt").read()
        parsed_author = self.parser.parse_author(input_string)
        author_text = open("test_text_files/shared/advanced_author.raw").read()

        self.assertEqual(Author(author_text), parsed_author)

    # Collaborators Tests
    def parse_single_collaborator_test(self):
        input_string = open("test_text_files/shared/single_collaborator.txt").read()
        parsed_collaborators = self.parser.parse_collaborators(input_string)
        collaborator_text = open("test_text_files/shared/single_collaborator.raw").read()

        self.assertEqual([Collaborator(collaborator_text)], parsed_collaborators)

    def parse_multiple_collaborators_test(self):
        input_string = open("test_text_files/shared/multiple_collaborators.txt").read()
        parsed_collaborators = self.parser.parse_collaborators(input_string)
        collaborators_list = open("test_text_files/shared/multiple_collaborators.raw").read().split(", ")

        self.assertEqual([Collaborator(collab) for collab in collaborators_list], parsed_collaborators)

    # Date Tests
    def parse_basic_date_test(self):
        input_string = open("test_text_files/memorandums/basic_date.txt").read()
        parsed_date = self.parser.parse_date(input_string)
        date_text = open("test_text_files/memorandums/basic_date.raw").read()

        self.assertEqual(Date(date_text), parsed_date)

    def parse_date_with_symbols_test(self):
        input_string = open("test_text_files/memorandums/date_with_symbols.txt").read()
        parsed_date = self.parser.parse_date(input_string)
        date_text = open("test_text_files/memorandums/date_with_symbols.raw").read()

        self.assertEqual(Date(date_text), parsed_date)

    # Title Tests
    def parse_basic_title_test(self):
        input_string = open("test_text_files/shared/basic_title.txt").read()
        parsed_title = self.parser.parse_title(input_string)
        title_text = open("test_text_files/shared/basic_title.raw").read()

        self.assertEqual(Title(title_text), parsed_title)

    def parse_advanced_title_test(self):
        input_string = open("test_text_files/shared/advanced_title.txt").read()
        parsed_title = self.parser.parse_title(input_string)
        title_text = open("test_text_files/shared/advanced_title.raw").read()

        self.assertEqual(Title(title_text), parsed_title)

    # Subtitle Tests
    def parse_basic_subtitle_test(self):
        input_string = open("test_text_files/memorandums/basic_subtitle.txt").read()
        parsed_subtitle = self.parser.parse_subtitle(input_string)
        subtitle_text = open("test_text_files/memorandums/basic_subtitle.raw").read()

        self.assertEqual(Subtitle(subtitle_text), parsed_subtitle)

    def parse_advanced_subtitle_test(self):
        input_string = open("test_text_files/memorandums/advanced_subtitle.txt").read()
        parsed_subtitle = self.parser.parse_subtitle(input_string)
        subtitle_text = open("test_text_files/memorandums/advanced_subtitle.raw").read()

        self.assertEqual(Subtitle(subtitle_text), parsed_subtitle)

    # School Tests
    def parse_basic_school_test(self):
        input_string = open("test_text_files/problem_sets/basic_school.txt").read()
        parsed_school = self.parser.parse_school(input_string)
        school_text = open("test_text_files/problem_sets/basic_school.raw").read()

        self.assertEqual(School(school_text), parsed_school)

    def parse_school_with_symbols_test(self):
        input_string = open("test_text_files/problem_sets/school_with_symbols.txt").read()
        parsed_school = self.parser.parse_school(input_string)
        school_text = open("test_text_files/problem_sets/school_with_symbols.raw").read()

        self.assertEqual(School(school_text), parsed_school)

    # Course Tests
    def parse_basic_course_test(self):
        input_string = open("test_text_files/problem_sets/basic_course.txt").read()
        parsed_course = self.parser.parse_course(input_string)
        course_text = open("test_text_files/problem_sets/basic_course.raw").read()

        self.assertEqual(Course(course_text), parsed_course)

    def parse_course_with_symbols_test(self):
        input_string = open("test_text_files/problem_sets/course_with_symbols.txt").read()
        parsed_course = self.parser.parse_course(input_string)
        course_text = open("test_text_files/problem_sets/course_with_symbols.raw").read()

        self.assertEqual(Course(course_text), parsed_course)

    # Due Date Tests
    def parse_basic_due_date_test(self):
        input_string = open("test_text_files/problem_sets/basic_due_date.txt").read()
        parsed_due_date = self.parser.parse_due_date(input_string)
        due_date_text = open("test_text_files/problem_sets/basic_due_date.raw").read()

        self.assertEqual(DueDate(due_date_text), parsed_due_date)

    def parse_due_date_with_symbols_test(self):
        input_string = open("test_text_files/problem_sets/due_date_with_symbols.txt").read()
        parsed_due_date = self.parser.parse_due_date(input_string)
        due_date_text = open("test_text_files/problem_sets/due_date_with_symbols.raw").read()

        self.assertEqual(DueDate(due_date_text), parsed_due_date)

    # Label Tests
    def parse_basic_label_test(self):
        input_string = open("test_text_files/problem_sets/basic_label.txt").read()
        parsed_label = self.parser.parse_label(input_string)
        label_text = open("test_text_files/problem_sets/basic_label.raw").read()

        self.assertEqual(Label(label_text), parsed_label)

    def parse_label_with_symbols_test(self):
        input_string = open("test_text_files/problem_sets/label_with_symbols.txt").read()
        parsed_label = self.parser.parse_label(input_string)
        label_text = open("test_text_files/problem_sets/label_with_symbols.raw").read()

        self.assertEqual(Label(label_text), parsed_label)

    # Statement Tests TODO: Add more
    def parse_basic_statement_test(self):  # Test a space-separated statement
        input_string = open("test_text_files/problem_sets/basic_statement.txt").read()
        parsed_statement = self.parser.parse_statement(input_string)
        statement_text = open("test_text_files/problem_sets/basic_statement.raw").read()

        self.assertEqual(Statement(statement_text), parsed_statement)

    def parse_advanced_statement_test(self):  # Test a return-separated statement
        input_string = open("test_text_files/problem_sets/advanced_statement.txt").read()
        parsed_statement = self.parser.parse_statement(input_string)
        statement_text = open("test_text_files/problem_sets/advanced_statement.raw").read()

        self.assertEqual(Statement(statement_text), parsed_statement)

    # Solution Tests TODO: Add more
    def parse_basic_solution_test(self):
        input_string = open("test_text_files/problem_sets/basic_solution.txt").read()
        parsed_solution = self.parser.parse_solution(input_string)
        solution_text = open("test_text_files/problem_sets/basic_solution.raw").read()

        self.assertEqual(Solution(solution_text), parsed_solution)

    # Problem Tests TODO: Add more
    def parse_basic_problem_test(self):
        input_string = open("test_text_files/problem_sets/basic_problem.txt").read()
        parsed_problem = self.parser.parse_problem(input_string)

        label = open("test_text_files/problem_sets/basic_label.raw").read()
        statement = open("test_text_files/problem_sets/advanced_statement.raw").read()
        solution = open("test_text_files/problem_sets/basic_solution.raw").read()

        self.assertEqual(Problem(Label(label), Statement(statement), Solution(solution)), parsed_problem)

    # Content Tests
    def parse_basic_content_test(self):
        input_string = open("test_text_files/memorandums/basic_content.txt").read()
        parsed_content = self.parser.parse_content(input_string)
        content_text = open("test_text_files/memorandums/basic_content.raw").read()

        self.assertEqual(Content(content_text), parsed_content)

    def parse_advanced_content_test(self):
        input_string = open("test_text_files/memorandums/advanced_content.txt").read()
        parsed_content = self.parser.parse_content(input_string)
        content_text = open("test_text_files/memorandums/advanced_content.raw").read()

        self.assertEqual(Content(content_text), parsed_content)

    # Section Tests
    def parse_basic_section_test(self):
        input_string = open("test_text_files/memorandums/basic_section.txt").read()
        parsed_section = self.parser.parse_section(input_string)
        content_text = open("test_text_files/memorandums/basic_content.raw").read()

        self.assertEqual(Section(Title("Abstract"), Content(content_text)), parsed_section)

    def parse_advanced_section_test(self):
        input_string = open("test_text_files/memorandums/advanced_section.txt").read()
        parsed_section = self.parser.parse_section(input_string)
        content_text = open("test_text_files/memorandums/advanced_content.raw").read()

        self.assertEqual(Section(Title("Summary"), Content(content_text)), parsed_section)

    # Problem Set Tests TODO: Add tests for optionality
    def parse_basic_problem_set_test(self):  # Test a problem set with one problem and all optional fields filled
        input_string = open("test_text_files/problem_sets/basic_problem_set.txt").read()
        parsed_problem_set = self.parser.parse_problem_set(input_string)

        author = self.parser.parse_author(open("test_text_files/shared/basic_author.txt").read())
        collaborators = self.parser.parse_collaborators(open("test_text_files/shared/multiple_collaborators.txt").read())
        due_date = self.parser.parse_due_date(open("test_text_files/problem_sets/basic_due_date.txt").read())
        title = self.parser.parse_title(open("test_text_files/shared/basic_title.txt").read())
        course = self.parser.parse_course(open("test_text_files/problem_sets/basic_course.txt").read())
        school = self.parser.parse_school(open("test_text_files/problem_sets/basic_school.txt").read())
        problem = self.parser.parse_problem(open("test_text_files/problem_sets/basic_problem.txt").read())

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem]),
            parsed_problem_set)

    def parse_advanced_problem_set_test(self):  # Test a problem with multiple problems and all optional fields filled
        input_string = open("test_text_files/problem_sets/advanced_problem_set.txt").read()
        parsed_problem_set = self.parser.parse_problem_set(input_string)

        author = self.parser.parse_author(open("test_text_files/shared/basic_author.txt").read())
        collaborators = self.parser.parse_collaborators(open("test_text_files/shared/multiple_collaborators.txt").read())
        due_date = self.parser.parse_due_date(open("test_text_files/problem_sets/basic_due_date.txt").read())
        title = self.parser.parse_title(open("test_text_files/shared/advanced_title.txt").read())
        course = self.parser.parse_course(open("test_text_files/problem_sets/course_with_symbols.txt").read())
        school = self.parser.parse_school(open("test_text_files/problem_sets/school_with_symbols.txt").read())
        problem_1 = self.parser.parse_problem(open("test_text_files/problem_sets/basic_problem.txt").read())
        problem_2 = self.parser.parse_problem(open("test_text_files/problem_sets/advanced_problem.txt").read())

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set
        )

    # Memorandum Tests
    def parse_basic_memorandum_test(self):  # Test a memorandum with one section and all optional fields filled
        input_string = open("test_text_files/memorandums/basic_memorandum.txt").read()
        parsed_memorandum = self.parser.parse_memorandum(input_string)

        author = self.parser.parse_author(open("test_text_files/shared/basic_author.txt").read())
        collaborators = self.parser.parse_collaborators(open("test_text_files/shared/multiple_collaborators.txt").read())
        date = self.parser.parse_date(open("test_text_files/memorandums/date_with_symbols.txt").read())
        title = self.parser.parse_title(open("test_text_files/shared/basic_title.txt").read())
        subtitle = self.parser.parse_subtitle(open("test_text_files/memorandums/advanced_subtitle.txt").read())
        section = self.parser.parse_section(open("test_text_files/memorandums/basic_section.txt").read())

        self.assertEqual(
            Memorandum(author, collaborators, date, title, subtitle, [section]),
            parsed_memorandum
        )

    def parse_advanced_memorandum_test(self):  # Test a memorandum with multiple sections and all optional fields filled
        input_string = open("test_text_files/memorandums/advanced_memorandum.txt").read()
        parsed_memorandum = self.parser.parse_memorandum(input_string)

        author = self.parser.parse_author(open("test_text_files/shared/basic_author.txt").read())
        collaborators = self.parser.parse_collaborators(open("test_text_files/shared/multiple_collaborators.txt").read())
        date = self.parser.parse_date(open("test_text_files/memorandums/date_with_symbols.txt").read())
        title = self.parser.parse_title(open("test_text_files/shared/basic_title.txt").read())
        subtitle = self.parser.parse_subtitle(open("test_text_files/memorandums/advanced_subtitle.txt").read())
        section_1 = self.parser.parse_section(open("test_text_files/memorandums/basic_section.txt").read())
        section_2 = self.parser.parse_section(open("test_text_files/memorandums/advanced_section.txt").read())

        self.assertEqual(
            Memorandum(author, collaborators, date, title, subtitle, [section_1, section_2]),
            parsed_memorandum
        )

    # Document Tests
    def parse_basic_problem_set_document(self):
        input_string = open("test_text_files/problem_sets/advanced_problem_set.txt").read()
        parsed_document = self.parser.parse_document(input_string)

        problem_set = self.parser.parse_problem_set(open("test_text_files/problem_sets/advanced_problem_set.txt").read())

        self.assertEqual(Document(problem_set=problem_set, memorandum=None), parsed_document)

    def parse_basic_memorandum_document(self):
        input_string = open("test_text_files/memorandums/advanced_memorandum.txt").read()
        parsed_document = self.parser.parse_document(input_string)

        memorandum = self.parser.parse_memorandum(open("test_text_files/memorandums/advanced_memorandum.txt").read())

        self.assertEqual(Document(problem_set=None, memorandum=memorandum), parsed_document)
