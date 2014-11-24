__author__ = 'Paul Dapolito'

import unittest

from parser.parser import EasyTeXParser
from interpreters.interpreter import EasyTeXInterpreter


class EasyTeXParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = EasyTeXParser()
        self.interpreter = EasyTeXInterpreter()

    def validate_test(self):
        self.assertEqual(1, 1)

    # Problem Set Tests
    ## Test a problem set with one problem and all optional fields filled
    def interpret_problem_set_1_test(self):
        input_string = open("test_text_files/problem_sets/full_problem_set_1/full_problem_set_1.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/full_problem_set_1/full_problem_set_1.tex").read()

        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and all optional fields filled
    def interpret_problem_set_2_test(self):
        input_string = open("test_text_files/problem_sets/full_problem_set_2/full_problem_set_2.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/full_problem_set_2/full_problem_set_2.tex").read()

        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems that are missing labels and all other optional fields filled
    def interpret_problem_set_3_test(self):
        input_string = open("test_text_files/problem_sets/full_problem_set_3/full_problem_set_3.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/full_problem_set_3/full_problem_set_3.tex").read()

        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no collaborators
    def interpret_partial_problem_set_1_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_1/partial_problem_set_1.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_1/partial_problem_set_1.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no due date
    def interpret_partial_problem_set_2_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_2/partial_problem_set_2.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_2/partial_problem_set_2.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no title
    def interpret_partial_problem_set_3_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_3/partial_problem_set_3.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_3/partial_problem_set_3.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no course
    def interpret_partial_problem_set_4_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_4/partial_problem_set_4.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_4/partial_problem_set_4.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no school
    def interpret_partial_problem_set_5_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_5/partial_problem_set_5.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_5/partial_problem_set_5.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no school, course, or title
    def interpret_partial_problem_set_6_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_6/partial_problem_set_6.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_6/partial_problem_set_6.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no collaborators or due date
    def interpret_partial_problem_set_7_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_7/partial_problem_set_7.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_7/partial_problem_set_7.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems and no optional fields filled
    def interpret_partial_problem_set_8_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_8/partial_problem_set_8.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_8/partial_problem_set_8.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    ## Test a problem set with two problems that are missing labels and no optional fields filled
    def interpret_partial_problem_set_9_test(self):
        input_string = open("test_text_files/problem_sets/partial_problem_set_9/partial_problem_set_9.txt").read()
        parsed_problem_set = self.parser.parse_document(input_string)

        interpreted_problem_set = self.interpreter.interpret_document(parsed_problem_set)
        expected_tex_file = open("test_text_files/problem_sets/partial_problem_set_9/partial_problem_set_9.tex").read()
        self.assertEqual(interpreted_problem_set, expected_tex_file)

    # Memorandum Tests
    ## Test a memorandum with one section and all optional fields filled
    def interpret_full_memorandum_1(self):
        input_string = open("test_text_files/memorandums/full_memorandum_1/full_memorandum_1.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/full_memorandum_1/full_memorandum_1.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and all optional fields filled
    def interpret_full_memorandum_2(self):
        input_string = open("test_text_files/memorandums/full_memorandum_2/full_memorandum_2.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/full_memorandum_2/full_memorandum_2.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and no collaborators
    def interpret_partial_memorandum_1(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_1/partial_memorandum_1.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/partial_memorandum_1/partial_memorandum_1.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and no date
    def interpret_partial_memorandum_2(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_2/partial_memorandum_2.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/partial_memorandum_2/partial_memorandum_2.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and no subtitle
    def interpret_partial_memorandum_3(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_3/partial_memorandum_3.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/partial_memorandum_3/partial_memorandum_3.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and no collaborators or date
    def interpret_partial_memorandum_4(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_4/partial_memorandum_4.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/partial_memorandum_4/partial_memorandum_4.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

    ## Test a memorandum with two sections and no optional fields filled
    def interpret_partial_memorandum_5(self):
        input_string = open("test_text_files/memorandums/partial_memorandum_5/partial_memorandum_5.txt").read()
        parsed_memorandum = self.parser.parse_document(input_string)

        interpreted_memorandum = self.interpreter.interpret_document(parsed_memorandum)
        expected_tex_file = open("test_text_files/memorandums/partial_memorandum_5/partial_memorandum_5.tex").read()
        self.assertEqual(interpreted_memorandum, expected_tex_file)

