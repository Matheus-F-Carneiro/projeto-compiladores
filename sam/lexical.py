"""
## 1 - Analisador Léxico

A primeira parte deste programa busca tratar a leitura do programa em uma análise léxica para preparar à analise sintática já separando comandos de valores e de labels. Alem disso, verifica se há algum problema de comandos desconhecidos.

"""
import re

# Checa se for uma linha em branco
branco = re.compile(r"^\s*$")

# Checa se for um label
labels = re.compile(r"^\s*([A-Za-z]+)\:\s*$")

# ompila para casos de possíveis comandos sem valor especificado (ex: ADD, EQUAL)
comando_direto = re.compile(r"^\s*([A-Z]+)\s*$")

# Compila para casos de possíveis comandos com valor numérico inteiro (ex: PUSHIMM, ADDSP)
comando_valor_num = re.compile(r"^\s*([A-Z]+)\s*(\d+)\s*$")

# Compila para casos de possíveis comandos com Labels (ex:JUMP, JSR)
comando_valor_lab = re.compile(r"^\s*([A-Z]+)\s*([A-Za-z]+)\s*$")

# Compila para casos de possíveis comandos com Float (only PUSHIMMF)
comando_valor_float = re.compile(r"^\s*([A-Z]+)\s*(\d+\.\d+)\s*$")

# Compila para casos de possíveis comandos com Char (only PUSHIMMCH)
comando_valor_char = re.compile(r"^\s*([A-Z]+)\s*\'(.)\'\s*$")

# Cuida da parte léxica do programa
def ler_linha(linha, indice):

    # Linhas em branco não interferem no programa:
    if branco.fullmatch(linha):
        return False

    # Checagem se for label
    label = labels.fullmatch(linha)
    if label:
        return {'Nome' : label.group(1) , 'Tipo' : 'Label', 'Endereco' : indice}
    
    # Checagem se for uma função sem operando
    comando = comando_direto.fullmatch(linha)
    if comando:    
        if comando.group(1) in ['DUP', 'SWAP']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Stack Manipulation', 'Endereco' : indice}
        elif comando.group(1) in ['PUSHSP', 'PUSHFBR', 'POPSP', 'POPFBR']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Register Manipulation', 'Endereco' : indice}
        elif comando.group(1) in ['PUSHIND', 'STOREIND']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Absolute Store/Retrieve', 'Endereco' : indice}
        elif comando.group(1) in ['ADD', 'SUB', 'TIMES', 'DIV', 'MOD']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Integer Algebra', 'Endereco' : indice}
        elif comando.group(1) in ['ADDF', 'SUBF', 'TIMESF', 'DIVF']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Float Algebra', 'Endereco' : indice}
        elif comando.group(1) in ['AND', 'OR', 'NOR', 'NAND', 'XOR', 'NOT']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Logic', 'Endereco' : indice}
        elif comando.group(1) in ['CMP', 'GREATER', 'LESS', 'EQUAL', 'ISNIL', 'ISPOS', 'ISNEG']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Comparison', 'Endereco' : indice}
        elif comando.group(1) in ['JUMPIND', 'RST', 'JSRIND', 'SKIP']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Jumps', 'Endereco' : indice}
        elif comando.group(1) in ['LINK', 'UNLINK']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Stack Frame', 'Endereco' : indice}
        elif comando.group(1) in ['WRITE', 'WRITEF', 'WRITECH']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Input/Output', 'Endereco' : indice}
        elif comando.group(1) in ['STOP']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Program Control', 'Endereco' : indice}
        

        else:
            raise Exception("Comando na linha " + indice + " não reconhecido.")


    # Checagem se for uma função com operando Float
    comando = comando_valor_float.fullmatch(linha)
    if comando:
        if comando.group(1) in ['PUSHIMMF']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Stack Insertion',
                    'Endereco' : indice, 'Valor': float(comando.group(2))}
        else:
            raise Exception("Comando na linha " + indice + " não reconhecido.")


    # Checagem se for uma função com operando Char
    comando = comando_valor_char.fullmatch(linha)
    if comando:
        if comando.group(1) in ['PUSHIMMCH']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Stack Insertion',
                    'Endereco' : indice, 'Valor': comando.group(2)}
        else:
            raise Exception("Comando na linha " + indice + " não reconhecido.")
        
    # Checagem se for uma função com operando Integer
    comando = comando_valor_num.fullmatch(linha)
    if comando:
        if comando.group(1) in ['PUSHIMM', 'PUSHIMMF', 'PUSHIMMCH']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Stack Insertion',
                    'Endereco' : indice, 'Valor': int(comando.group(2))}
        elif comando.group(1) in ['ADDSP']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Stack/Heap Allocation',
            'Endereco' : indice, 'Valor': int(comando.group(2))}
        elif comando.group(1) in ['PUSHABS', 'STOREABS']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Absolute Store/Retrieve',
            'Endereco' : indice, 'Valor': int(comando.group(2))}
        elif comando.group(1) in ['PUSHOFF', 'STOREOFF']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Relative Store/Retrieve',
            'Endereco' : indice, 'Valor': int(comando.group(2))}
        elif comando.group(1) in ['JUMP', 'JUMPC', 'JSR']:
            return {'Nome' : comando.group(1), 'Tipo' : 'Jumps', 'Endereco' : indice,
                    'Tipo_operando' : 'Integer', 'Valor': int(comando.group(2))}

        else:
            raise Exception("Comando na linha " + indice + " não reconhecido.")

    # Checagem se for um comando com operando Label
    # (Único tipo de comando que recebe Label é Jumps)
    comando = comando_valor_lab.fullmatch(linha)
    if comando:
        jumps = ['JUMP', 'JUMPC', 'JSR']
        if comando.group(1) in jumps:
            return {'Nome:' : comando.group(1), 'Tipo' : 'Jumps', 'Endereco' : indice,
                    'Tipo_Operando' : 'Label', 'Valor' : comando.group(2)}
        raise Exception("Comando na linha " + indice + " não reconhecido.")

    # Ultimo caso
    raise Exception("Comando na linha " + indice + " não reconhecido.")