# Modules
from sys import argv, platform
import os
import os.path

# Variables
dir_char = '\\' if platform in ['win32', 'cygwin', 'msys'] else '/'
paths = {'temp': '.' + dir_char + 'temp' + dir_char}
usage = 'Usage: python3 ' + os.path.basename(__file__) + ' <src_paths> <tests_paths> <test_number> [<--show-all>]'

# Functions
def deleteFile(file):
    try:
        os.remove(file)
    except:
        pass

def deleteDirectory(dir):
    try:
        os.rmdir(dir)
    except:
        pass

def deleteTempDir():
    for root, dirs, files in os.walk(paths['temp'], topdown=False):
        for name in files:
            deleteFile(os.path.join(root, name))
        for name in dirs:
            deleteDirectory(os.path.join(root, name))
        deleteDirectory(root)

# Argument Parsing: Number Of Arguments
if len(argv) < 4:
    print('\033[91m\u2717\033[0m Error: 3 arguments are required, but only ' + str(len(argv)-1) + ' ' + ('was' if len(argv) == 2 else 'were') + ' given.\n' + usage)
    exit()
print('\033[92m\u2713\033[0m Successfully parsed the 3 required arguments given.')

# Argument Parsing: Arg.1 - src directory
paths['src'] = argv[1]

if not os.path.isdir(paths['src']):
    print('\033[91m\u2717\033[0m Error: Invalid paths specified at arg1, directory was not found or is corrupted.\n' + usage)
    exit()
print('\033[92m\u2713\033[0m Successfully parsed source paths.')

if not 'Main.java' in [f for f in os.listdir(paths['src']) if os.path.isfile(os.path.join(paths['src'], f))]:
    print('\033[91m\u2717\033[0m Error: Main.java not found at "' + paths['src'] + '".')
    exit()
print('\033[92m\u2713\033[0m Successfully parsed Main.java file.')

if not paths['src'].endswith(dir_char):
    paths['src'] += dir_char

# Argument Parsing: Arg.2 - tests directory
paths['tests'] = argv[2]

if not os.path.isdir(paths['tests']):
    print('\033[91m\u2717\033[0mError: Invalid paths specified at arg2, directory was not found or is corrupted.\n' + usage)
    exit()
print('\033[92m\u2713\033[0m Successfully parsed tests paths.')

if not paths['tests'].endswith(dir_char):
    paths['tests'] += dir_char
    print('\033[96m\u2713\033[0m Fixed missing directory indicator at the end of the paths.')

# Argument Parsing: Arg.3 - test id
test_id = argv[3]

if not test_id.isdigit():
    print('\033[91m\u2717\033[0m Error: Argument 3 is not a valid test number.\n' + usage)
    exit()
print('\033[92m\u2713\033[0m Successfully parsed test number.')

if not test_id + '-in.txt' in [f for f in os.listdir(paths['tests']) if os.path.isfile(os.path.join(paths['tests'], f))]:
    print('\033[91m\u2717\033[0m Error: Could not find ' + test_id + '-in.txt in ' + paths['tests'] + '.')
    exit()

lines_input = [l.strip().replace('\n', '') for l in open(paths['tests'] + test_id + '-in.txt', 'r').readlines()]
if len(lines_input) <= 0 or (len(lines_input) == 1 and lines_input[0] == ''):
    print('\033[91m\u2717\033[0m Error: ' + test_id + '-in.txt must not be empty.')
    exit()
print('\033[92m\u2713\033[0m Successfully parsed input file successfully.')

if not test_id + '-out.txt' in [f for f in os.listdir(paths['tests']) if os.path.isfile(os.path.join(paths['tests'], f))]:
    print('\033[91m\u2717\033[0m Error: Could not find ' + test_id + '-out.txt in ' + paths['tests'] + '.')
    exit()
print('\033[92m\u2713\033[0m Successfully parsed output file successfully.')

# Temporary Directory Setup
if 'temp' in os.listdir('.') and os.path.isdir('temp'):

    opt = ''
    while opt not in ['Y', 'N']:
        opt = input('Folder "temp" already exists, would you like to delete it? (Y/N) ').upper()
    
    if opt == 'Y':
        deleteTempDir()
    else:
        exit()
