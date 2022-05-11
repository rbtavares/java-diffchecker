# Java Diffchecker

Java Diffchecker is a python script designed to verify ouputs of a java execution with a given input.

![Python](https://img.shields.io/static/v1?label=Python&message=3.10&color=orange)
![Latest Release](https://img.shields.io/github/v/release/rafa-875/java-diffchecker?label=Latest)
![GitHub Last Commit](https://img.shields.io/github/last-commit/rafa-875/java-diffchecker?label=Last%20Commit)

## Credits & General Information

- **Assured Compatibility:** Windows, MacOS
- **Contributors:** *[Tiago Neto](https://github.com/tiagofneto)*

## How To Use

In order to properly use the script, the following command should be issued:

`python3 main.py <java_src_dir> <tests_dir> <test_id> [--show-all]`

- `java_src_dir` corresponds to the project's base directory, where the `.java` files to be compiled are located.
- `tests_dir` should be the directory where the input and output text files are placed.
- `test_id` would be an integer number corresponding to the `#-in.txt` and `#-out.txt` files in `test_dir`.
- `--show-all` available option to show all output comparison lines not skipping matching lines.

**Warning:** Your project's main java file should be called `Main.java` and be located at the base directory of the project. This can be modified by changing properties in the code. (Do at your own risk)

## Required Modules

The following python modules are required for the execution of the script:

- `sys`
- `os` and `os.path`

All the previous listed modules are part of the default python 3.10 installation, so no new installations will be required.

## Detecting An Error

If the output of the program execution based on the input file given is not equal to the expected output, a line will appear showing: *the line where it occured*, *the output of the execution* and *the output expected for the matching line*. At the end of the execution the number of lines checked, lines which were not equal and lines which were equal will be displayed.

## Licensing

Licensed under the [MIT](LICENSE) license.
