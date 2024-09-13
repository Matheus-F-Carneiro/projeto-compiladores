def print_rec_desc(G, output_file):
    with open(output_file, 'w') as f:
        for X in G.nonterminals():
            f.write(
                f'def {X}(ts:token_sequence, p:predict_algorithm) -> None:\n')
            first = True
            f.write(f'\tprint("\\nProductions for {X}:")\n')
            for P in G.productions_for(X):
                f.write('\tprint(f"{ts.peek()} and {p.predict(' + f'{P}' +
                        ')}")\n')
            for P in G.productions_for(X):
                if first:
                    f.write('\tif')
                    first = False
                else:
                    f.write('\telif')
                f.write(f' ts.peek() in p.predict({P}):\n')
                if len(G.rhs(P)) == 0:
                    f.write('\t\treturn\n')
                    continue
                for x in G.rhs(P):
                    if G.is_terminal(x):
                        f.write(f'\t\t ts.match("{x}")\n')
                    else:
                        f.write(f'\t\t {x}(ts,p)\n')
            f.write(f'\telse:\n\t\tprint("Syntax Error in {X}")\n')
            f.write('\t\tsys.exit(0)\n\n')

    print("Finished")
