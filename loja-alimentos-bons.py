# classe base

#new
class Produto :
    def __init__(self, nome: str, cod: int, valor: float, qtd: int ):
        self.nome = nome
        self.cod = cod
        self.valor = valor
        self.qtn = qtd

    def exibirinfo(self):
        return (f'nome: {self.nome} | código: {self.cod} | valor: R${self.valor} | quantidade: {self.qtn}')

    def add(self, qtd: int = 1):
        self.qtn = self.qtn + qtd

    def remover(self, qtd: int = 1):
        self.qtn = self.qtn - qtd


class Alimento(Produto):
    def __init__(self, nome: str, cod: int, valor: float, qtd: int, validade, peso):
        super().__init__(nome, cod, valor, qtd)
        self.__validade = validade
        self.__peso = peso

    def exibirinfo(self):
        return (f'nome: {self.nome} | código: {self.cod} | valor: R${self.valor} | quantidade: {self.qtn} | peso(unitário): {self.__peso} | validade: {self.__validade}')


class Bebida(Produto):
    def __init__(self, nome: str, cod: int, valor: float, qtd: int, alcoolica: bool, ml: int):
        '''Cria um objeto da classe Bebida. Deverá ser passado um booleano para o atributo alcoolica. True indica que é uma bebida alcoolica e False indica que não é.'''
        super().__init__(nome,cod,valor,qtd)
        self.__alcoolica = alcoolica
        self.__ml = ml

    def exibirInfo(self):
        return (f'Nome: {self.nome} | Código: {self.cod} | Valor: R${self.valor} | Quantidade: {self.qtd} | Peso(unitário): {self.peso} | Validade: {self.validade}')


class Estoque:
    def __init__(self, listaprodutos = []):
        self.__listaprodutos = listaprodutos

    def addlista(self, produto):
        self.__listaprodutos.append(produto)

    def remove(self, codproduto):
        for produto in self.__listaprodutos:
            if codproduto == produto.cod:
                self.__listaprodutos.remove(produto)

    def exibirdisponiveil(self):
        for produto in self.__listaprodutos:
            if produto.qtn >= 1:
                print(produto.exibirinfo())

    def exibirindisponiveil(self):
        for produto in self.__listaprodutos:
            if produto.qtn <= 0:
                print(produto.exibirinfo())

    def all(self):
        for produto in self.__listaprodutos:
            print(produto.exibirinfo())





al1 = Alimento(nome="Arroz", cod=1, valor=20.50, qtd=50, validade=(2025, 1, 10), peso="1kg")
al2 = Alimento(nome="Feijão", cod=2, valor=8.70, qtd=40, validade=(2024, 12, 15), peso="1kg")
al3 = Alimento(nome="Macarrão", cod=3, valor=5.30, qtd=60, validade=(2025, 6, 20), peso="500g")
al4 = Alimento(nome="Açúcar", cod=4, valor=3.20, qtd=100, validade=(2026, 2, 25), peso="1kg")
al5 = Alimento(nome="Farinha de Trigo", cod=5, valor=4.50, qtd=30, validade=(2024, 11, 5), peso="1kg")

beb1 = Bebida(nome="Água Mineral", cod=6, valor=2.00, qtd=200, alcoolica=False, ml=500)
beb2 = Bebida(nome="Refrigerante", cod=7, valor=6.00, qtd=150, alcoolica=False, ml=2000)
beb3 = Bebida(nome="Cerveja", cod=8, valor=4.50, qtd=300, alcoolica=True, ml=350)
beb4 = Bebida(nome="Vinho", cod=9, valor=25.00, qtd=80, alcoolica=True, ml=750)
beb5 = Bebida(nome="Suco de Laranja", cod=10, valor=7.50, qtd=120, alcoolica=False, ml=1000)

estoque = Estoque()

estoque.addlista(al1)
estoque.addlista(al2)
estoque.addlista(al3)
estoque.addlista(al4)
estoque.addlista(al5)

estoque.addlista(beb1)
estoque.addlista(beb2)
estoque.addlista(beb3)
estoque.addlista(beb4)
estoque.addlista(beb5)





estoque.all()
print('='*30)


