class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plimplim")

    def parar(self):
        print(" Parando a bike")
        print("Bike parada")

    def correr(self):
        print("vrummmm")

    def get_cor(self):
        return self.cor


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", 'monark', 2000, 189)
b2.buzinar()
print(b2.cor)


class Foo:
    def hello(self): print(self.__class__.__name__.lower())

    class Bar(Foo):
        def hello(self): return super().hello() bar = Bar() bar.hello()
