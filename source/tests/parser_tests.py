__author__ = 'Paul Dapolito'

import unittest

from parser.parser import EasyTeXParser

from ir.problem_sets.school import School
from ir.problem_sets.course import Course
from ir.problem_sets.due_date import DueDate

from ir.problem_sets.label import Label
from ir.problem_sets.statement import Statement
from ir.problem_sets.solution import Solution


class EasyTeXParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = EasyTeXParser()

    def validate_test(self):
        self.assertEqual(1, 1)

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

    def parse_basic_school_test(self):
        input_string = "school: Staten Island Academy"
        parsed_school = self.parser.parse_school(input_string)

        self.assertEqual(School("Staten Island Academy"), parsed_school)

    def parse_school_with_symbols_test(self):
        input_string = "school: Dallas Science School: \\textbf{magnet}"
        parsed_school = self.parser.parse_school(input_string)

        self.assertEqual(School("Dallas Science School: \\textbf{magnet}"), parsed_school)

    def parse_basic_course_test(self):
        input_string = "course: Programming Languages"
        parsed_course = self.parser.parse_course(input_string)

        self.assertEqual(Course("Programming Languages"), parsed_course)

    def parse_course_with_symbols_test(self):
        input_string = "course: \\textbf{Domain-Specific} Languages"
        parsed_course = self.parser.parse_course(input_string)

        self.assertEqual(Course("\\textbf{Domain-Specific} Languages"), parsed_course)

    def parse_basic_due_date_test(self):
        input_string = "due_date: September 21, 2015"
        parsed_due_date = self.parser.parse_due_date(input_string)

        self.assertEqual(DueDate("September 21, 2015"), parsed_due_date)

    def parse_due_date_with_symbols_test(self):
        input_string = "due_date: 09/21/2015"
        parsed_due_date = self.parser.parse_due_date(input_string)

        self.assertEqual(DueDate("09/21/2015"), parsed_due_date)

    def parse_basic_label_test(self):
        input_string = "label: 1"
        parsed_label = self.parser.parse_label(input_string)

        self.assertEqual(Label("1"), parsed_label)

    def parse_label_with_symbols_test(self):
        input_string = "label: 1(a)(b)"
        parsed_label = self.parser.parse_label(input_string)

        self.assertEqual(Label("1(a)(b)"), parsed_label)

    def parse_basic_statement_test(self):
        statement = "What is the rate of change $f'$ of a function $f$ at the point $a$?"
        input_string = "statement: " + statement
        parsed_statement = self.parser.parse_statement(input_string)

        self.assertEqual(Statement(statement), parsed_statement)

    def parse_advanced_statement_test(self):
        statement = "Carefully prove that if $L_1$ and $L_2$ are languages and $L_1 \subseteq L_2*$, then $L_1 * \subseteq L_2*$"
        input_string = "statement: " + statement
        parsed_statement = self.parser.parse_statement(input_string)

        self.assertEqual(Statement(statement), parsed_statement)

    def parse_basic_solution_test(self):
        solution = "The derivative of $f$ at $a$, denoted $f'(a)$, is: \
                        $$ f'(a) = \lim_{k \\to 0} \\frac{f(a + h) - f(a)}{h} $$"
        input_string = "solution: \r \t" + solution
        parsed_solution = self.parser.parse_solution(input_string)

        self.assertEqual(Solution(solution), parsed_solution)

    def parse_advanced_solution_test(self):
        solution = '''Suppose $L_1$ is some arbitrary language over an alphabet $\Sigma$ with words $l_1,l_2,l_3,...,l_{n-1},l_{n}$. $L_1$ is defined as:
                $$ L_1 = \{l_1, l_2, l_3,...,l_{n-1}, l_{n}\} $$

            For the languages $L_1$ and $L_2$, we are given that that $L_1 \subseteq L_2*$. Using the fact that $L_1 \subseteq L_2*$ and the definition of the Kleene star operation, $L_2*$ must be such that:
                $$ \{\epsilon, l_1, l_2, l_3,...,l_{n-1}, l_{n},...\} \subseteq L_2* #

            Using the definition of the Kleene star operation again, we know that $L_1*$ is given by:
                $$ L_1* =  \{\epsilon, l_1, l_2, l_3,...,l_{n-1}, l_{n},...\} $$

            Thus, Equation 1 becomes:
                $$ L_1* \subseteq L_2* $$

            And we have thus proven that if $L_1$ and $L_2$ are languages and $L_1 \subseteq L_2*$, then $L_1 * \subseteq L_2*$. QED.'''
        input_string = "solution: \r \t" + solution
        parsed_solution = self.parser.parse_solution(input_string)

        self.assertEqual(Solution(solution), parsed_solution)