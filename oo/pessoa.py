class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=18):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):ote
        return 'Aperto de mão'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    araujo = Mutante(nome='Araujo')
    bruno = Homem(araujo, nome='Bruno')
    print(Pessoa.cumprimentar(bruno))
    print(id(bruno))
    print(bruno.cumprimentar())
    print(bruno.nome)
    print(bruno.idade)
    for filho in bruno.filhos:
        print(filho.nome)
    bruno.sobrenome = "Queiroz"
    del bruno.filhos
    bruno.olhos = 1
    del bruno.olhos
    print(bruno.__dict__)
    print(araujo.__dict__)
    print(Pessoa.olhos)
    print(bruno.olhos)
    print(araujo.olhos)
    print(id(Pessoa.olhos), id(bruno.olhos), id(araujo.olhos))
    print(Pessoa.metodo_estatico(), bruno.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), bruno.nome_e_atributos_de_classe())
    pessoa =Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa,Homem))
    print(isinstance(araujo,Pessoa))
    print(isinstance(araujo,Pessoa))
    print(araujo.olhos)
    print(bruno.cumprimentar())
    print(araujo.cumprimentar())