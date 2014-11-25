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

    # Problem Set Tests
    ## Test a problem set with one problem and all optional fields filled
    def parse_full_problem_set_1_test(self):
        input_string = open("test_text_files/problem_sets/full_problem_set_1/full_problem_set_1.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/full_problem_set_1/author.txt").read())

        collaborators_txt = open("test_text_files/problem_sets/full_problem_set_1/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open("test_text_files/problem_sets/full_problem_set_1/due_date.txt").read())

        title = Title(open("test_text_files/problem_sets/full_problem_set_1/title.txt").read())
        course = Course(open("test_text_files/problem_sets/full_problem_set_1/course.txt").read())
        school = School(open("test_text_files/problem_sets/full_problem_set_1/school.txt").read())

        problem_1_label_txt = open("test_text_files/problem_sets/full_problem_set_1/problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open("test_text_files/problem_sets/full_problem_set_1/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/full_problem_set_1/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem]),
            parsed_problem_set)

    ## Test a problem set with two problems and all optional fields filled
    def parse_full_problem_set_2_test(self):
        input_string = open("test_text_files/problem_sets/full_problem_set_2/full_problem_set_2.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/full_problem_set_2/author.txt").read())

        collaborators_txt = open("test_text_files/problem_sets/full_problem_set_2/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open("test_text_files/problem_sets/full_problem_set_2/due_date.txt").read())

        title = Title(open("test_text_files/problem_sets/full_problem_set_2/title.txt").read())
        course = Course(open("test_text_files/problem_sets/full_problem_set_2/course.txt").read())
        school = School(open("test_text_files/problem_sets/full_problem_set_2/school.txt").read())

        problem_1_label_txt = open("test_text_files/problem_sets/full_problem_set_2/problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open("test_text_files/problem_sets/full_problem_set_2/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/full_problem_set_2/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open("test_text_files/problem_sets/full_problem_set_2/problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open("test_text_files/problem_sets/full_problem_set_2/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/full_problem_set_2/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems that are missing labels and all other optional fields filled
    def parse_full_problem_set_3_test(self):
        input_string = open("test_text_files/problem_sets/full_problem_set_3/full_problem_set_3.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/full_problem_set_3/author.txt").read())

        collaborators_txt = open("test_text_files/problem_sets/full_problem_set_3/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open("test_text_files/problem_sets/full_problem_set_3/due_date.txt").read())

        title = Title(open("test_text_files/problem_sets/full_problem_set_3/title.txt").read())
        course = Course(open("test_text_files/problem_sets/full_problem_set_3/course.txt").read())
        school = School(open("test_text_files/problem_sets/full_problem_set_3/school.txt").read())

        problem_1_label = None

        problem_1_statement_txt = open("test_text_files/problem_sets/full_problem_set_3/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/full_problem_set_3/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label = None

        problem_2_statement_txt = open("test_text_files/problem_sets/full_problem_set_3/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/full_problem_set_3/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and all optional fields filled in an alternate order
    def parse_full_problem_set_4_test(self):
        input_string = open("test_text_files/problem_sets/full_problem_set_4/full_problem_set_4.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/full_problem_set_4/author.txt").read())

        collaborators_txt = open("test_text_files/problem_sets/full_problem_set_4/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open("test_text_files/problem_sets/full_problem_set_4/due_date.txt").read())

        title = Title(open("test_text_files/problem_sets/full_problem_set_4/title.txt").read())
        course = Course(open("test_text_files/problem_sets/full_problem_set_4/course.txt").read())
        school = School(open("test_text_files/problem_sets/full_problem_set_4/school.txt").read())

        problem_1_label_txt = open("test_text_files/problem_sets/full_problem_set_4/problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open("test_text_files/problem_sets/full_problem_set_4/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/full_problem_set_4/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open("test_text_files/problem_sets/full_problem_set_4/problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open("test_text_files/problem_sets/full_problem_set_4/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/full_problem_set_4/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)


    ## Test a problem set with two problems and no collaborators
    def parse_partial_problem_set_1_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_1/partial_problem_set_1.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/partial_problem_set_1/author.txt").read())

        collaborators = None

        due_date = DueDate(open("test_text_files/problem_sets/partial_problem_set_1/due_date.txt").read())

        title = Title(open("test_text_files/problem_sets/partial_problem_set_1/title.txt").read())
        course = Course(open("test_text_files/problem_sets/partial_problem_set_1/course.txt").read())
        school = School(open("test_text_files/problem_sets/partial_problem_set_1/school.txt").read())

        problem_1_label_txt = open("test_text_files/problem_sets/partial_problem_set_1/problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open("test_text_files/problem_sets/partial_problem_set_1/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/partial_problem_set_1/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open("test_text_files/problem_sets/partial_problem_set_1/problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open("test_text_files/problem_sets/partial_problem_set_1/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/partial_problem_set_1/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no due date
    def parse_partial_problem_set_2_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_2/partial_problem_set_2.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/partial_problem_set_2/author.txt").read())

        collaborators_txt = open("test_text_files/problem_sets/partial_problem_set_2/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = None

        title = Title(open("test_text_files/problem_sets/partial_problem_set_2/title.txt").read())
        course = Course(open("test_text_files/problem_sets/partial_problem_set_2/course.txt").read())
        school = School(open("test_text_files/problem_sets/partial_problem_set_2/school.txt").read())

        problem_1_label_txt = open("test_text_files/problem_sets/partial_problem_set_2/problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open("test_text_files/problem_sets/partial_problem_set_2/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/partial_problem_set_2/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open("test_text_files/problem_sets/partial_problem_set_2/problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open("test_text_files/problem_sets/partial_problem_set_2/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/partial_problem_set_2/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no title
    def parse_partial_problem_set_3_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_3/partial_problem_set_3.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/partial_problem_set_3/author.txt").read())

        collaborators_txt = open("test_text_files/problem_sets/partial_problem_set_3/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open("test_text_files/problem_sets/partial_problem_set_3/due_date.txt").read())

        title = None
        course = Course(open("test_text_files/problem_sets/partial_problem_set_3/course.txt").read())
        school = School(open("test_text_files/problem_sets/partial_problem_set_3/school.txt").read())

        problem_1_label_txt = open("test_text_files/problem_sets/partial_problem_set_3/problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open("test_text_files/problem_sets/partial_problem_set_3/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/partial_problem_set_3/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open("test_text_files/problem_sets/partial_problem_set_3/problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open("test_text_files/problem_sets/partial_problem_set_3/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/partial_problem_set_3/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no course
    def parse_partial_problem_set_4_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_4/partial_problem_set_4.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/partial_problem_set_4/author.txt").read())

        collaborators_txt = open("test_text_files/problem_sets/partial_problem_set_4/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open("test_text_files/problem_sets/partial_problem_set_4/due_date.txt").read())

        title = Title(open("test_text_files/problem_sets/partial_problem_set_4/title.txt").read())
        course = None
        school = School(open("test_text_files/problem_sets/partial_problem_set_4/school.txt").read())

        problem_1_label_txt = open("test_text_files/problem_sets/partial_problem_set_4/problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open("test_text_files/problem_sets/partial_problem_set_4/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/partial_problem_set_4/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open("test_text_files/problem_sets/partial_problem_set_4/problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open("test_text_files/problem_sets/partial_problem_set_4/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/partial_problem_set_4/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no school
    def parse_partial_problem_set_5_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_5/partial_problem_set_5.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/partial_problem_set_5/author.txt").read())

        collaborators_txt = open("test_text_files/problem_sets/partial_problem_set_5/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open("test_text_files/problem_sets/partial_problem_set_5/due_date.txt").read())

        title = Title(open("test_text_files/problem_sets/partial_problem_set_5/title.txt").read())
        course = Course(open("test_text_files/problem_sets/partial_problem_set_5/course.txt").read())
        school = None

        problem_1_label_txt = open("test_text_files/problem_sets/partial_problem_set_5/problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open("test_text_files/problem_sets/partial_problem_set_5/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/partial_problem_set_5/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open("test_text_files/problem_sets/partial_problem_set_5/problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open("test_text_files/problem_sets/partial_problem_set_5/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/partial_problem_set_5/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no school, course, or title
    def parse_partial_problem_set_6_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_6/partial_problem_set_6.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/partial_problem_set_6/author.txt").read())

        collaborators_txt = open("test_text_files/problem_sets/partial_problem_set_6/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        due_date = DueDate(open("test_text_files/problem_sets/partial_problem_set_6/due_date.txt").read())

        title = None
        course = None
        school = None

        problem_1_label_txt = open("test_text_files/problem_sets/partial_problem_set_6/problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open("test_text_files/problem_sets/partial_problem_set_6/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/partial_problem_set_6/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open("test_text_files/problem_sets/partial_problem_set_6/problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open("test_text_files/problem_sets/partial_problem_set_6/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/partial_problem_set_6/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no collaborators or due date
    def parse_partial_problem_set_7_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_7/partial_problem_set_7.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/partial_problem_set_7/author.txt").read())

        collaborators = None
        due_date = None

        title = Title(open("test_text_files/problem_sets/partial_problem_set_7/title.txt").read())
        course = Course(open("test_text_files/problem_sets/partial_problem_set_7/course.txt").read())
        school = School(open("test_text_files/problem_sets/partial_problem_set_7/school.txt").read())

        problem_1_label_txt = open("test_text_files/problem_sets/partial_problem_set_7/problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open("test_text_files/problem_sets/partial_problem_set_7/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/partial_problem_set_7/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open("test_text_files/problem_sets/partial_problem_set_7/problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open("test_text_files/problem_sets/partial_problem_set_7/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/partial_problem_set_7/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)

    ## Test a problem set with two problems and no optional fields filled
    def parse_partial_problem_set_8_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_8/partial_problem_set_8.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/partial_problem_set_8/author.txt").read())

        collaborators = None
        due_date = None
        title = None
        course = None
        school = None

        problem_1_label_txt = open("test_text_files/problem_sets/partial_problem_set_8/problem_1_label.txt").read()
        problem_1_label = Label(problem_1_label_txt)

        problem_1_statement_txt = open("test_text_files/problem_sets/partial_problem_set_8/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/partial_problem_set_8/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label_txt = open("test_text_files/problem_sets/partial_problem_set_8/problem_2_label.txt").read()
        problem_2_label = Label(problem_2_label_txt)

        problem_2_statement_txt = open("test_text_files/problem_sets/partial_problem_set_8/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/partial_problem_set_8/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)

   # Test a problem set with two problems and no optional fields filled

    ## Test a problem set with two problems that are missing labels and no optional fields filled
    def parse_partial_problem_set_9_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_9/partial_problem_set_9.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/problem_sets/partial_problem_set_9/author.txt").read())

        collaborators = None
        due_date = None
        title = None
        course = None
        school = None

        problem_1_label = None

        problem_1_statement_txt = open("test_text_files/problem_sets/partial_problem_set_9/problem_1_statement.txt").read()
        problem_1_statement = Statement(problem_1_statement_txt)

        problem_1_solution_txt = open("test_text_files/problem_sets/partial_problem_set_9/problem_1_solution.txt").read()
        problem_1_solution = Solution(problem_1_solution_txt)

        problem_1 = Problem(problem_1_label, problem_1_statement, problem_1_solution)

        problem_2_label = None

        problem_2_statement_txt = open("test_text_files/problem_sets/partial_problem_set_9/problem_2_statement.txt").read()
        problem_2_statement = Statement(problem_2_statement_txt)

        problem_2_solution_txt = open("test_text_files/problem_sets/partial_problem_set_9/problem_2_solution.txt").read()
        problem_2_solution = Solution(problem_2_solution_txt)

        problem_2 = Problem(problem_2_label, problem_2_statement, problem_2_solution)

        self.assertEqual(
            ProblemSet(author, collaborators, due_date, title, course, school, [problem_1, problem_2]),
            parsed_problem_set)

    # Memorandum Tests
    ## Test a memorandum with one section and all optional fields filled
    def parse_full_memorandum_1_test(self):
        input_string = open("test_text_files/memorandums/full_memorandum_1/full_memorandum_1.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/memorandums/full_memorandum_1/author.txt").read())

        collaborators_txt = open("test_text_files/memorandums/full_memorandum_1/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open("test_text_files/memorandums/full_memorandum_1/date.txt").read())
        title = Title(open("test_text_files/memorandums/full_memorandum_1/title.txt").read())
        subtitle = Subtitle(open("test_text_files/memorandums/full_memorandum_1/subtitle.txt").read())

        section_1_title = Title(open("test_text_files/memorandums/full_memorandum_1/section_1_title.txt").read())
        section_1_content = Content(open("test_text_files/memorandums/full_memorandum_1/section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        self.assertEqual(
            Memorandum(author, collaborators, date, title, subtitle, [section_1]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and all optional fields filled
    def parse_full_memorandum_2_test(self):
        input_string = open("test_text_files/memorandums/full_memorandum_2/full_memorandum_2.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/memorandums/full_memorandum_2/author.txt").read())

        collaborators_txt = open("test_text_files/memorandums/full_memorandum_2/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open("test_text_files/memorandums/full_memorandum_2/date.txt").read())
        title = Title(open("test_text_files/memorandums/full_memorandum_2/title.txt").read())
        subtitle = Subtitle(open("test_text_files/memorandums/full_memorandum_2/subtitle.txt").read())

        section_1_title = Title(open("test_text_files/memorandums/full_memorandum_2/section_1_title.txt").read())
        section_1_content = Content(open("test_text_files/memorandums/full_memorandum_2/section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open("test_text_files/memorandums/full_memorandum_2/section_2_title.txt").read())
        section_2_content = Content(open("test_text_files/memorandums/full_memorandum_2/section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author, collaborators, date, title, subtitle, [section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and all optional fields filled in an alternate order
    def parse_full_memorandum_3_test(self):
        input_string = open("test_text_files/memorandums/full_memorandum_3/full_memorandum_3.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/memorandums/full_memorandum_3/author.txt").read())

        collaborators_txt = open("test_text_files/memorandums/full_memorandum_3/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open("test_text_files/memorandums/full_memorandum_3/date.txt").read())
        title = Title(open("test_text_files/memorandums/full_memorandum_3/title.txt").read())
        subtitle = Subtitle(open("test_text_files/memorandums/full_memorandum_3/subtitle.txt").read())

        section_1_title = Title(open("test_text_files/memorandums/full_memorandum_3/section_1_title.txt").read())
        section_1_content = Content(open("test_text_files/memorandums/full_memorandum_3/section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open("test_text_files/memorandums/full_memorandum_2/section_2_title.txt").read())
        section_2_content = Content(open("test_text_files/memorandums/full_memorandum_2/section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author, collaborators, date, title, subtitle, [section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and no collaborators
    def parse_partial_memorandum_1_test(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_1/partial_memorandum_1.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/memorandums/partial_memorandum_1/author.txt").read())

        collaborators = None

        date = Date(open("test_text_files/memorandums/partial_memorandum_1/date.txt").read())
        title = Title(open("test_text_files/memorandums/partial_memorandum_1/title.txt").read())
        subtitle = Subtitle(open("test_text_files/memorandums/partial_memorandum_1/subtitle.txt").read())

        section_1_title = Title(open("test_text_files/memorandums/partial_memorandum_1/section_1_title.txt").read())
        section_1_content = Content(open("test_text_files/memorandums/partial_memorandum_1/section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open("test_text_files/memorandums/partial_memorandum_1/section_2_title.txt").read())
        section_2_content = Content(open("test_text_files/memorandums/partial_memorandum_1/section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author, collaborators, date, title, subtitle, [section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and no date
    def parse_partial_memorandum_2_test(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_2/partial_memorandum_2.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/memorandums/partial_memorandum_2/author.txt").read())

        collaborators_txt = open("test_text_files/memorandums/partial_memorandum_2/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = None
        title = Title(open("test_text_files/memorandums/partial_memorandum_2/title.txt").read())
        subtitle = Subtitle(open("test_text_files/memorandums/partial_memorandum_2/subtitle.txt").read())

        section_1_title = Title(open("test_text_files/memorandums/partial_memorandum_2/section_1_title.txt").read())
        section_1_content = Content(open("test_text_files/memorandums/partial_memorandum_2/section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open("test_text_files/memorandums/partial_memorandum_2/section_2_title.txt").read())
        section_2_content = Content(open("test_text_files/memorandums/partial_memorandum_2/section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author, collaborators, date, title, subtitle, [section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and no subtitle
    def parse_partial_memorandum_3_test(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_3/partial_memorandum_3.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/memorandums/partial_memorandum_3/author.txt").read())

        collaborators_txt = open("test_text_files/memorandums/partial_memorandum_3/collaborators.txt").read().split(", ")
        collaborators = [Collaborator(collab) for collab in collaborators_txt]

        date = Date(open("test_text_files/memorandums/partial_memorandum_3/date.txt").read())
        title = Title(open("test_text_files/memorandums/partial_memorandum_3/title.txt").read())
        subtitle = None

        section_1_title = Title(open("test_text_files/memorandums/partial_memorandum_3/section_1_title.txt").read())
        section_1_content = Content(open("test_text_files/memorandums/partial_memorandum_3/section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open("test_text_files/memorandums/partial_memorandum_3/section_2_title.txt").read())
        section_2_content = Content(open("test_text_files/memorandums/partial_memorandum_3/section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author, collaborators, date, title, subtitle, [section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and no collaborators or date
    def parse_partial_memorandum_4_test(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_4/partial_memorandum_4.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/memorandums/partial_memorandum_4/author.txt").read())

        collaborators = None

        date = None
        title = Title(open("test_text_files/memorandums/partial_memorandum_4/title.txt").read())
        subtitle = Subtitle(open("test_text_files/memorandums/partial_memorandum_4/subtitle.txt").read())

        section_1_title = Title(open("test_text_files/memorandums/partial_memorandum_4/section_1_title.txt").read())
        section_1_content = Content(open("test_text_files/memorandums/partial_memorandum_4/section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open("test_text_files/memorandums/partial_memorandum_4/section_2_title.txt").read())
        section_2_content = Content(open("test_text_files/memorandums/partial_memorandum_4/section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author, collaborators, date, title, subtitle, [section_1, section_2]),
            parsed_memorandum
        )

    ## Test a memorandum with two sections and no optional fields filled
    def parse_partial_memorandum_5_test(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_5/partial_memorandum_5.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        author = Author(open("test_text_files/memorandums/partial_memorandum_5/author.txt").read())

        collaborators = None

        date = None
        title = Title(open("test_text_files/memorandums/partial_memorandum_5/title.txt").read())
        subtitle = None

        section_1_title = Title(open("test_text_files/memorandums/partial_memorandum_5/section_1_title.txt").read())
        section_1_content = Content(open("test_text_files/memorandums/partial_memorandum_5/section_1_content.txt").read())
        section_1 = Section(section_1_title, section_1_content)

        section_2_title = Title(open("test_text_files/memorandums/partial_memorandum_5/section_2_title.txt").read())
        section_2_content = Content(open("test_text_files/memorandums/partial_memorandum_5/section_2_content.txt").read())
        section_2 = Section(section_2_title, section_2_content)

        self.assertEqual(
            Memorandum(author, collaborators, date, title, subtitle, [section_1, section_2]),
            parsed_memorandum
        )
