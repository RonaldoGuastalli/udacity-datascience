elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# Adicione uma entrada 'is_noble_gas' para hydrogen e helium identificando se são gases nobres
# dica: helium é um gás nobre, hydrogênio não

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
print(elements)

print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])

print(elements['hydrogen']['weight'])

a = elements.items()
b = elements.get('hydrogen')
print(a)
print(b)

