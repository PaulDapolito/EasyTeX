__author__ = 'Paul Dapolito'

import os
import json


def main():
    # Copy syntax highlighting file
    os.system("mkdir ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/EasyTeX")
    os.system("cp EasyTex\ Grammar.tmLanguage ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/EasyTex")

    # Open and load Sublime build file
    build_file_name = "EasyTeX.sublime-build"
    build_file = open(build_file_name, "r+")
    build_config = json.loads(str(build_file.read()))
    build_file.close()

    # Add correct working directory to Sublime build configuration
    project_path = os.path.dirname(os.path.realpath(__file__))
    build_config["working_dir"] = project_path

    # Write Sublime build configuration file
    updated_build_file = open(build_file_name + ".tmp", "w+")
    updated_build_file.write(json.dumps(build_config))
    updated_build_file.close()

    # Move Sublime build configuration file to Sublime User Packages directory
    os.system("mv EasyTeX.sublime-build.tmp ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/User/EasyTeX.sublime-build")

    print "Sublime Text 2 syntax highlighting and EasyTeX build have been configured. \
           Please restart Sublime Text 2 to see these changes."

if __name__ == "__main__":
    main()