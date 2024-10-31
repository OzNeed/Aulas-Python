# def dobro (num):
#   dobro = num * 2
#   print(f"O dobro de {num} é {dobro}")


# def triplo (num):
#   triplo = num * 3
#   print(f"O triplo de {num} é {triplo}")


# def quadruplo(num):
#   quadruplo = num * 4
#   print(f"O quadruplo de {num} é {quadruplo}")


# num = int(input("Digite um valor: "))
# dobro (num)
# triplo(num)
# quadruplo(num)


def criar_multiplicador(multiplicador):
  def multiplicar(num):
    return num * multiplicador
  return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

print(duplicar(2))