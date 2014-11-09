__author__ = 'Paul Dapolito'

from ir.problem_sets.school import School

from errors.parser.parse_text_error import ParseTextError
from errors.parser.parse_school_error import ParseSchoolError

from pyparsing import Word, Literal, Optional, ZeroOrMore, Group, OneOrMore, ParseException, delimitedList


# Terminals
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
digits = "0123456789"
symbols = "[]{}()<>\'\"=|.,;\\/"

# Grammar
text = delimitedList(Word(caps + lowers + digits + symbols), delim=' ', combine=True)
school = Literal("school: ") + text
course = Literal("course: ") + text


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
    def parse_school(input_string):
        try:
            parsed_school = school.parseString(input_string)
        except ParseException as pex:
            raise ParseSchoolError("Error parsing school: {}. Exception raised :{}".format(input_string, pex))

        if parsed_school[1]:
            return School(parsed_school[1])
        else:
            raise ParseSchoolError("Error parsing school: {}".format(input_string))
