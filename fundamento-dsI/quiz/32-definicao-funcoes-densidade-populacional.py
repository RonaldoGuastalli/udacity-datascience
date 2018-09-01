'''
Quiz: Função de densidade populacional
Escreva uma função chamada population_density que aceita dois argumentos, population e land_area, e devolve uma
densidade populacional calculada a partir desses valores. Eu incluí dois casos de teste que você pode usar para
verificar se sua função funciona corretamente. Uma vez que você já escreveu sua função, use o botão de execução de
teste para testar seu código.
'''
# write your function here
def population_density(population, land_area):
    density = population / land_area
    return density

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))