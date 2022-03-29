class Pessoa:
    def __init__(self, nome = None, idade=39):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa("Ceni")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Mateus'
    print(p.nome)
    print(p.idade)