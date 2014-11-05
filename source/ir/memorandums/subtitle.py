__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.memorandums.subtitle_error import SubtitleError


class Subtitle(EasyTeXElement):
    def __init__(self, text):
        self.text = text

        if self.text == "":
            raise SubtitleError("EasyTeX subtitles cannot be empty!")

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass
