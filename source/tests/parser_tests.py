__author__ = 'Paul Dapolito'

import unittest

from parser.parser import EasyTeXParser


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