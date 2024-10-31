# Uma copia raza por mais que esteja indicando ela, qualquer alteracao afeta o primeiro dicionario em um elemento "mutavel"

import copy

d1 = {
  'c1': 1,
  'c2': 2,
  'li': [1, 2, 3],
}

# para ter uma copia profunda onde nao irá afetar outro elementos
d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['li'][1] = 9999

print(d1)
print(d2)