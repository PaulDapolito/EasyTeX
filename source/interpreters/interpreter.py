__author__ = 'Paul Dapolito'

from source.ir.problem_sets.problem_set import ProblemSet
from source.ir.memorandums.memorandum import Memorandum

from problem_set_interpreter import ProblemSetInterpreter
from memorandum_interpreter import MemorandumInterpreter

from source.errors.interpreters.interpret_document_error import InterpretDocumentError


class EasyTeXInterpreter(object):
    @classmethod
    def interpret_document(cls, document):
        if type(document) is ProblemSet:
            return ProblemSetInterpreter.interpret_problem_set(document)
        elif type(document) is Memorandum:
            return MemorandumInterpreter.interpret_memorandum(document)
        else:
            raise InterpretDocumentError("Could not interpret document: no memorandum or problem set found!")
