"""
## 2 - Manipulação da pilha

Definição de funções que vão simplificar o controle dos elementos na pilha, controlando problemas que se encontrem durante o processamento ao manipular a pilha.
"""
# Adiciona um elemento ao final da pilha
def stack_push(stack, tipo, valor, indice):
	stack.append({'Tipo' : tipo, 'Valor' : valor, 'Endereco' : indice})

# Retira e retorna o último elemnto da pilha se existir algum
def stack_pop(stack, comando):
	if not stack:
		raise Exception("Antes do comando na linha " + comando['Endereco'] +
				  " a pilha não tem suficientes valores.")
	return stack.pop()

# Retorna o valor presente em um endereço da pilha
# (Se for relativo, deve receber a posição atual junto do offset desta posição)
# (Se for absoluto, recebe diretamente a posição que está sendo buscada, e offset 0.)
def stack_read(stack, comando, indice, offset):
	if not stack[indice+offset]:
		raise Exception("Comando na linha " + comando['Endereco'] + " chama uma posição na pilha não-existente.")
	return stack[indice+offset]

# Sobrepõe um elemento na pilha com um valor novo
# (Se for relativo, deve receber a posição atual junto do offset desta posição)
# (Se for absoluto, recebe diretamente a posição que está sendo buscada, e offset 0.)
def stack_store(stack, comando, tipo, valor, indice, offset):
	if not stack[indice+offset]:
		raise Exception("Comando na linha " + comando['Endereco'] + " chama uma posição na pilha não-existente.")
	stack[indice+offset] = {'Tipo' : tipo, 'Valor' : valor, 'Endereco' : indice+offset}