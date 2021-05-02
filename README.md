# Java Diffchecker

Java Diffchecker is a python-based script capable of veryfing expected java runtime outputs in mass using files.

![Python](https://img.shields.io/static/v1?label=Python&message=3.9&color=orange)
![Base OS](https://img.shields.io/static/v1?label=Base%20OS&message=Win%2010&color=blue)
![Latest Release](https://img.shields.io/github/v/release/rafa-875/java-diffchecker?label=Latest)
![GitHub Last Commit](https://img.shields.io/github/last-commit/rafa-875/java-diffchecker?label=Last%20Commit)
![GitHub Repo Stars](https://img.shields.io/github/stars/rafa-875/java-diffchecker?style=social)

## Credits & General Information
 - **Compatibility:** Windows 10, MacOS, Linux
 - **Contributors:** *[Tiago Neto](https://github.com/tiagofneto)*

## How To Use
In order to properly run the script, the following command should be issued:

`python3 main.py <java_src_dir> <tests_dir> <test_id> [--show-all]`

- `java_src_dir` corresponds to the directory where the `.java` files to be compiled are located.
- `tests_dir` should be the directory where the input and output text files are placed.
- `test_id` would be an integer number corresponding to the `#-in.txt` and `#-out.txt` files in `test_dir`.
- `--show-all` available option to show all output comparison lines not skipping matching lines.

## To Do List
 - Add multiple test option.

## Required Modules
The following python modules are required for the execution of the script:
 - `sys`
 - `os` and `os.path`

All the previous listed modules are part of the default python 3.9 installation, so no new installations will be required.

## Detecting An Error

If the output of the program execution based on the input file given is not equal to the expected output, a line will appear showing: *the line where it occured*, *the output of the execution* and *the output expected for the matching line*. At the end of the execution the number of lines checked, lines which were not equal and lines which were equal will be displayed.

## Licensing
Licensed under the [GNU GPL v3.0](LICENSE) license.
