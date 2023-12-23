"""
Formatação básica de strings
s - string
d - int
f - float

.<número de dígitos>f

x ou X - Hexadecimal
(caractere)(><^)(quantidade)

> - esquerda
< - Direita
^ - centro
= - Força o número a aparecer antes ddos zeros
sinal - + ou -
ex: 0>-100,1f
Conversion flags - !r !s !a

"""

variave = 'ABC'

print(f"{variave}")
print(f"{variave: >10}")
print(f"{variave: <10}")
print(f"{variave: ^10}")

print(f'{-1000.46571401478914:0>-10,.1f}') #Depois dos zeros
print(f'{1000.46571401478914:0=+10,.1f}') #Antes dos zeros
print(f'O hexadecimal de 1500 é{1500:08X}')
print(f'O hexadecimal de 500 é{500:08X}')