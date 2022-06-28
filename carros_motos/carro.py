
class Carro():

  def __init__(self, modelo, cor, ano, hodometro = 150):

   self.modelo = modelo
   self.cor = cor
   self.ano = ano
   self.hodometro = hodometro



  def buzinar (self): #retorne uma string com a buzina do carro.
    return f"bi bi bi"

  def abrir_porta_malas(self): #retornar um valor verdadeiro.
    print("Portas Abrindo...")
    return True

  def dirigir(self):
    self.hodometro += self.hodometro

  def __str__(self):
    return f' O modelo {self.modelo} de cor {self.cor} do ano {self.ano} tem {self.hodometro} km rodados'


fusca = Carro("Fusca", "Amarelo", 1980, 10)
gol = Carro("Gol", "Prata", 2021, 25)

print(fusca)
print(fusca.buzinar())
print(fusca.abrir_porta_malas())
print(gol)
fusca.dirigir()
gol.dirigir()
print(f"{fusca.hodometro} km rodados")
print(f"{gol.hodometro} km rodados")
print(gol.buzinar())
print(gol.abrir_porta_malas())
