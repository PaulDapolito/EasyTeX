__author__ = 'Paul Dapolito'

# Basic elements
newline = "\n"
tab = "    "


class ProblemSetInterpreter(object):
    @classmethod
    def interpret_problem_set(cls, problem_set):
        # Problem set headers
        document_class = "\documentclass[11pt,letterpaper,boxed]{hmcpset}"
        package_spec = "\usepackage[margin=0.9in]{geometry}"

        # Author
        author = "\\name{" + problem_set.author.name + "}"
        author = author + newline

        # Check for course and school
        if problem_set.course is not None and problem_set.school is not None:
            course_and_school = "\\class{" + problem_set.course.text + ", " + problem_set.school.text + "}"
            course_and_school = course_and_school + newline
        elif problem_set.course is not None:
            course_and_school = "\\class{" + problem_set.course.text + "}"
            course_and_school = course_and_school + newline
        elif problem_set.school is not None:
            course_and_school = "\\class{" + problem_set.school.text + "}"
            course_and_school = course_and_school + newline
        else:
            course_and_school = None

        # Check for title
        if problem_set.title is not None:
            title = "\\assignment{" + problem_set.title.text + "}"
            title = title + newline
        else:
            title = None

        # Check for due date
        if problem_set.due_date is not None:
            due_date = "\\duedate{" + problem_set.due_date.date_string + "}"
            due_date = due_date + newline
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
            collaborators = tab + collaborators + 2*newline
        else:
            collaborators = None

        # Accumulate problems
        problems = ""
        problems += cls.interpret_problem(problem_set.problems[0])
        for problem in problem_set.problems[1:]:
            problems += newline + tab + "\pagebreak" + 2*newline + cls.interpret_problem(problem)

        end_document = "\\end{document}"

        # Accumulate and filter document
        document_as_list = [
            document_class,
            newline,
            package_spec,
            2*newline,
            author,
            course_and_school,
            title,
            due_date,
            newline,
            begin_document,
            2*newline,
            collaborators,
            problems,
            newline,
            end_document,
            newline
        ]
        filtered_document = [elem for elem in document_as_list if elem is not None]
        accumulated_document = "".join(filtered_document)

        return accumulated_document

    @classmethod
    def interpret_problem(cls, problem):
        # Assemble problem statement
        ## Check for label
        if problem.label is not None:
            problem_opening_tag = "\\begin{problem}[" + problem.label.text + "]"
        else:
            problem_opening_tag = "\\begin{problem}"
        ## Add tabs to each line of statement
        statement_text = problem.statement.text
        split_statement = statement_text.split("\n")
        statement_lines_with_tabs = [2*tab + line for line in split_statement]
        statement = "\n".join(statement_lines_with_tabs)
        problem_closing_tag = "\\end{problem}"

        # Assemble problem solution
        solution_opening_tag = "\\begin{solution}"
        solution_text = problem.solution.text
        ## Add tabs to each line of solution
        split_solution = solution_text.split("\n")
        solution_lines_with_tabs = [2*tab + line for line in split_solution if line != ""]
        solution = "\n".join(solution_lines_with_tabs)
        solution_closing_tag = "\\end{solution}"

        # Assemble problem as list and then accumulate
        problem_as_list = [
            tab, problem_opening_tag,
            newline,
            statement,
            newline,
            tab, problem_closing_tag,
            2*newline,
            tab, solution_opening_tag,
            newline,
            solution,
            newline,
            tab, solution_closing_tag,
            newline
        ]
        accumulated_problem = "".join(problem_as_list)

        return accumulated_problem
