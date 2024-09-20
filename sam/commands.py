"""
## 3 - Comandos SaM

Definição das funções que serão usadas para executar cada comando SaM, checando durante a etapa de processamento se há algum problema.
"""

import math

from stack import *

def stack_manip(comando, stack, sp):
    if comando['Nome'] == 'DUP':
        value_dupped = stack_read(stack, comando, sp, -1)
        stack_push(stack, value_dupped['Valor'], value_dupped['Tipo'], sp)
        sp += 1
    elif comando['Nome'] == 'SWAP':
        temp1 = stack_pop(stack, comando)
        sp -= 1
        temp2 = stack_pop(stack, comando)
        sp -= 1
        stack_push(stack, temp1['Tipo'], temp1['Valor'], sp)
        sp += 1
        stack_push(stack, temp2['Tipo'], temp2['Valor'], sp)
        sp += 1

    else:
        raise Exception("Erro Fatal: Algo de errado com a função stack_manip, revisar o código")

    return sp

def regist_manip(comando, fbr, stack, sp):
    if comando['Nome'] == 'PUSHSP':
        stack_push(stack, 'M', sp, sp)
        sp += 1

    elif comando['Nome'] == 'PUSHFBR':
        stack_push(stack, 'M', fbr, sp)
        sp += 1

    elif comando['Nome'] == 'POPSP':
        novo_sp = stack_pop(stack, comando)
        sp = novo_sp['Valor']

    elif comando['Nome'] == 'POPFBR':
        novo_fbr = stack_pop(stack, comando)
        sp -= 1
        fbr = novo_fbr['Valor']

    else:
        raise Exception("Erro Fatal: Algo de errado com a função regist_manip, revisar o código")

    return fbr, sp

def absol_st_ret(comando, stack, sp):
    if comando['Nome'] == 'PUSHIND':
        mem_address = stack_pop(stack, comando)
        sp -= 1
        data_push = stack_read(stack, comando, mem_address['Valor'], 0)
        stack_push(stack, data_push['Tipo'], data_push['Valor'], sp)
        sp += 1

    elif comando['Nome'] == 'STOREIND':
        value_store = stack_pop(stack, comando)
        sp -= 1
        mem_address = stack_pop(stack, comando)
        sp -= 1
        stack_store(stack, comando, value_store['Tipo'], value_store['Valor'], mem_address['Valor'], 0)
        sp += 1

    elif comando['Nome'] == 'PUSHABS':
        find_value = stack_read(stack, comando, comando['Valor'], 0)
        stack_push(stack, find_value['Tipo'], find_value['Valor'], sp)
        sp += 1

    elif comando['Nome'] == 'STOREABS':
        value_store = stack_pop(stack, comando)
        sp -= 1
        stack_store(stack, comando, value_store['Tipo'], value_store['Valor'], comando['Valor'], 0)

    else:
        raise Exception("Erro Fatal: Algo de errado com a função absol_st_ret, revisar o código")

    return sp

def rel_st_ret(comando, fbr, stack, sp):
    if comando['Nome'] == 'PUSHOFF':
        find_value = stack_read(stack, comando, fbr, comando['valor'])
        stack_push(stack, find_value['Tipo'], find_value['Valor'], sp)
        sp += 1

    elif comando['Nome'] == 'STOREOFF':
        value_store = stack_pop(stack, comando)
        stack_store(stack, comando, value_store['Tipo'], value_store['Valor'], fbr, comando['Valor'])
        sp -=1

    else:
        raise Exception("Erro Fatal: Algo de errado com a função rel_st_ret, revisar o código")

    return sp

def stack_insert(comando, stack, sp):
    if comando['Nome'] == 'PUSHIMM':
        stack_push(stack, 'I', comando['Valor'], sp)
        sp += 1

    elif comando['Nome'] == 'PUSHIMMF':
        stack_push(stack, 'F', comando['Valor'], sp)
        sp += 1
    
    elif comando['Nome'] == 'PUSHIMMCH':
        stack_push(stack, 'C', comando['Valor'], sp)
        sp += 1

    else:
        raise Exception("Erro Fatal: Algo de errado com a função stack_insert, revisar o código")

    return sp

def stk_heap_alloc(comando, stack, sp):
    if comando['Nome'] == 'ADDSP':
        if comando['Valor'] >= 0:
            for i in range(comando['Valor']):
                stack_push(stack, 'M', 0, sp)
                sp += 1

        if comando['Valor'] < 0:
            for i in range(0, comando['Valor'], -1):
                stack_pop(stack, comando)
                sp-=1

    else:
        raise Exception("Erro Fatal: Algo de errado com a função stk_heap_alloc, revisar o código")

    return sp

