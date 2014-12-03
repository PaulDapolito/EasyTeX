__author__ = 'Paul Dapolito'

# Basic elements
newline = "\n"
tab = "    "


class MemorandumInterpreter(object):
    @classmethod
    def interpret_memorandum(cls, memorandum):
        # Memorandum headers
        document_class = "\documentclass[letterpaper, boxed]{hmcpset}"
        document_class += newline
        package_spec = "\usepackage[margin=1in]{geometry}"
        package_spec += newline

        begin_document = "\\begin{document}"
        begin_document += newline

        begin_center = tab + "\\begin{center}"
        begin_center += newline

        # Title
        title = 2*tab + "\\Large{\\textbf{" + memorandum.title.text + "}} \\\\ "
        title += newline

        # Check for subtitle
        if memorandum.subtitle is not None:
            subtitle = 2*tab + "\\textit{" + memorandum.subtitle.text + "} \\\\"
            subtitle += newline
        else:
            subtitle = None

        # Author
        author = 2*tab + "\\large{" + memorandum.author.name + "} \\\\"
        author += newline

        # Check for collaborators
        if memorandum.collaborators is not None:
            # Accumulate collaborators
            collaborators = ""
            if memorandum.collaborators[0]:
                collaborators += memorandum.collaborators[0].name
            for collaborator in memorandum.collaborators[1:]:
                collaborators += ", " + collaborator.name
            collaborators = "Worked with " + collaborators
            collaborators = 2*tab + "\\large{" + collaborators + "} \\\\"
            collaborators += newline
        else:
            collaborators = None

        # Check for date
        if memorandum.date is not None:
            date = 2*tab + "\\large{" + memorandum.date.date_string + "}"
            date += newline
        else:
            date = None

        end_center = tab + "\\end{center}"
        end_center += newline

        # Accumulate sections
        sections = ""
        for section in memorandum.sections:
            sections += newline + cls.interpret_section(section)

        end_document = "\\end{document}"

        # Accumulate and filter document
        document_as_list = [
            document_class,
            package_spec,
            newline,
            begin_document,
            newline,
            begin_center,
            title,
            subtitle,
            author,
            collaborators,
            date,
            end_center,
            sections,
            newline,
            end_document,
            newline
        ]
        filtered_document = [elem for elem in document_as_list if elem is not None]
        accumulated_document = "".join(filtered_document)

        return accumulated_document

    @classmethod
    def interpret_section(cls, section):
        section_header = tab + "\large \\begin{flushleft}"
        section_header += newline

        section_title = tab + "\\textbf{" + section.title.text + "}"
        section_title += newline

        end_flush_left = tab + "\\end{flushleft}"
        end_flush_left += newline

        normal_size = tab + "\\normalsize"
        normal_size += newline

        ## Add tabs to each line of content
        content_text = section.content.text
        split_content = content_text.split("\n")
        content_lines_with_tabs = [2*tab + line for line in split_content]
        content = "\n".join(content_lines_with_tabs)

        section_as_list = [
            section_header,
            section_title,
            end_flush_left,
            normal_size,
            content,
            newline
        ]
        accumulated_section = "".join(section_as_list)

        return accumulated_section

