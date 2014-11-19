__author__ = 'Paul Dapolito'


class ProblemSetInterpreter(object):
    @classmethod
    def interpret_problem_set(cls, problem_set):
        document_class = "\documentclass[11pt,letterpaper,boxed]{hmcpset}"
        package_spec = "\usepackage[margin=0.9in]{geometry}"

        author = "\\name{" + problem_set.author.name + "}"
        course = "\\class{" + problem_set.course.text + "}"
        title = "\\assignment{" + problem_set.title.text + "}"
        due_date = "\\duedate{" + problem_set.due_date.date_string + "}"

        begin_document = "\\begin{document}"

        # Accumulate collaborators
        collaborators = ""
        if problem_set.collaborators[0]:
            collaborators += problem_set.collaborators[0].name
        for collaborator in problem_set.collaborators[1:]:
            collaborators += ", " + collaborator.name
        collaborators = "Worked with " + collaborators + "\\\\"

        # Accumulate problems
        problems = ""
        for problem in problem_set.problems:
            problems += cls.interpret_problem(problem)

        end_document = "\\end{document}"

        document_as_list = [
            document_class,
            package_spec,
            author,
            course,
            title,
            due_date,
            begin_document,
            collaborators,
            problems,
            end_document

        ]
        accumulated_document = "\n".join(document_as_list)

        return accumulated_document

    @classmethod
    def interpret_problem(cls, problem):
        problem_opening_tag = "\\begin{problem}[" + problem.label.text + "]"
        statement = problem.statement.text
        problem_closing_tag = "\\end{problem}"

        solution = "\\begin{solution}\n" + problem.solution.text + "\n\\end{solution}\n"

        problem_as_list = [problem_opening_tag, statement, problem_closing_tag, solution]
        accumulated_problem = "\n".join(problem_as_list)

        return accumulated_problem