def integ_algebra(comando, stack, sp):
    if comando['Nome'] == 'ADD':
        valor1 = stack_pop(stack, comando)
        valor2 = stack_pop(stack, comando)
        if valor1['Tipo'] == 'I' and valor2['Tipo'] == 'I':
            sp -= 2
            total = valor1['Valor'] + valor2['Valor']
            stack_push(stack, 'I', total, sp)
            sp += 1
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "Integer Algebra para não-inteiros.")
        

    elif comando['Nome'] == 'SUB':
        valor1 = stack_pop(stack, comando)
        valor2 = stack_pop(stack, comando)
        if valor1['Tipo'] == 'I' and valor2['Tipo'] == 'I':
            sp -= 2
            total = valor1['Valor'] - valor2['Valor']
            stack_push(stack, 'I', total, sp)
            sp += 1
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "Integer Algebra para não-inteiros.")

    elif comando['Nome'] == 'TIMES':
        valor1 = stack_pop(stack, comando)
        valor2 = stack_pop(stack, comando)
        if valor1['Tipo'] == 'I' and valor2['Tipo'] == 'I':
            sp -= 2
            total = valor1['Valor'] * valor2['Valor']
            stack_push(stack, 'I', total, sp)
            sp += 1
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "Integer Algebra para não-inteiros.")

    elif comando['Nome'] == 'DIV':
        valor1 = stack_pop(stack, comando)
        valor2 = stack_pop(stack, comando)
        if valor1['Tipo'] == 'I' and valor2['Tipo'] == 'I':
            sp -= 2
            if valor1['Valor'] == 0:
                raise Exception("Na linha " + comando['Endereco'] + " não podemos dividir por 0.")
            total = valor2['Valor'] / valor1['Valor']
            total = int(math.trunc(total))
            stack_push(stack, 'I', total, sp)
            sp += 1
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "Integer Algebra para não-inteiros.")
        

    elif comando['Nome'] == 'MOD':
        valor1 = stack_pop(stack, comando)
        valor2 = stack_pop(stack, comando)
        if valor1['Tipo'] == 'I' and valor2['Tipo'] == 'I':
            sp -= 2
            if valor1['Valor'] == 0:
                raise Exception("Na linha " + comando['Endereco'] + " não podemos dividir por 0.")
            total = valor2['Valor'] % valor1['Valor']
            total = int(math.trunc(total))
            stack_push(stack, 'I', total, sp)
            sp += 1
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "Integer Algebra para não-inteiros.")

    else:
        raise Exception("Erro Fatal: Algo de errado com a função integ_algebra, revisar o código.")

    return sp

def float_algebra(comando, stack, sp):
    if comando['Nome'] == 'ADDF':
        valor1 = stack_pop(stack, comando)
        valor2 = stack_pop(stack, comando)
        if valor1['Tipo'] == 'F' and valor2['Tipo'] == 'F':
            sp -= 2
            total = valor1['Valor'] + valor2['Valor']
            stack_push(stack, 'F', total, sp)
            sp += 1
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "Float Algebra para não-floats.")
        

    elif comando['Nome'] == 'SUBF':
        valor1 = stack_pop(stack, comando)
        valor2 = stack_pop(stack, comando)
        if valor1['Tipo'] == 'F' and valor2['Tipo'] == 'F':
            sp -= 2
            total = valor1['Valor'] - valor2['Valor']
            stack_push(stack, 'F', total, sp)
            sp += 1
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "Float Algebra para não-floats.")

    elif comando['Nome'] == 'TIMESF':
        valor1 = stack_pop(stack, comando)
        valor2 = stack_pop(stack, comando)
        if valor1['Tipo'] == 'F' and valor2['Tipo'] == 'F':
            sp -= 2
            total = valor1['Valor'] * valor2['Valor']
            stack_push(stack, 'F', total, sp)
            sp += 1
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "Float Algebra para não-floats.")

    elif comando['Nome'] == 'DIVF':
        valor1 = stack_pop(stack, comando)
        valor2 = stack_pop(stack, comando)
        if valor1['Tipo'] == 'F' and valor2['Tipo'] == 'F':
            sp -= 2
            if valor1['Valor'] == 0:
                raise Exception("Na linha " + comando['Endereco'] + " não podemos dividir por 0.")
            total = valor2['Valor'] / valor1['Valor']
            total = int(math.trunc(total))
            stack_push(stack, 'F', total, sp)
            sp += 1
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "Float Algebra para não-floats.")
    

    else:
        raise Exception("Erro Fatal: Algo de errado com a função float_algebra, revisar o código.")

    return sp

