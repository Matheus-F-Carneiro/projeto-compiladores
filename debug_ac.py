import re
import sys

import print_rec_desc
from grammar import Grammar
from ll1_check import is_ll1
from predict import predict_algorithm
from token_sequence import token_sequence


def create_ac_grammar() -> Grammar:
    G = Grammar()
    G.add_terminal('begin') #0
    G.add_terminal('main') #1
    G.add_terminal('end') #2
    G.add_terminal('$') #3
    G.add_terminal('if') #4
    G.add_terminal('else') #5
    G.add_terminal('while') #6
    G.add_terminal('return') #7
    G.add_terminal('printf') #8
    G.add_terminal('intdcl') #9
    G.add_terminal('void') #10
    G.add_terminal('floatdcl') #11
    G.add_terminal('chardcl') #12
    G.add_terminal('endif') #13
    G.add_terminal('plus') #14
    G.add_terminal('minus') #15
    G.add_terminal('mult') #16
    G.add_terminal('div') #17
    G.add_terminal('assign') #18
    G.add_terminal('inum') #19
    G.add_terminal('fnum') #20
    G.add_terminal('cchar') #21
    G.add_terminal('equal') #22
    G.add_terminal('diff') #23
    G.add_terminal('smallerthan') #24
    G.add_terminal('biggerthan') #25
    G.add_terminal('smallerequal') #26
    G.add_terminal('biggerequal') #27
    G.add_terminal('or') #28
    G.add_terminal('and') #29
    G.add_terminal('not') #30
    G.add_terminal('semicolon') #31
    G.add_terminal('comma') #32
    G.add_terminal('openpara') #33
    G.add_terminal('closepara') #34
    G.add_terminal('openbracket') #35
    G.add_terminal('closebracket') #36
    G.add_terminal('fnum') #37
    G.add_terminal('inum') #38
    G.add_terminal('cchar') #39
    G.add_terminal('identifier') #40
    G.add_nonterminal('Program') #41
    G.add_nonterminal('FunctList') #42
    G.add_nonterminal('Func') #43
    G.add_nonterminal('Stmts') #44
    G.add_nonterminal('Stmt') #45
    G.add_nonterminal('SimpleStmt') #46
    G.add_nonterminal('CondIf') #47
    G.add_nonterminal('CondElse') #48
    G.add_nonterminal('Loop') #49
    G.add_nonterminal('VarDefine') #50
    G.add_nonterminal('VarId') #51
    G.add_nonterminal('Assign') #52
    G.add_nonterminal('Expr') #53
    G.add_nonterminal('Math') #54
    G.add_nonterminal('MathAdd') #55
    G.add_nonterminal('MathCont') #56
    G.add_nonterminal('MathMult') #57
    G.add_nonterminal('MathPar') #58
    G.add_nonterminal('Logic') #59
    G.add_nonterminal('LogicTail') #60
    G.add_nonterminal('LogicComp') #61
    G.add_nonterminal('LogicCompTail') #62
    G.add_nonterminal('TypeFunc') #63
    G.add_nonterminal('TypeSpec') #64
    G.add_nonterminal('Id') #65
    G.add_nonterminal('AddOp') #66
    G.add_nonterminal('MultOp') #67
    G.add_nonterminal('LopNeg') #68
    G.add_nonterminal('ConnecOp') #69
    G.add_nonterminal('CompOp') #70
    G.add_nonterminal('Print') #71
    G.add_nonterminal('Literals') #72
    G.add_production('Program', ['FunctList', '$']) #73
    G.add_production('FunctList', ['Func', 'FunctList']) #74
    G.add_production('FunctList', []) #75
    G.add_production('Func', [
        'TypeFunc', 'main', 'openpara', 'closepara', 
        'openbracket', 'Stmts', 'closebracket'
    ]) #76
    G.add_production('Stmts', ['Stmt', 'Stmts']) #77
    G.add_production('Stmts', []) #78
    G.add_production('Stmt', ['SimpleStmt']) #79
    G.add_production('Stmt', ['CondIf']) #80
    G.add_production('Stmt', ['Loop']) #81
    G.add_production('SimpleStmt', ['VarDefine', 'semicolon']) #82
    G.add_production('SimpleStmt', ['Assign', 'semicolon']) #83
    G.add_production('SimpleStmt', ['Print', 'semicolon']) #84
    G.add_production('CondIf', [
        'if', 'openpara', 'Logic', 'closepara', 'openbracket',
        'Stmts', 'closebracket', 'CondElse', 'endif'
    ]) #85
    G.add_production('CondElse',['else', 'openbracket', 'Stmts', 'closebracket']) #86
    G.add_production('CondElse', []) #87
    G.add_production('Loop', [
        'while', 'openpara', 'Logic', 'closepara', 'openbracket', 'Stmts','closebracket'
    ]) #88
    G.add_production('VarDefine', ['TypeSpec', 'VarId']) #89
    G.add_production('VarId', ['identifier']) #90
    G.add_production('Assign', ['identifier', 'assign', 'Expr']) #91
    G.add_production('Expr', ['Logic']) #92
    G.add_production('Logic', ['LogicComp', 'LogicTail']) #93
    G.add_production('Logic', ['LopNeg', 'Logic']) #94
    G.add_production('LogicTail', ['ConnecOp', 'Logic']) #95
    G.add_production('LogicTail', []) #96
    G.add_production('LogicComp', ['Math', 'LogicCompTail']) #97
    G.add_production('LogicCompTail', []) #98
    G.add_production('LogicCompTail', ['CompOp', 'Math']) #99
    G.add_production('Math', ['MathCont', 'MathAdd']) #100
    G.add_production('MathAdd', ['AddOp', 'MathCont', 'MathAdd']) #101
    G.add_production('MathAdd', []) #102
    G.add_production('MathCont', ['MathPar', 'MathMult']) #103
    G.add_production('MathMult', ['MultOp', 'MathPar', 'MathMult']) #104
    G.add_production('MathMult', []) #105
    G.add_production('MathPar', ['openpara', 'Expr', 'closepara']) #106
    G.add_production('MathPar', ['Id']) #107
    G.add_production('Print', ['printf', 'openpara', 'Id', 'closepara']) #108
    G.add_production('TypeFunc', ['TypeSpec']) #109
    G.add_production('TypeFunc', ['void']) #110
    G.add_production('TypeSpec', ['intdcl']) #111
    G.add_production('TypeSpec', ['floatdcl']) #112
    G.add_production('TypeSpec', ['chardcl']) #113
    G.add_production('Id', ['Literals']) #114
    G.add_production('Id', ['identifier']) #115
    G.add_production('Literals', ['inum']) #116
    G.add_production('Literals', ['fnum']) #117
    G.add_production('Literals', ['cchar']) #118
    G.add_production('AddOp', ['plus']) #119
    G.add_production('AddOp', ['minus']) #120
    G.add_production('MultOp', ['mult']) #121
    G.add_production('MultOp', ['div']) #122
    G.add_production('LopNeg', ['not']) #123
    G.add_production('ConnecOp', ['or']) #124
    G.add_production('ConnecOp', ['and']) #125
    G.add_production('CompOp', ['equal']) #126
    G.add_production('CompOp', ['biggerthan']) #127
    G.add_production('CompOp', ['smallerthan']) #128
    G.add_production('CompOp', ['biggerequal']) #129
    G.add_production('CompOp', ['smallerequal']) #130
    G.add_production('CompOp', ['diff']) #131

    return G


