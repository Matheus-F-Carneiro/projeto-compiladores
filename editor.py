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