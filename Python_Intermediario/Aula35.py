# Generator expression, Iterables e Iterators em Python
# Só sabe entregar o próximo valor

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))