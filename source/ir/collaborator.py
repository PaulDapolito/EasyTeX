__author__ = 'Paul Dapolito'

from ir.easytex_element import EasyTeXElement
from errors.collaborator_error import CollaboratorError


class Collaborator(EasyTeXElement):
    def __init__(self, name):
        self.name = name

        if self.name == "":
            raise CollaboratorError("EasyTeX collaborators cannot be empty!")

    # TODO: Implement proper LaTeX output
    def latex_output(self):
        pass
