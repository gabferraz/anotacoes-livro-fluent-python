# Parte I - Prologo
# Cap. 1: Implementando uma classe que representa um tipo numérico (vetor)
from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    # O método repr representa a forma que as instâncias de Vector serão representadas pelo console
    # Sem ele o console retorna a posição na memória da instância
    # OBS: O método __repr__ é diferente de __str__, __str__ é chamado pela função str() e deve retornar
    #      uma formatação para o usuário (algo legível para ser chamado em um print).
    #      Se __str__ não tiver implementado o Python irá tentar chamar __repr__ 
    def __repr__(self):
        # O argumento !r serve para obter a representação padrão dos atributos
        # Serve para deixar explicito que os argumentos são números e não strings
        return 'Vector({!r}, {!r})'.format(self.x, self.y)
    
    # Método chamado pela função abs(), retorna o tamanho do vetor
    def __abs__(self):
        return hypot(self.x, self.y)
    
    # Por padrão as classes feitas pelo usuário retornam True se __bool__ ou __len__ não estiverem
    # implementadas. bool() chama x.__bool__() e usa seu resultado, se __bool__ não tiver disponível
    # ele vai chamar __len__ e se o tamanho for maior que 0 vai retornar True, se não retorna False
    def __bool__(self):
        # Basicamente __bool__ retorna True se o vetor não for nulo e False caso contrário
        return bool(abs(self))
    
    # Os métodos add e mul mostram um exemplo simples dos operadores + e *
    # OBS: Em ambos os casos os operadores retornam um novo Vector, o Vector original não é alterado 
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    # OBS: Essa implementação de mul permite multiplicar um Vector por um número mas não permite 
    #      multiplicar um número por um Vector. Existe outros métodos especiais que resolvem isso
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
# Mais métodos especiais estão disponíveis em http://docs.python.org/3/reference/datamodel.html

if __name__ == '__main__':
    vec1 = Vector(3, 4)
    vec2 = Vector(15, 4)
    # Chama __repr__
    print(vec1)
    # Chama __abs__
    print(abs(vec1))
    # Chama __add__
    print(vec1 + vec2)
    # Chama __mul__
    print(vec2*6)
    # Chama __bool__
    print(bool(vec1))