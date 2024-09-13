import re

def build_non_terminals():
    prefix = 'G.add_nonterminal('
    suffix = ')'

    seen_lines = set()
    modified_lines = []

    def add_nonterminal(terminal):
        return prefix + terminal + suffix

    with open('productiongrammar.py', 'r') as f:
        for line in f:
            stripped_line = line.strip()

            if stripped_line not in seen_lines:
                seen_lines.add(stripped_line)

                modified_line = add_nonterminal(stripped_line)

                modified_lines.append(modified_line)


    with open('newnonterminalgrammar.py', 'w') as f:
        for line in modified_lines:
            f.write(line + '\n')

    print("Complete.")

def replace_symbols(rhs):
    regex_table = {
        r'^f$': 'floatdcl',
        r'^i$': 'intdcl',
        r'^p$': 'print',
        r'^\=$': 'assign',
        r'^\+$': 'plus',
        r'^\-$': 'minus',
        r'^\*$': 'mult',
        r'^\/$': 'div',
        r'^\=': 'assign',
        r'^\=\=$': 'equal',
        r'^\!\=$': 'diff',
        r'^\<$': 'smallerthan',
        r'^\>$': 'biggerthan',
        r'^\<=$': 'smallerequal',
        r'^\>=$': 'biggerequal',
        r'^\|\|$': 'or',
        r'^\&\&$': 'and',
        r'^\!': 'not',
        r'^\;$': 'semicolon',
        r'^\,$': 'comma',
        r'^\($': 'openpara',
        r'^\)$': 'closepara',
        r'^\{$': 'openbracket',
        r'^\}$': 'closebracket',
        r'empty': ''
    }

    rhs_elements = rhs.split()
    replaced_elements = []
    for element in rhs_elements:
        replaced = False
        for pattern, replacement in regex_table.items():
            if re.match(pattern, element):
                replaced_elements.append(replacement)
                replaced = True
                break
        if not replaced:
            replaced_elements.append(element)

    return replaced_elements
            
    

def process_productions(line):
    lhs, rhs = line.split('->')
    
    lhs = lhs.strip()
    rhs = rhs.strip()

    rhs_elements = replace_symbols(rhs)
    rhs_elements_quoted = [f"'{element}'" for element in rhs_elements]
    
    formatted_production = f"G.add_production({lhs}, [{', '.join(rhs_elements_quoted)}])"
    
    return formatted_production
    

def build_productions(fileinput,fileoutput):
    with open(fileinput, 'r') as infile, open(fileoutput, 'w') as outfile:
        for line in infile:
            formatted_production = process_productions(line)
            outfile.write(formatted_production + '\n')

    print("Complete.")

    

def parse_productions(grammar_file):
    productions = {}
    with open(grammar_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        match = re.match(r"G\.add_production\('(\w+)', \[(.*)\]\) *#(\d+)",
                         line.strip())
        if match:
            lhs = match.group(1)
            rhs = match.group(2).split(', ') if match.group(2) else []
            prod_number = int(match.group(3))

            if lhs not in productions:
                productions[lhs] = []
            productions[lhs].append((rhs, prod_number))

    return productions

def generate_function(lhs, rhs_list):
    function_lines = []
    function_lines.append(f"def {lhs}(ts: token_sequence, p: predict_algorithm) -> None:")

    for i, (rhs, prod_number) in enumerate(rhs_list):
        if i == 0:
            function_lines.append(f"    if ts.peek() in p.predict({prod_number}):")
        else:
            function_lines.append(f"    elif ts.peek() in p.predict({prod_number}):")
            
        if rhs:
            for symbol in rhs:
                match = re.match(r"'([A-Z][A-Za-z]+)'", symbol)
                if match:
                    function_lines.append(f"        {match.group(1)}(ts, p)")
                else:
                    function_lines.append(f"        ts.match({symbol})")
                    
        else:
            function_lines.append("        return")

    function_lines.append("")
    return "\n".join(function_lines)

def write_functions_to_file(productions, output_file):
    with open(output_file, 'w') as file:
        for lhs, rhs_list in productions.items():
            function_code = generate_function(lhs, rhs_list)
            file.write(function_code)
            file.write("\n")


def add_lines_numbers(fileinput, fileoutput):
    with open(fileinput, 'r') as file:
        lines = file.readlines()

    for i in range(0, len(lines)):
        match = re.match("(.+) #[0-9]+", lines[i])
        if match:
            lines[i] = match.group(1) + f" #{i}"
        else:
            lines[i] = f"{lines[i].strip()} #{i}"

    with open(fileoutput, 'w') as file:
        file.write("\n".join(lines))

    