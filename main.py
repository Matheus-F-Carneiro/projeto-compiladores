# https://github.com/danielsaad/compiladores-codigos/blob/main/ac.py

prefix = 'G.add_nonterminal('
suffix = ')'

seen_lines = set()
modified_lines = []

def add_nonterminal(terminal):
    return prefix + terminal + suffix

with open('nonterminalgrammar.py', 'r') as f:
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
