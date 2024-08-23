'Program' -> FunctList \$
'FunctList' -> Func FunctList
'FunctList' -> empty
'Func' -> TypeFunc indentifier ( ) { Stmts }
'Stmts' -> Stmt ; Stmts
'Stmts' -> empty
'Stmt' -> SimpleStmt
'Stmt' -> Conditional
'Stmt' -> Loop
'SimpStmt' -> VarDefine
'SimpStmt' -> Assign
'CondIf' -> if ( Logic ) { Stmts } CondElse endif
'CondElse' -> else { Stmts } 
'CondElse' -> empty
'Loop' -> while ( Logic ) { Stmts }
'VarDefine' -> TypeSpec VarId
'VarId' -> identifier
'VarId' -> Assign
'Assign' -> indentifier = Math
'Assign' -> indentifier = Logic
'Math'  -> MathCont MathAdd
'MathAdd' -> AddOp MathCont MathAdd
'MathAdd' -> empty
'MathCont'  -> MathPar MathMult
'MathMult' -> MultOp MathPar MathMult
'MathMult' -> empty
'MathPar'  -> ( Math )
'MathPar' -> Id    
'Logic' -> ( Logic )
'Logic' -> LogicComp LopConec Logic
'Logic' -> LopNeg Logic
'LogicComp' -> Id LopComp Id
'TypeFunc' -> TypeSpec
'TypeFunc' -> void
'TypeSpec' -> int
'TypeSpec' -> float
'TypeSpec' -> char
'Id' -> literals
'Id' -> indentifier
'AddOp' -> +
'AddOp' -> -
'MultOp' -> *
'MultOp' -> /
'LopNeg' -> !
'LopConec' -> ||
'LopConec' -> &&
'LopComp' -> ==
'LopComp' -> >
'LopComp' -> <
'LopComp' -> >=
'LopComp' -> <=
'LopComp' -> !=