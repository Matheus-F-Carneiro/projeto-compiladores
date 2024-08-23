G.add_production('Program', ['FunctList', '$']) #62
G.add_production('FunctList', ['Func', 'FunctList']) #63
G.add_production('FunctList', []) #64
G.add_production('Func', ['TypeFunc', 'indentifier', 'openpara', 'closepara',
'openbracket', 'Stmts', 'closebracket']) #65
G.add_production('Stmts', ['Stmt', 'semicolon', 'Stmts']) #66
G.add_production('Stmts', []) #67
G.add_production('Stmt', ['SimpleStmt']) #68
G.add_production('Stmt', ['Conditional']) #69
G.add_production('Stmt', ['Loop']) #70
G.add_production('SimpStmt', ['VarDefine']) #71
G.add_production('SimpStmt', ['Assign']) #72
G.add_production('CondIf', ['if', 'openpara', 'Logic', 'closepara', 'openbracket', 
'Stmts', 'closebracket', 'CondElse', 'endif']) #73
G.add_production('CondElse', ['else', 'openbracket', 'Stmts', 'closebracket']) #74
G.add_production('CondElse', []) #75
G.add_production('Loop', ['while', 'openpara', 'Logic', 'closepara', 'openbracket', 
'Stmts', 'closebracket']) #76
G.add_production('VarDefine', ['TypeSpec', 'VarId']) #77
G.add_production('VarId', ['identifier']) #78
G.add_production('VarId', ['Assign']) #79
G.add_production('Assign', ['indentifier', 'assign', 'Math']) #80
G.add_production('Assign', ['indentifier', 'assign', 'Logic']) #81
G.add_production('Math', ['MathCont', 'MathAdd']) #82
G.add_production('MathAdd', ['AddOp', 'MathCont', 'MathAdd']) #83
G.add_production('MathAdd', []) #84
G.add_production('MathCont', ['MathPar', 'MathMult']) #85
G.add_production('MathMult', ['MultOp', 'MathPar', 'MathMult']) #86
G.add_production('MathMult', []) #87
G.add_production('MathPar', ['openpara', 'Math', 'closepara']) #88
G.add_production('MathPar', ['Id']) #89
G.add_production('Logic', ['openpara', 'Logic', 'closepara']) #90
G.add_production('Logic', ['LogicComp', 'LopConec', 'Logic']) #91
G.add_production('Logic', ['LopNeg', 'Logic']) #92
G.add_production('LogicComp', ['Id', 'LopComp', 'Id']) #93
G.add_production('TypeFunc', ['TypeSpec']) #94
G.add_production('TypeFunc', ['void']) #95
G.add_production('TypeSpec', ['int']) #96
G.add_production('TypeSpec', ['float']) #97
G.add_production('TypeSpec', ['char']) #98
G.add_production('Id', ['literals']) #99
G.add_production('Id', ['indentifier']) #100
G.add_production('AddOp', ['plus']) #101
G.add_production('AddOp', ['minus']) #102
G.add_production('MultOp', ['mult']) #103
G.add_production('MultOp', ['div']) #104
G.add_production('LopNeg', ['not']) #105
G.add_production('LopConec', ['or']) #106
G.add_production('LopConec', ['and']) #107
G.add_production('LopComp', ['assign']) #108
G.add_production('LopComp', ['biggerthan']) #109
G.add_production('LopComp', ['smallerthan']) #110
G.add_production('LopComp', ['biggerequal']) #111
G.add_production('LopComp', ['smallerequal']) #112
G.add_production('LopComp', ['diff']) #113