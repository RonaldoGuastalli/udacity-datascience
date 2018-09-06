# navegue na lista completa de métodos de string em:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# e teste alguns aqui
minha_str = 'este é um teste dos métodos de string em Python.'
#capitalize()
metodo_capitalize = minha_str.capitalize()
print(metodo_capitalize)
#casefold()
metodo_casefold = minha_str.casefold()
print(metodo_casefold)
#str.center
metodo_center = minha_str.center(89, '*')
print(metodo_center)
#str.encode(encoding="utf-8", errors="strict")
metodo_encode = minha_str.encode(encoding="utf-8")
print(metodo_encode)
#find
metodo_find = minha_str.find('teste')
print('posição ', metodo_find)
#str.isnumeric()
metodo_isnumeric = minha_str.isnumeric()
print(metodo_isnumeric)
