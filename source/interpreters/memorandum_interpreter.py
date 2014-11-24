__author__ = 'Paul Dapolito'


class MemorandumInterpreter(object):
    @classmethod
    def interpret_memorandum(cls, memorandum):
        document_class = "\documentclass[letterpaper, boxed]{hmcpset}"
        package_spec = "\usepackage[margin=1in]{geometry}"

        begin_document = "\\begin{document}"
        begin_center = "\\begin{center}"

        title = "\\Large{\\textbf{" + memorandum.title.text + "}} \\\\ "
        subtitle = "\\textit{" + memorandum.subtitle.text + "} \\\\"
        author = "\\large{" + memorandum.author.name + "} \\\\"

        # Accumulate collaborators
        collaborators = ""
        if memorandum.collaborators[0]:
            collaborators += memorandum.collaborators[0].name
        for collaborator in memorandum.collaborators[1:]:
            collaborators += ", " + collaborator.name
        collaborators = "Worked with " + collaborators
        collaborators = "\\large{" + collaborators + "} \\\\"

        date = "\\large{" + memorandum.date.date_string + "}"

        end_center = "\\end{center}"

        sections = ""
        for section in memorandum.sections:
            sections += cls.interpret_section(section)

        end_document = "\\end{document}"

        document_as_list = [
            document_class,
            package_spec,
            begin_document,
            begin_center,
            title,
            subtitle,
            author,
            collaborators,
            date,
            end_center,
            sections,
            end_document
        ]
        accumulated_document = "\n".join(document_as_list)

        return accumulated_document

    @classmethod
    def interpret_section(cls, section):
        section_header = "\large \\begin{flushleft}"
        section_title = "\\textbf{" + section.title.text + "}"
        end_flush_left = "\\end{flushleft}"
        normal_size = "\\normalsize"

        section_content = section.content.text

        section_as_list = [section_header, section_title, end_flush_left, normal_size, section_content]
        accumulated_section = "\n".join(section_as_list)

        return accumulated_section

