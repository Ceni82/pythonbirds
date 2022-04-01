class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=39):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    # @staticmathod
    # def metodo_estatico():
    #     return 42
    #
    # @classmathod
    # def nome_e_atributos_de_classe(cls):
    #     return f'{cls} - olhos {cls.olhos}'






if __name__ == '__main__':
    mateus = Pessoa(nome='Mateus')
    ceni = Pessoa(mateus, nome='Ceni')
    print(Pessoa.cumprimentar(mateus))
    print(id(mateus))
    print(mateus.cumprimentar())
    print(mateus.nome)
    print(mateus.idade)
    for filho in mateus.filhos:
        print(filho.nome)
    mateus.sobrenome = 'Thor'
    del mateus.filhos
    mateus.olhos = 1
    del mateus.olhos
    print(mateus.__dict__)
    print(ceni.__dict__)
    Pessoa.olhos= 3
    print(Pessoa.olhos)
    print(mateus.olhos)
    print(ceni.olhos)
    print(id(Pessoa.olhos), id(mateus.olhos), id(ceni.olhos))
    # print(Pessoa.metodo_estatico(), mateus.metodo_estatico))
    # print(Pessoa.nome_e_atributos_de_classe(), mateus.nome_e_atributos_de_classe())
