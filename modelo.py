class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.likes += 1

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}")

atlanta = Serie('atlanta', 2018, 2)
print(f"Nome: {atlanta.nome} - Ano {atlanta.ano} - Temporadas {atlanta.temporadas} ")