def comparison(comando, stack, sp):
    if comando['Nome'] == 'CMP':
        valor1 = stack_pop(stack, comando)['Valor']
        valor2 = stack_pop(stack, comando)['Valor']
        sp -= 2
        if valor1 > valor2:
            stack_push(stack, 'I', 1, sp)
        elif valor1 < valor2:
            stack_push(stack, 'I', -1, sp)
        else:
            stack_push(stack, 'I', 0, sp)
        sp+= 1

    elif comando['Nome'] == 'GREATER':
        valor1 = stack_pop(stack, comando)['Valor']
        valor2 = stack_pop(stack, comando)['Valor']
        sp -= 2
        if valor2 > valor1:
            stack_push(stack, 'I', 1, sp)
        else:
            stack_push(stack, 'I', 0, sp)
        sp+=1

    elif comando['Nome'] == 'LESS':
        valor1 = stack_pop(stack, comando)['Valor']
        valor2 = stack_pop(stack, comando)['Valor']
        sp -= 2
        if valor2 < valor1:
            stack_push(stack, 'I', 1, sp)
        else:
            stack_push(stack, 'I', 0, sp)
        sp+=1

    elif comando['Nome'] == 'EQUAL':
        valor1 = stack_pop(stack, comando)['Valor']
        valor2 = stack_pop(stack, comando)['Valor']
        sp -= 2
        if valor2 == valor1:
            stack_push(stack, 'I', 1, sp)
        else:
            stack_push(stack, 'I', 0, sp)
        sp+=1

    elif comando['Nome'] == 'ISNIL':
        valor = stack_pop(stack, comando)['Valor']
        sp -= 1
        if valor == 0:
            stack_push(stack, 'I', 1, sp)
        else:
            stack_push(stack, 'I', 0, sp)
        sp += 1

    elif comando['Nome'] == 'ISPOS':
        valor = stack_pop(stack, comando)['Valor']
        sp -= 1
        if valor > 0:
            stack_push(stack, 'I', 1, sp)
        else:
            stack_push(stack, 'I', 0, sp)
        sp += 1

    elif comando['Nome'] == 'ISNEG':
        valor = stack_pop(stack, comando)['Valor']
        sp -= 1
        if valor < 0:
            stack_push(stack, 'I', 1, sp)
        else:
            stack_push(stack, 'I', 0, sp)
        sp += 1

    else:
        raise Exception("Erro Fatal: Algo de errado com a função comparison, revisar o código.")

    return sp

def logic(comando, stack, sp):
    if comando['Nome'] == 'AND':
        valor1 = stack_pop(stack, comando)['Valor']
        valor2 = stack_pop(stack, comando)['Valor']
        sp-=2
        if valor1 != 0 and valor2 != 0:
            stack_push(stack, 'I', 1, sp)
        else:
            stack_push(stack, 'I', 0, sp)
        sp+=1

    elif comando['Nome'] == 'OR':
        valor1 = stack_pop(stack, comando)['Valor']
        valor2 = stack_pop(stack, comando)['Valor']
        sp-=2
        if valor1 != 0 or valor2 != 0:
            stack_push(stack, 'I', 1, sp)
        else:
            stack_push(stack, 'I', 0, sp)
        sp+=1

    elif comando['Nome'] == 'NOR':
        valor1 = stack_pop(stack, comando)['Valor']
        valor2 = stack_pop(stack, comando)['Valor']
        sp-=2
        if valor1 != 0 or valor2 != 0:
            stack_push(stack, 'I', 0, sp)
        else:
            stack_push(stack, 'I', 1, sp)
        sp+=1

    elif comando['Nome'] == 'NAND':
        valor1 = stack_pop(stack, comando)['Valor']
        valor2 = stack_pop(stack, comando)['Valor']
        sp-=2
        if valor1 != 0 and valor2 != 0:
            stack_push(stack, 'I', 0, sp)
        else:
            stack_push(stack, 'I', 1, sp)
        sp+=1

    elif comando['Nome'] == 'XOR':
        valor1 = stack_pop(stack, comando)['Valor']
        valor2 = stack_pop(stack, comando)['Valor']
        sp-=2
        if valor1 != 0 ^ valor2 != 0:
            stack_push(stack, 'I', 1, sp)
        else:
            stack_push(stack, 'I', 0, sp)
        sp+=1


    elif comando['Nome'] == 'NOT':
        valor = stack_pop(stack, comando)['Valor']
        sp-=1
        if valor != 0:
            stack_push(stack, 'I', 0, sp)
        else:
            stack_push(stack, 'I', 1, sp)
        sp+=1

    else:
        raise Exception("Erro Fatal: Algo de errado com a função logic, revisar o código.")

    return sp

