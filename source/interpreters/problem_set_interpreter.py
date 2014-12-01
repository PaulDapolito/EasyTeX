__author__ = 'Paul Dapolito'


class ProblemSetInterpreter(object):
    @classmethod
    def interpret_problem_set(cls, problem_set):
        document_class = "\documentclass[11pt,letterpaper,boxed]{hmcpset}"
        package_spec = "\usepackage[margin=0.9in]{geometry}"

        author = "\\name{" + problem_set.author.name + "}"

        # Check for course and school
        if problem_set.course is not None and problem_set.school is not None:
            course_and_school = "\\class{" + problem_set.course.text + ", " + problem_set.school.text + "}"
        elif problem_set.course is not None:
            course_and_school = "\\class{" + problem_set.course.text + "}"
        elif problem_set.school is not None:
            course_and_school = "\\class{" + problem_set.school.text + "}"
        else:
            course_and_school = None

        # Check for title
        if problem_set.title is not None:
            title = "\\assignment{" + problem_set.title.text + "}"
        else:
            title = None

        # Check for due date
        if problem_set.due_date is not None:
            due_date = "\\duedate{" + problem_set.due_date.date_string + "}"
        else:
            due_date = None

        begin_document = "\\begin{document}"

        # Accumulate collaborators
        if problem_set.collaborators:
            collaborators = ""
            if problem_set.collaborators[0]:
                collaborators += problem_set.collaborators[0].name
            for collaborator in problem_set.collaborators[1:]:
                collaborators += ", " + collaborator.name
            collaborators = "Worked with " + collaborators + "\\\\"
        else:
            collaborators = None

        # Accumulate problems
        problems = ""
        problems += cls.interpret_problem(problem_set.problems[0])
        for problem in problem_set.problems[1:]:
            problems += "\n" + "\pagebreak" + "\n" + cls.interpret_problem(problem)

        end_document = "\\end{document}"

        # Accumulate and filter document
        document_as_list = [
            document_class,
            package_spec,
            author,
            course_and_school,
            title,
            due_date,
            begin_document,
            collaborators,
            problems,
            end_document

        ]
        filtered_document = [elem for elem in document_as_list if elem is not None]
        accumulated_document = "\n".join(filtered_document)

        return accumulated_document

    @classmethod
    def interpret_problem(cls, problem):
        # Check for label
        if problem.label is not None:
            problem_opening_tag = "\\begin{problem}[" + problem.label.text + "]"
        else:
            problem_opening_tag = "\\begin{problem}"

        statement = problem.statement.text
        problem_closing_tag = "\\end{problem}"

        solution = "\\begin{solution}\n" + problem.solution.text + "\\end{solution}"

        problem_as_list = [problem_opening_tag, statement, problem_closing_tag, solution]
        accumulated_problem = "\n".join(problem_as_list)

        return accumulated_problem