regex_table = {
    r'^float$': 'floatdcl',
    r'^int$': 'intdcl',
    r'^char$': 'chardcl',
    r'^printf$': 'printf',
    r'^if$': 'if',
    r'^else$': 'else',
    r'^endif$': 'endif',
    r'^while$': 'while',
    r'^return$': 'return',
    r'^main$': 'main',
    r'^=$': 'assign',
    r'^\+$': 'plus',
    r'^\-$': 'minus',
    r'^\*$': 'mult',
    r'^/$': 'div',
    r'^==$': 'equal',
    r'^\!\=$': 'diff',
    r'^\<$': 'smallerthan',
    r'^\>$': 'biggerthan',
    r'^\<=$': 'smallerequal',
    r'^\>=$': 'biggerequal',
    r'^\|\|$': 'or',
    r'^&&$': 'and',
    r'^\!$': 'not',
    r'^\;$': 'semicolon',
    r'^\,$': 'comma',
    r'^\($': 'openpara',
    r'^\)$': 'closepara',
    r'^\{$': 'openbracket',
    r'^\}$': 'closebracket',
    r'^[0-9]+$': 'inum',
    r'^[0-9]+\.[0-9]+$': 'fnum',
    r'^\'.\'$': 'cchar',
    r'^%$': 'percent',
    r'^%[diuf]$': 'format_specifier',
    r'^[a-zA-Z_][a-zA-Z_0-9]*$': 'identifier',
}