try:
    os.mkdir(paths['temp'])
    print('\033[92m\u2713\033[0m Successfully created temp directory.')
except Exception as exception:
    print('\033[91m\u2717\033[0m Error: Unable to create temp directory ({}).'.format(exception))

# Compile Java Project
try:
    if platform in ['win32', 'cygwin', 'msys']:
            os.system('javac -d ' + paths['temp'] + ' -cp ' + paths['src'] + ' ' + paths['src'] + '*.java"')
    else:
        os.system('javac -d ' + paths['temp'] + ' $(find ' + paths['src'] + ' -name "*.java")')
    print('\033[92m\u2713\033[0m Successfully compiled project.')
except Exception as exception:
    print('\033[91m\u2717\033[0m Error: Unable to compile java files ({}).'.format(exception))

# Add Missing Line If Needed
if '\n' not in [f for f in open(paths['tests'] + test_id + '-in.txt', 'r').readlines()][-1]:
    with open(paths['tests'] + test_id + '-in.txt', 'a') as f:
        f.write('\n')

# Obtain Java Exec Output
try:
    os.system('java -cp ' + paths['temp'] + ' Main < ' + paths['tests'] + test_id + '-in.txt > ' + paths['temp'] + 'raw.txt')
    print('\033[92m\u2713\033[0m Successfully executed and exported execution output.')
except Exception as exception:
    print('\033[91m\u2717\033[0m Error: Unable to execute or export output ({}).'.format(exception))

# Line Checking
print('\n\033[96mUsing "' + paths['tests'] + test_id + '-out.txt".\033[39m\n')

output_execution = [f.replace('\n', '') for f in open(paths['temp'] + 'raw.txt', 'r').readlines()]
output_expected = [f.replace('\n', '') for f in open(paths['tests'] + test_id + '-out.txt', 'r').readlines()]

lines = {'checked': 0, 'failed': 0, 'succeeded': 0}

lengths = [
    len(str(max(len(output_execution), len(output_expected)))) if len(str(max(len(output_execution), len(output_expected)))) > len('Ln') else len('Ln'),
    len(max(output_execution, key=len)) if len(max(output_execution, key=len)) > len('Output') else len('Output'),
    len(max(output_expected, key=len)) if len(max(output_expected, key=len)) > len('Expected') else len('Expected')
]

print("| {}{} | {}{} | {}{} |\n".format('Ln', ' ' * (lengths[0] - len('Ln')), 'Output', ' ' * (lengths[1] - len('Output')), 'Expected', ' ' * (lengths[2] - len('Expected'))))

for i in range(max(len(output_execution), len(output_expected))-1):

    if i > len(output_execution)-1:
        output_execution.append('')

    if i > len(output_expected)-1:
        output_expected.append('')

    lines['checked'] += 1
    spacer = [lengths[0]-(len(str(i+1))), lengths[1]-len(output_execution[i]), lengths[2]-len(output_expected[i])]

    if i >= len(output_execution):
        output_execution.append("")

    if i >= len(output_expected):
        output_expected.append("")

    if output_execution[i].strip() == output_expected[i].strip():
        lines['succeeded'] += 1
        if len(argv) > 4:
            if argv[4] == '--show-all':
                print('| {}{} | {}{} | {}{} |'.format(i+1, ' ' * spacer[0], output_execution[i], ' ' * spacer[1], output_expected[i], ' ' * spacer[2]))
    else:
        lines['failed'] += 1
        print('| {}{} | \033[91m{}\033[0m{} | \033[92m{}\033[0m{} |'.format(i+1, ' ' * spacer[0], output_execution[i], ' ' * spacer[1], output_expected[i], ' ' * spacer[2]))
        
print(f'\n\033[95m' + str(lines['checked']) + '\033[0m checked \033[91m' + str(lines['failed']) + '\033[0m failed \033[92m' + str(lines['succeeded']) + '\033[0m succeeded.')

# Delete Temp Dir & Files
deleteTempDir()
