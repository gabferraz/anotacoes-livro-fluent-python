# Part 2 - Data Structures
# Cap. 2: 

# LIST COMPREHENSIONS
# Listcomps só devem ser utilizadas para gerar uma lista, se for necessario fazer algum processamento de dados
# ou executar um código varias vezes o recomendado é utilizar o loop for. Listcomp não substitui o for.

# Exemplo: Criando uma lista de todos os modelos de camisa possíveis
cores = ['preto', 'branco']
tamanhos = ['G', 'M', 'P']

# Essa linha gera uma lista de tuplas organizadas por cores e depois tamanhos
# É o mesmo resultado de dois for aninhados na mesma ordem da listcomp
camisas = [(cor, tamanho) for cor in cores 
                          for tamanho in tamanhos]
print(camisas)

# GENERATOR EXPRESSIONS
# Genexp serve para preencher outros tipos de sequencers tirando listas.
# É melhor do que usar listcomp para preencher outros sequencers pois utiliza menos memória.

# O mesmo exemplo de cima só que utilizando genexp e sem construir os modelos na memória
for camisa in (f'{cor} {tamanho}' for cor in cores for tamanho in tamanhos):
    print(camisa)
    
# TUPLE
# Tuplas tem duas funções: Servem como listas imutáveis ou como um conjunto de campos sem nomes
# Quando se utiliza tuplas como um conjunto de campos o número de campos e sua ordem é importante
# Por exemplo:
id_viajantes = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA2058268')]
for passaporte in sorted(id_viajantes):
    print('%s/%s' % passaporte)
    
# Um dos motivos da tupla funcionar bem como um conjunto de campos é a capacidade de unpacking
# Podemos "desempacotar" a tupla em variáveis e iteráveis
# Por exemplo:
# \-> Desempacotação paralela: Os valores da tupla são distribuidos para as variáveis
cidade, ano, populacao, area = ('Tokyo', 2003, '32450', '8014')

# \-> Prefixo *: Em uma operação que recebe mais de um parâmetro você pode desempacotar a tupla com *
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))

# \-> Retorno de multiplas variáveis: No exemplo anterior a função divmod retorna dois valores utilizando
#     tuplas que pode ser desempacotada em variáveis diferentes
quociente, resto = divmod(*t)
print(f'{quociente} {resto}')

# \-> Prefixo * para pegar excesso: Na definição de uma função * pode ser utilizado para pegar argumentos
#     em excesso. Isso também funciona para desempacotação paralela
a, b, *resto = range(6)
print(f'{a}, {b}, {resto}')

# \-> Desempacotamento de tupla aninhada: Se a tupla que for desempacotada tiver uma tupla aninhada
#     o Python vai realizar o desempacotamento correto se a expressão combinar com a estrutura da tupla
dados_metro = [
    ('Tokyo', 'JP', 36.9, (35.689722, 139.691778)),
    ('Delhi NCR', 'IN', 21.9, (28.613888, 77.208889)),
    ('Mexico City', 'MX', 20.1, (19.433333, -99.133333)),
    ('Sao Paulo', 'BR', 19.7, (-23.547777, -46.635833)),
]
fmt = '{:15} | {:9.4f} | {:9.4f}'
for nome, pais, populacao, (latitude, longitude) in dados_metro:
    if longitude <= 0:
        print(fmt.format(nome, latitude, longitude))
        
# NAMED TUPLE
# Umas das desvantagens da tupla como um conjunto de campos é a falta de um label
# Named tuples resolve esse problema
from collections import namedtuple

# namedtuple recebe dois parâmetros: nome da classe e um iterável de strings ou uma string
# com os nomes dos atributos separados por espaço
Cidade = namedtuple('Cidade', 'nome pais populacao coordenadas')
tokyo = Cidade('Tokyo', 'JP', 36.933, (35.689722, 139.691677))
print(tokyo)
print(tokyo.populacao)
print(tokyo[3])

# OBS: Tuplas como lista imutáveis:
#      Tuplas possuem todas as funções de lista que não envolvem adicionar ou remover itens
#      com exceção do método __reversed__ por motivos de otimização

# SLICING
# É possível fazer slices com pulos (stride) com a chamada s[começo:fim:stride]. Por exemplo:
s = 'bicicleta'
print(s[::3])
print(s[::-2])

# Também é possível armazenar slices como objeto, que pode ser interessante para processar
# arquivos de texto puro por exemplo
comprovante = """
1909 Chave de fenda R$5.50  3  R$16.50
4052 Chave estrela  R$4.30  2  R$8.60
5942 Corda sisal 1m R$1.20  5  R$6.00
"""
CODIGO = slice(0, 4)
DESCRICAO = slice(4, 19)
PRECO_UNIDADE = slice(19, 27)
QUANTIDADE = slice(27, 31)
PRECO_TOTAL = slice(31, None)

linha_items = comprovante.split('\n')[1:]
for item in linha_items:
    print(item[PRECO_TOTAL], item[DESCRICAO]) 
    
# Slices também podem ser utilizados para modificar a região de uma sequência
l = list(range(10))
print(l)
del l[2:6]
print(l)
l[3:5] = [11, 11, 11]
print(l)

# Usando + e * com sequências:
# Os operadores + e * suportam sequências, para isso ambos os operandos tem que ser do mesmo tipo
# Esses operadores nunca modificam a sequência, eles sempre retornam uma nova sequência

# OBS: Cuidado com expressões tipo a * n se a for uma sequência que contém elementos mutáveis.
#      O problema é que os resultados dessa expressão pode ser diferentes do esperado. Por exemplo
#      se a = [[]] então a * 3 vai resultar numa lista com 3 referências para a mesma lista interior

# OBS: O melhor meio de contruir listas de multiplas dimensões é utilizando listcomp. 
#      Podemos ver nesse exemplo que o campo é modificado do jeito esperado
tabuleiro = [['_'] * 3 for i in range(3)]
tabuleiro[1][2] = 'X'
print(tabuleiro)
#      Utilizar o operador * é errado pois acaba criando referências para as listas aninhadas
#      nesse caso todos os elementos da lista representam a mesma lista
errado = [['_'] * 3] * 3
errado[1][2] = 'O'
print(errado)

# Operadores += e *= com sequências
# O comportamento desses operadores vão depender se a sequência é imutável ou não
# se a sequência for imutável um novo objeto será criado e associado ao nome da
# variável original. Logo não é recomendado realizar concatenações repetidas em
# sequência imutáveis utilizando esses valores pois é ineficiente.

# OBS: Algumas dicas importantes:
#      -Não é uma boa ideia colocar elementos mutáveis dentro de elementos imutáveis
#      -As operações *=, +=, etc não são atômicas

# list.sort vs sorted()
# O método list.sort altera o objeto enquanto a função sorted() retorna um novo objeto
# list.sort retorna None no final que é uma convenção do Python que indica que o método
# altera o objeto

