'''
O Python não permite que funções modifiquem variáveis que não estão no escopo da função.
'''
egg_count = 0

def buy_eggs(count):
    if(count >= 0):
        print('valor da variavel passado atravez da função: Funciona')
        return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count) # passa o valor da variável pela função
print('quantidade de eggs: {}'.format(egg_count))

print('----------')


def buy_eggs2():
    egg_count += 15 # purchase a dozen eggs

buy_eggs2() # UnboundLocalError: local variable 'egg_count' referenced before assignment