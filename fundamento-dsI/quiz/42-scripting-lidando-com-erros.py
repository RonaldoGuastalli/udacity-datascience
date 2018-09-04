"""Quiz: Lidando com a divisão por zero Neste momento, executar o código abaixo causará um erro durante a segunda
recorrência à função create_groups porque ela se depara com uma exceção ZeroDivisionError. Edite a função abaixo para
lidar com esta exceção. Se ela se depara com a exceção durante a primeira linha da função, deve exibir uma mensagem de
aviso e retornar uma lista vazia. Caso contrário, ela deve executar o resto do código da função. No final, a função
deve sempre exibir quantos grupos foram devolvidos"""

def create_groups(items, n):
    """Splits items into n groups of equal size, although the last one may be shorter."""

    try:
        # determine the size each group should be
        size = len(items) // n  # this line could cause a ZeroDivisionError exception

    except ZeroDivisionError:
        print("WARNING: retorno de lista vazia. Por favor use um numero não zero.")
        return []
    else:
        # create each group and append to a new list
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])

        # print the number of groups and return groups
        return groups
    finally:
        print("{} groups returned.".format(n))



print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))
