import ast
import sys

def analyze_syntax(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError as error:
        sys.stderr.write(f'Syntax error: {error}\n')
        return False


with open('updated_python_code.py') as file:
    code = file.read()
    is_valid = analyze_syntax(code)
    if is_valid:
        print('The code is syntactically valid.')
    else:
        print('The code is not syntactically valid.')