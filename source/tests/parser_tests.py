__author__ = 'Paul Dapolito'

import unittest

from parser.parser import EasyTeXParser

from ir.problem_sets.solution import Solution
from ir.problem_sets.statement import Statement
from ir.problem_sets.label import Label
from ir.problem_sets.problem import Problem

from ir.problem_sets.due_date import DueDate
from ir.problem_sets.course import Course
from ir.problem_sets.school import School

from ir.memorandums.subtitle import Subtitle
from ir.shared.title import Title
from ir.memorandums.date import Date
from ir.shared.collaborator import Collaborator
from ir.shared.author import Author

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

    # Solution Tests
    def parse_basic_solution_test(self):
        input_string = open("test_text_files/problem_sets/basic_solution.txt").read()
        parsed_solution = self.parser.parse_solution(input_string)
        solution_text = open("test_text_files/problem_sets/basic_text_solution.txt").read()

        self.assertEqual(Solution(solution_text), parsed_solution)

    def parse_advanced_solution_test(self):
        input_string = open("test_text_files/problem_sets/advanced_solution.txt").read()
        parsed_solution = self.parser.parse_solution(input_string)
        solution_text = open("test_text_files/problem_sets/advanced_text_solution.txt").read()

        self.assertEqual(Solution(solution_text), parsed_solution)

    # Statement Tests
    def parse_basic_statement_test(self):
        statement = "What is the rate of change $f'$ of a function $f$ at the point $a$?"
        input_string = "statement: " + statement
        parsed_statement = self.parser.parse_statement(input_string)

        self.assertEqual(Statement(statement), parsed_statement)

    def parse_advanced_statement_test(self):
        statement = \
            "Carefully prove that if $L_1$ and $L_2$ are languages and $L_1 \subseteq L_2*$, then $L_1 * \subseteq L_2*$"
        input_string = "statement: " + statement
        parsed_statement = self.parser.parse_statement(input_string)

        self.assertEqual(Statement(statement), parsed_statement)

    # Label Tests
    def parse_basic_label_test(self):
        input_string = "label: 1"
        parsed_label = self.parser.parse_label(input_string)

        self.assertEqual(Label("1"), parsed_label)

    def parse_label_with_symbols_test(self):
        input_string = "label: 1(a)(b)"
        parsed_label = self.parser.parse_label(input_string)

        self.assertEqual(Label("1(a)(b)"), parsed_label)

    # Problem Tests
    def parse_basic_problem_test(self):
        input_string = open("test_text_files/problem_sets/basic_problem.txt").read()
        parsed_problem = self.parser.parse_problem(input_string)

        label = "1"
        statement = "What is the rate of change $f'$ of a function $f$ at the point $a$?"
        solution = open("test_text_files/problem_sets/basic_text_solution.txt").read()
        self.assertEqual(Problem(Label(label), Statement(statement), Solution(solution)), parsed_problem)

    def parse_advanced_problem_test(self):
        input_string = open("test_text_files/problem_sets/advanced_problem.txt").read()
        parsed_problem = self.parser.parse_problem(input_string)

        label = "2"
        statement = \
            "Carefully prove that if $L_1$ and $L_2$ are languages and $L_1 \subseteq L_2*$, then $L_1 * \subseteq L_2*$"
        solution = open("test_text_files/problem_sets/advanced_text_solution.txt").read()
        self.assertEqual(Problem(Label(label), Statement(statement), Solution(solution)), parsed_problem)

    # Due Date Tests
    def parse_basic_due_date_test(self):
        input_string = "due_date: September 21, 2015"
        parsed_due_date = self.parser.parse_due_date(input_string)

        self.assertEqual(DueDate("September 21, 2015"), parsed_due_date)

    def parse_due_date_with_symbols_test(self):
        input_string = "due_date: 09/21/2015"
        parsed_due_date = self.parser.parse_due_date(input_string)

        self.assertEqual(DueDate("09/21/2015"), parsed_due_date)

    # Course Tests
    def parse_basic_course_test(self):
        input_string = "course: Programming Languages"
        parsed_course = self.parser.parse_course(input_string)

        self.assertEqual(Course("Programming Languages"), parsed_course)

    def parse_course_with_symbols_test(self):
        input_string = "course: \\textbf{Domain-Specific} Languages"
        parsed_course = self.parser.parse_course(input_string)

        self.assertEqual(Course("\\textbf{Domain-Specific} Languages"), parsed_course)

    # School Tests
    def parse_basic_school_test(self):
        input_string = "school: Staten Island Academy"
        parsed_school = self.parser.parse_school(input_string)

        self.assertEqual(School("Staten Island Academy"), parsed_school)

    def parse_school_with_symbols_test(self):
        input_string = "school: Dallas Science School: \\textbf{magnet}"
        parsed_school = self.parser.parse_school(input_string)

        self.assertEqual(School("Dallas Science School: \\textbf{magnet}"), parsed_school)

    # Subtitle Tests
    def parse_basic_subtitle_test(self):
        input_string = "subtitle: Basic subtitle"
        parsed_subtitle = self.parser.parse_subtitle(input_string)

        self.assertEqual(Subtitle("Basic subtitle"), parsed_subtitle)

    def parse_advanced_subtitle_test(self):
        input_string = "subtitle: Super \underline{Advanced} Subtitle"
        parsed_subtitle = self.parser.parse_subtitle(input_string)

        self.assertEqual(Subtitle("Super \underline{Advanced} Subtitle"), parsed_subtitle)

    # Title Tests
    def parse_basic_title_test(self):
        input_string = "title: Basic title"
        parsed_title = self.parser.parse_title(input_string)

        self.assertEqual(Title("Basic title"), parsed_title)

    def parse_advanced_title_test(self):
        input_string = "title: Super \underline{Advanced} Subtitle"
        parsed_title = self.parser.parse_title(input_string)

        self.assertEqual(Title("Super \underline{Advanced} Subtitle"), parsed_title)

    # Date Tests
    def parse_basic_date_test(self):
        input_string = "date: September 21, 2015"
        parsed_date = self.parser.parse_date(input_string)

        self.assertEqual(Date("September 21, 2015"), parsed_date)

    def parse_date_with_symbols_test(self):
        input_string = "due_date: 09/21/2015"
        parsed_date = self.parser.parse_date(input_string)

        self.assertEqual(Date("09/21/2015"), parsed_date)

    # Collaborators Tests
    def parse_single_collaborator_test(self):
        input_string = "collaborators: Robert"
        parsed_collaborators = self.parser.parse_collaborators(input_string)

        self.assertEqual([Collaborator("Robert")], parsed_collaborators)

    def parse_multiple_collaborators_test(self):
        input_string = "collaborators: Robert, Angela, Daniel"
        parsed_collaborators = self.parser.parse_collaborators(input_string)

        self.assertEqual([Collaborator("Robert"), Collaborator("Angela"), Collaborator("Daniel")], parsed_collaborators)

    # Author Tests
    def parse_basic_author_test(self):
        input_string = "author: Paul"
        parsed_author = self.parser.parse_author(input_string)

        self.assertEqual(Author("Paul"), parsed_author)

    def parse_advanced_author_test(self):
        input_string = "author: Paul Dapolito IV \\textbf{THE GREAT}"
        parsed_author = self.parser.parse_author(input_string)

        self.assertEqual(Author("Paul Dapolito IV \\textbf{THE GREAT}"), parsed_author)

    # Content Tests
    def parse_basic_content_test(self):
        input_string = open("test_text_files/memorandums/basic_content.txt").read()
        parsed_content = self.parser.parse_content(input_string)
        content_text = open("test_text_files/memorandums/basic_text_content.txt").read()

        self.assertEqual(Content(content_text), parsed_content)

    def parse_advanced_content_test(self):
        input_string = open("test_text_files/memorandums/advanced_content.txt").read()
        parsed_content = self.parser.parse_content(input_string)
        content_text = open("test_text_files/memorandums/advanced_text_content.txt").read()

        self.assertEqual(Content(content_text), parsed_content)

    # Section Tests
    def parse_basic_section_test(self):
        input_string = open("test_text_files/memorandums/basic_section.txt").read()
        parsed_section = self.parser.parse_section(input_string)
        section_text = open("test_text_files/memorandums/basic_text_content.txt").read()

        self.assertEqual(Section("Abstract", section_text), parsed_section)

    def parse_advanced_section_test(self):
        input_string = open("test_text_files/memorandums/advanced_section.txt").read()
        parsed_section = self.parser.parse_section(input_string)
        section_text = open("test_text_files/memorandums/advanced_text_content.txt").read()

        self.assertEqual(Section("Summary", section_text), parsed_section)

    # Problem Set Tests
    def parse_basic_problem_set_test(self):  # Test a problem set with one problem and all optional fields filled
        input_string = open("test_text_files/problem_sets/basic_problem_set.txt").read()
        parsed_problem_set = self.parser.parse_problem_set(input_string)

        problem = self.parser.parse_problem(open("test_text_files/problem_sets/basic_problem.txt").read())
        author = "Paul Dapolito"
        collaborator_1 = "Angela"
        collaborator_2 = "Rob"
        due_date = "November 1, 2014"
        title = "Assignment 3"
        course = "CS111"
        school = "Harvey Mudd College"

        self.assertEqual(
            ProblemSet(author, [collaborator_1, collaborator_2], due_date, title, course, school, [problem]),
            parsed_problem_set)

    def parse_advanced_problem_set_test(self):  # Test a problem with multiple problems and all optional fields filled
        input_string = open("test_text_files/problem_sets/advanced_problem_set.txt").read()
        parsed_problem_set = self.parser.parse_problem_set(input_string)

        problem_1 = self.parser.parse_problem(open("test_text_files/problem_sets/basic_problem.txt").read())
        problem_2 = self.parser.parse_problem(open("test_text_files/problem_sets/advanced_problem.txt").read())
        author = "Paul Dapolito"
        collaborator_1 = "Angela"
        collaborator_2 = "Rob"
        due_date = "November 1, 2014"
        title = "Assignment 3"
        course = "CS111"
        school = "Harvey Mudd College"

        self.assertEqual(
            ProblemSet(author, [collaborator_1, collaborator_2], due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set
        )

    # Memorandum Tests
    def parse_basic_memorandum_test(self):  # Test a memorandum with one section and all optional fields filled
        input_string = open("test_text_files/memorandums/basic_memorandum.txt").read()
        parsed_memorandum = self.parser.parse_memorandum(input_string)

        section_1 = self.parser.parse_section(open("test_text_files/memorandums/basic_section.txt").read())
        author = "Paul Dapolito"
        collaborator_1 = "Michael"
        collaborator_2 = "Rojesh"
        date = "October 31, 2014"
        title = "A Canonical Example of EasyTeX"
        subtitle = "Quick, easy, and syntactically charming!"

        self.assertEqual(
            Memorandum(author, [collaborator_1, collaborator_2], date, title, subtitle, [section_1]),
            parsed_memorandum
        )

    def parse_advanced_memorandum_test(self):  # Test a memorandum with multiple sections and all optional fields filled
        input_string = open("test_text_files/memorandums/advanced_memorandum.txt").read()
        parsed_memorandum = self.parser.parse_memorandum(input_string)

        section_1 = self.parser.parse_section(open("test_text_files/memorandums/basic_section.txt").read())
        section_2 = self.parser.parse_section(open("test_text_files/memorandums/advanced_section.txt").read())
        author = "Paul Dapolito"
        collaborator_1 = "Michael"
        collaborator_2 = "Rojesh"
        date = "October 31, 2014"
        title = "A Canonical Example of EasyTeX"
        subtitle = "Quick, easy, and syntactically charming!"

        self.assertEqual(
            Memorandum(author, [collaborator_1, collaborator_2], date, title, subtitle, [section_1, section_2]),
            parsed_memorandum
        )

    # Document Tests
    def parse_basic_problem_set_document(self):
        input_string = open("test_text_files/problem_sets/advanced_problem_set.txt").read()
        parsed_document = self.parser.parse_document(input_string)

        problem_set = self.parser.parse_problem(open("test_text_files/problem_sets/advanced_problem_set.txt").read())

        self.assertEqual(Document(problem_set=problem_set, memorandum=None), parsed_document)

    def parse_basic_memorandum_document(self):
        input_string = open("test_text_files/memorandums/advanced_memorandum.txt").read()
        parsed_document = self.parser.parse_document(input_string)

        memorandum = self.parser.parse_memorandum(open("test_text_files/memorandums/advanced_memorandum.txt").read())

        self.assertEqual(Document(problem_set=None, memorandum=memorandum), parsed_document)
