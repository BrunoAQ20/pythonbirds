class Pessoa:
    def __init__(self, *filhos, nome=None, idade=18):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    araujo = Pessoa(nome='Araújo')
    bruno = Pessoa(araujo, nome='Bruno')
    print(Pessoa.cumprimentar(bruno))
    print(id(bruno))
    print(bruno.cumprimentar())
    print(bruno.nome)
    print(bruno.idade)
    for filho in bruno.filhos:
        print(filho.nome)
    bruno.sobrenome = 'Queiroz'
    del bruno.filhos
    print(bruno.__dict__)
    print(araujo.__dict__)