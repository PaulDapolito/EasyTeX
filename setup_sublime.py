__author__ = 'Paul Dapolito'

import os
import json


def main():
    # Copy syntax highlighting file
    os.system("mkdir ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/EasyTeX")
    os.system("cp EasyTex\ Grammar.tmLanguage ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/EasyTex")

    # Configure Sublime build file
    build_file = open("EasyTeX.sublime-build", "r+")
    build_config = json.loads(str(build_file.read()))
    project_path = os.path.dirname(os.path.realpath(__file__))
    build_config["working_dir"] = project_path
    build_file.seek(0)
    build_file.write(json.dumps(build_config))
    build_file.close()

    # Copy Sublime build file
    os.system("cp EasyTeX.sublime-build ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/User")

    print "Sublime Text 2 syntax highlighting and EasyTeX build have been configured. \
           Please restart Sublime Text 2 to see these changes."

if __name__ == "__main__":
    main()