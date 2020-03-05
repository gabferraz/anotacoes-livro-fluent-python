# Parte I - Prologo
# Cap. 1: Deck de cartas pythonico, introdução a métodos especiais e a estrutura de dados
#         do Python
import collections

# collections.namedtuple pode ser utilizado para construir
# uma classe simples que apenas possuem um conjunto de atributos
# sem nenhum método definido pelo usuário
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    # gera uma lista ['2', '3', '4', ..., '11', 'J', 'Q', 'K', 'A']
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # gera uma lista ['spades', 'diamonds', 'clubs', 'hearts']
    suits = 'spades diamonds clubs hearts'.split()
    
    # essa classe apenas utiliza métodos especiais do Python para
    # processar seus atributos em vez de métodos customizados
    def __init__(self):
        # semelhante a um for aninhado, cria uma lista de cartas passando os valores das listas
        # ranks e suits para os campos da namedtuple
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
if __name__ == "__main__":
    # namedtuple pode ser utilizada para criar representações mais legíveis de dados. Por exemplo:
    carta = Card('7', 'diamonds')
    print(carta)
    
    deck = FrenchDeck()
    # A vantagem de utilizar métodos especiais é que o objeto passa a ser compatível com a biblioteca
    # padrão do Python. Que tem como beneficios:
    # 1- Não é necessario definir nomes arbitrários como .retornaCarta() ou .tamanhoDoBaralho()
    print(len(deck))
    print(deck[0])
    print(deck[-1])
    
    # 2- O objeto é compatível com a biblioteca padrão do Python. 
    #   \-> Por exemplo podemos usar choice para buscar uma carta aleatória do baralho em vez de criar um método para isso
    from random import choice
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    #   \-> Como __getitem__ referencia o operador [] de _cards o deck automaticamente suporta slicing
    print(deck[:3])
    print(deck[49:])
    print(deck[12::15])
    #   \-> Por causa do __getitem__ o objeto também passa a ser iterável e também pode ser revertido
    for card in deck:
        print(card)    
    for card in reversed(deck):
        print(card)
    #   OBS: Iteração geralmente é implicita. Se um collection não possui um método __contains__
    #        o operador in faz uma busca sequencial, tanto que a classe FrechDeck é compatível
    #        com o operador porque ela é iterável
    print(Card('2', 'hearts') in deck)
    print(Card('M', 'coisa') in deck)
    #   OBS: FrenchDeck herda implicitamente da classe object mas as funcionalidades não são
    #        herdadas implicitamente. Implementando os métodos especiais __getitem e __len__
    #        o objeto passa a se comportar como uma sequence padrão do Python