G.add_terminal('begin')
G.add_terminal('end')
G.add_terminal('if')
G.add_terminal('else')
G.add_terminal('while')
G.add_terminal('return')
G.add_terminal('print')
G.add_terminal('int')
G.add_terminal('void')
G.add_terminal('float')
G.add_terminal('endif')
G.add_terminal('plus')
G.add_terminal('minus')
G.add_terminal('mult')
G.add_terminal('div')
G.add_terminal('assign')
G.add_terminal('equal')
G.add_terminal('diff')
G.add_terminal('smallerthan')
G.add_terminal('biggerthan')
G.add_terminal('smallerequal')
G.add_terminal('biggerequal')
G.add_terminal('or')
G.add_terminal('and')
G.add_terminal('not')
G.add_terminal('semicolon')
G.add_terminal('comma')
G.add_terminal('openpara')
G.add_terminal('closepara')
G.add_terminal('openbracket')
G.add_terminal('closebracket')
G.add_terminal('fnum')
G.add_terminal('inum')
G.add_terminal('cchar')
G.add_terminal('identifier')

regex_table = {
    r'^f$': 'floatdcl',
    r'^i$': 'intdcl',
    r'^p$': 'print',
    r'^[a-zA-Z_][a-zA-Z_0-9]*$' : 'identifier',
    r'^\=$': 'assign',
    r'^\+$': 'plus',
    r'^\-$': 'minus',
    r'^\*$': 'mult',
    r'^\\$': 'div',
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
    r'^[0-9]+$': 'inum',
    r'^[0-9]+\.[0-9]+$': 'fnum',
    r'^\'.\'': 'cchar'
}