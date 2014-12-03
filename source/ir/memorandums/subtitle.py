__author__ = 'Paul Dapolito'

from source.ir.easytex_element import EasyTeXElement
from source.errors.ir.memorandums.subtitle_error import SubtitleError


class Subtitle(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise SubtitleError("EasyTeX subtitles cannot be empty!")

    def __eq__(self, other):
        return self.text == other.text