def jump(comando, label_transl, fbr, stack, sp):
    if comando['Nome'] == 'JUMP':
        if isinstance(comando['Valor'], str):
            fbr = label_transl[comando['Valor']]
        else:
            fbr = comando['Valor']
    elif comando['Nome'] == 'JUMPC':
        valor = stack_pop(stack, comando)['Valor']
        if valor == 0:
            if isinstance(comando['Valor'], str):
                fbr = label_transl[comando['Valor']]
            else:
                fbr = comando['Valor']
    elif comando['Nome'] == 'JUMPIND':
        jumpTo = stack_pop(stack, comando)['Valor']
        fbr = jumpTo
    elif comando['Nome'] == 'RST':
        jumpTo = stack_pop(stack, comando)['Valor']
        sp -= 1
        fbr = jumpTo
    elif comando['Nome'] == 'JSR':
        if isinstance(comando['Valor'], str):
            fbr = label_transl[comando['Valor']]
        else:
            fbr = comando['Valor']
        stack_push(stack, 'I', fbr+1, sp)
        sp += 1
    elif comando['Nome'] == 'JSRIND':
        jumpTo = stack_pop(stack, comando)['Valor']
        sp -= 1
        fbr = jumpTo
        stack_push(stack, 'I', fbr+1, sp)
        sp += 1
    elif comando['Nome'] == 'SKIP':
        skipTo = stack_pop(stack, comando)['Valor']
        fbr += skipTo

    else:
        raise Exception("Erro Fatal: Algo de errado com a função jump, revisar o código.")

    return fbr, sp

def stack_frame(comando, fbr, stack, sp):
    if comando['Nome'] == 'LINK':
        stack_push(stack, 'I', fbr, sp)
        sp += 1
        fbr = sp - 1
    elif comando['Nome'] == 'UNLINK':
        fbr = stack_pop(stack, comando)['Valor']
        sp -= 1
    else:
        raise Exception("Erro Fatal: Algo de errado com a função stack_frame, revisar o código.")
    return sp

def input_output(comando, stack, sp):
    if comando['Nome'] == 'WRITE':
        print_target = stack_pop(stack, comando)['Valor']
        sp -= 1
        if print_target['Tipo'] == 'I':
            print(print_target)
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "WRITE para não-integers.")
    if comando['Nome'] == 'WRITEF':
        print_target = stack_pop(stack, comando)['Valor']
        sp -= 1
        if print_target['Tipo'] == 'F':
            print(print_target)
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "WRITEF para não-floats.")
    if comando['Nome'] == 'WRITECH':
        print_target = stack_pop(stack, comando)['Valor']
        sp -= 1
        if print_target['Tipo'] == 'C':
            print(print_target)
        else:
            raise Exception ("Na linha " + comando['Endereco'] + " não podemos aplicar" +
                             "WRITECH para não-characters.")
    
    else:
        raise Exception("Erro Fatal: Algo de errado com a função logic, revisar o código.")
    return sp


def detect_comando(programa, label_transl, fbr, stack, sp, halt):
    if programa[fbr]['Tipo'] == 'Stack Manipulation':
        sp = stack_manip(programa[fbr], stack, sp)
    elif programa[fbr]['Tipo'] == 'Register Manipulation':
        fbr, sp = regist_manip(programa[fbr], fbr, stack, sp)
    elif programa[fbr]['Tipo'] == 'Absolute Store/Retrieve':
        sp = absol_st_ret(programa[fbr], stack, sp)
    elif programa[fbr]['Tipo'] == 'Relative Store/Retrieve':
        sp = rel_st_ret(programa[fbr], fbr, stack, sp)
    elif programa[fbr]['Tipo'] == 'Stack Insertion':
        sp = stack_insert(programa[fbr], stack, sp)
    elif programa[fbr]['Tipo'] == 'Stack/Heap Allocation':
        sp = stk_heap_alloc(programa[fbr], stack, sp)
    elif programa[fbr]['Tipo'] == 'Integer Algebra':
        sp = integ_algebra(programa[fbr], stack, sp)
    elif programa[fbr]['Tipo'] == 'Float Algebra':
        sp = float_algebra(programa[fbr], stack, sp)
    elif programa[fbr]['Tipo'] == 'Comparison':
        sp = comparison(programa[fbr], stack, sp)
    elif programa[fbr]['Tipo'] == 'Logic':
        sp = logic(programa[fbr], stack, sp)
    elif programa[fbr]['Tipo'] == 'Jumps':
        fbr, sp = jump(programa[fbr], label_transl, fbr, stack, sp)
    elif programa[fbr]['Tipo'] == 'Stack Frames':
        sp = stack_frame(programa[fbr], fbr, stack, sp)
    elif programa[fbr]['Tipo'] == 'Input/Output':
        sp = input_output(programa[fbr], stack, sp)
    
    return fbr, sp, halt