def lexical_analyzer(filepath) -> str:
    with open(filepath, 'r') as f:
        code = f.read()
    token_sequence = []
    token_pattern = r'[a-zA-Z_][a-zA-Z_0-9]*|[0-9]+\.[0-9]+|[0-9]+|==|!=|<=|>=|\|\||&&|[+\-*/%<>=!;,(){}]'
    tokens = re.findall(token_pattern, code)
    for t in tokens:
        found = False
        for regex, category in regex_table.items():
            if re.match(regex, t):
                token_sequence.append(category)
                found = True
                break
        if not found:
            print('Lexical error: ', t)
            exit(0)
    token_sequence.append('$') 
    return token_sequence # type: ignore

def Program(ts:token_sequence, p:predict_algorithm) -> None: # type: ignore
    print("\nProductions for Program:")
    print(f"{ts.peek()} and {p.predict(73)}")
    if ts.peek() in p.predict(73):
        FunctList(ts,p)
        ts.match("$")
    else:
       print("Syntax Error in Program")
       sys.exit(0)

def Program(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Program:")
    print(f"{ts.peek()} and {p.predict(73)}")
    if ts.peek() in p.predict(73):
         FunctList(ts,p)
         ts.match("$")
    else:
        print("Syntax Error in Program")
        sys.exit(0)

def FunctList(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for FunctList:")
    print(f"{ts.peek()} and {p.predict(74)}")
    print(f"{ts.peek()} and {p.predict(75)}")
    if ts.peek() in p.predict(74):
         Func(ts,p)
         FunctList(ts,p)
    elif ts.peek() in p.predict(75):
        return
    else:
        print("Syntax Error in FunctList")
        sys.exit(0)

def Func(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Func:")
    print(f"{ts.peek()} and {p.predict(76)}")
    if ts.peek() in p.predict(76):
         TypeFunc(ts,p)
         ts.match("main")
         ts.match("openpara")
         ts.match("closepara")
         ts.match("openbracket")
         Stmts(ts,p)
         ts.match("closebracket")
    else:
        print("Syntax Error in Func")
        sys.exit(0)

def Stmts(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Stmts:")
    print(f"{ts.peek()} and {p.predict(77)}")
    print(f"{ts.peek()} and {p.predict(78)}")
    if ts.peek() in p.predict(77):
         Stmt(ts,p)
         Stmts(ts,p)
    elif ts.peek() in p.predict(78):
        return
    else:
        print("Syntax Error in Stmts")
        sys.exit(0)

def Stmt(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Stmt:")
    print(f"{ts.peek()} and {p.predict(79)}")
    print(f"{ts.peek()} and {p.predict(80)}")
    print(f"{ts.peek()} and {p.predict(81)}")
    if ts.peek() in p.predict(79):
         SimpleStmt(ts,p)
    elif ts.peek() in p.predict(80):
         CondIf(ts,p)
    elif ts.peek() in p.predict(81):
         Loop(ts,p)
    else:
        print("Syntax Error in Stmt")
        sys.exit(0)

def SimpleStmt(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for SimpleStmt:")
    print(f"{ts.peek()} and {p.predict(82)}")
    print(f"{ts.peek()} and {p.predict(83)}")
    print(f"{ts.peek()} and {p.predict(84)}")
    if ts.peek() in p.predict(82):
         VarDefine(ts,p)
         ts.match("semicolon")
    elif ts.peek() in p.predict(83):
         Assign(ts,p)
         ts.match("semicolon")
    elif ts.peek() in p.predict(84):
         Print(ts,p)
         ts.match("semicolon")
    else:
        print("Syntax Error in SimpleStmt")
        sys.exit(0)

def CondIf(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for CondIf:")
    print(f"{ts.peek()} and {p.predict(85)}")
    if ts.peek() in p.predict(85):
         ts.match("if")
         ts.match("openpara")
         Logic(ts,p)
         ts.match("closepara")
         ts.match("openbracket")
         Stmts(ts,p)
         ts.match("closebracket")
         CondElse(ts,p)
         ts.match("endif")
    else:
        print("Syntax Error in CondIf")
        sys.exit(0)

def CondElse(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for CondElse:")
    print(f"{ts.peek()} and {p.predict(86)}")
    print(f"{ts.peek()} and {p.predict(87)}")
    if ts.peek() in p.predict(86):
         ts.match("else")
         ts.match("openbracket")
         Stmts(ts,p)
         ts.match("closebracket")
    elif ts.peek() in p.predict(87):
        return
    else:
        print("Syntax Error in CondElse")
        sys.exit(0)

def Loop(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Loop:")
    print(f"{ts.peek()} and {p.predict(88)}")
    if ts.peek() in p.predict(88):
         ts.match("while")
         ts.match("openpara")
         Logic(ts,p)
         ts.match("closepara")
         ts.match("openbracket")
         Stmts(ts,p)
         ts.match("closebracket")
    else:
        print("Syntax Error in Loop")
        sys.exit(0)

def VarDefine(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for VarDefine:")
    print(f"{ts.peek()} and {p.predict(89)}")
    if ts.peek() in p.predict(89):
         TypeSpec(ts,p)
         VarId(ts,p)
    else:
        print("Syntax Error in VarDefine")
        sys.exit(0)

def VarId(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for VarId:")
    print(f"{ts.peek()} and {p.predict(90)}")
    if ts.peek() in p.predict(90):
         ts.match("identifier")
    else:
        print("Syntax Error in VarId")
        sys.exit(0)

def Assign(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Assign:")
    print(f"{ts.peek()} and {p.predict(91)}")
    if ts.peek() in p.predict(91):
         ts.match("identifier")
         ts.match("assign")
         Expr(ts,p)
    else:
        print("Syntax Error in Assign")
        sys.exit(0)

def Expr(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Expr:")
    print(f"{ts.peek()} and {p.predict(92)}")
    if ts.peek() in p.predict(92):
         Logic(ts,p)
    else:
        print("Syntax Error in Expr")
        sys.exit(0)

def Math(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Math:")
    print(f"{ts.peek()} and {p.predict(100)}")
    if ts.peek() in p.predict(100):
         MathCont(ts,p)
         MathAdd(ts,p)
    else:
        print("Syntax Error in Math")
        sys.exit(0)

def MathAdd(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for MathAdd:")
    print(f"{ts.peek()} and {p.predict(101)}")
    print(f"{ts.peek()} and {p.predict(102)}")
    if ts.peek() in p.predict(101):
         AddOp(ts,p)
         MathCont(ts,p)
         MathAdd(ts,p)
    elif ts.peek() in p.predict(102):
        return
    else:
        print("Syntax Error in MathAdd")
        sys.exit(0)

def MathCont(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for MathCont:")
    print(f"{ts.peek()} and {p.predict(103)}")
    if ts.peek() in p.predict(103):
         MathPar(ts,p)
         MathMult(ts,p)
    else:
        print("Syntax Error in MathCont")
        sys.exit(0)

def MathMult(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for MathMult:")
    print(f"{ts.peek()} and {p.predict(104)}")
    print(f"{ts.peek()} and {p.predict(105)}")
    if ts.peek() in p.predict(104):
         MultOp(ts,p)
         MathPar(ts,p)
         MathMult(ts,p)
    elif ts.peek() in p.predict(105):
        return
    else:
        print("Syntax Error in MathMult")
        sys.exit(0)

def MathPar(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for MathPar:")
    print(f"{ts.peek()} and {p.predict(106)}")
    print(f"{ts.peek()} and {p.predict(107)}")
    if ts.peek() in p.predict(106):
         ts.match("openpara")
         Expr(ts,p)
         ts.match("closepara")
    elif ts.peek() in p.predict(107):
         Id(ts,p)
    else:
        print("Syntax Error in MathPar")
        sys.exit(0)

def Logic(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Logic:")
    print(f"{ts.peek()} and {p.predict(93)}")
    print(f"{ts.peek()} and {p.predict(94)}")
    if ts.peek() in p.predict(93):
         LogicComp(ts,p)
         LogicTail(ts,p)
    elif ts.peek() in p.predict(94):
         LopNeg(ts,p)
         Logic(ts,p)
    else:
        print("Syntax Error in Logic")
        sys.exit(0)

def LogicTail(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for LogicTail:")
    print(f"{ts.peek()} and {p.predict(95)}")
    print(f"{ts.peek()} and {p.predict(96)}")
    if ts.peek() in p.predict(95):
         ConnecOp(ts,p)
         Logic(ts,p)
    elif ts.peek() in p.predict(96):
        return
    else:
        print("Syntax Error in LogicTail")
        sys.exit(0)

def LogicComp(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for LogicComp:")
    print(f"{ts.peek()} and {p.predict(97)}")
    if ts.peek() in p.predict(97):
         Math(ts,p)
         LogicCompTail(ts,p)
    else:
        print("Syntax Error in LogicComp")
        sys.exit(0)

def LogicCompTail(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for LogicCompTail:")
    print(f"{ts.peek()} and {p.predict(98)}")
    print(f"{ts.peek()} and {p.predict(99)}")
    if ts.peek() in p.predict(98):
        return
    elif ts.peek() in p.predict(99):
         CompOp(ts,p)
         Math(ts,p)
    else:
        print("Syntax Error in LogicCompTail")
        sys.exit(0)

def TypeFunc(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for TypeFunc:")
    print(f"{ts.peek()} and {p.predict(109)}")
    print(f"{ts.peek()} and {p.predict(110)}")
    if ts.peek() in p.predict(109):
         TypeSpec(ts,p)
    elif ts.peek() in p.predict(110):
         ts.match("void")
    else:
        print("Syntax Error in TypeFunc")
        sys.exit(0)

def TypeSpec(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for TypeSpec:")
    print(f"{ts.peek()} and {p.predict(111)}")
    print(f"{ts.peek()} and {p.predict(112)}")
    print(f"{ts.peek()} and {p.predict(113)}")
    if ts.peek() in p.predict(111):
         ts.match("intdcl")
    elif ts.peek() in p.predict(112):
         ts.match("floatdcl")
    elif ts.peek() in p.predict(113):
         ts.match("chardcl")
    else:
        print("Syntax Error in TypeSpec")
        sys.exit(0)

def Id(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Id:")
    print(f"{ts.peek()} and {p.predict(114)}")
    print(f"{ts.peek()} and {p.predict(115)}")
    if ts.peek() in p.predict(114):
         Literals(ts,p)
    elif ts.peek() in p.predict(115):
         ts.match("identifier")
    else:
        print("Syntax Error in Id")
        sys.exit(0)

def AddOp(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for AddOp:")
    print(f"{ts.peek()} and {p.predict(119)}")
    print(f"{ts.peek()} and {p.predict(120)}")
    if ts.peek() in p.predict(119):
         ts.match("plus")
    elif ts.peek() in p.predict(120):
         ts.match("minus")
    else:
        print("Syntax Error in AddOp")
        sys.exit(0)

def MultOp(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for MultOp:")
    print(f"{ts.peek()} and {p.predict(121)}")
    print(f"{ts.peek()} and {p.predict(122)}")
    if ts.peek() in p.predict(121):
         ts.match("mult")
    elif ts.peek() in p.predict(122):
         ts.match("div")
    else:
        print("Syntax Error in MultOp")
        sys.exit(0)

def LopNeg(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for LopNeg:")
    print(f"{ts.peek()} and {p.predict(123)}")
    if ts.peek() in p.predict(123):
         ts.match("not")
    else:
        print("Syntax Error in LopNeg")
        sys.exit(0)

def ConnecOp(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for ConnecOp:")
    print(f"{ts.peek()} and {p.predict(124)}")
    print(f"{ts.peek()} and {p.predict(125)}")
    if ts.peek() in p.predict(124):
         ts.match("or")
    elif ts.peek() in p.predict(125):
         ts.match("and")
    else:
        print("Syntax Error in ConnecOp")
        sys.exit(0)

def CompOp(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for CompOp:")
    print(f"{ts.peek()} and {p.predict(126)}")
    print(f"{ts.peek()} and {p.predict(127)}")
    print(f"{ts.peek()} and {p.predict(128)}")
    print(f"{ts.peek()} and {p.predict(129)}")
    print(f"{ts.peek()} and {p.predict(130)}")
    print(f"{ts.peek()} and {p.predict(131)}")
    if ts.peek() in p.predict(126):
         ts.match("equal")
    elif ts.peek() in p.predict(127):
         ts.match("biggerthan")
    elif ts.peek() in p.predict(128):
         ts.match("smallerthan")
    elif ts.peek() in p.predict(129):
         ts.match("biggerequal")
    elif ts.peek() in p.predict(130):
         ts.match("smallerequal")
    elif ts.peek() in p.predict(131):
         ts.match("diff")
    else:
        print("Syntax Error in CompOp")
        sys.exit(0)

def Print(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Print:")
    print(f"{ts.peek()} and {p.predict(108)}")
    if ts.peek() in p.predict(108):
         ts.match("printf")
         ts.match("openpara")
         Id(ts,p)
         ts.match("closepara")
    else:
        print("Syntax Error in Print")
        sys.exit(0)

def Literals(ts:token_sequence, p:predict_algorithm) -> None:
    print("\nProductions for Literals:")
    print(f"{ts.peek()} and {p.predict(116)}")
    print(f"{ts.peek()} and {p.predict(117)}")
    print(f"{ts.peek()} and {p.predict(118)}")
    if ts.peek() in p.predict(116):
         ts.match("inum")
    elif ts.peek() in p.predict(117):
         ts.match("fnum")
    elif ts.peek() in p.predict(118):
         ts.match("cchar")
    else:
        print("Syntax Error in Literals")
        sys.exit(0)



if __name__ == '__main__':
    filepaths = ['logicop.c']
    for filepath in filepaths:
        tokens = lexical_analyzer('testcodes/' + filepath)
        ts = token_sequence(tokens) # type: ignore
        G = create_ac_grammar()
        p_alg = predict_algorithm(G)
        print(tokens)    
        print(is_ll1(G, p_alg))
        print_rec_desc.print_rec_desc(G, "output.txt")
        Program(ts, p_alg)
