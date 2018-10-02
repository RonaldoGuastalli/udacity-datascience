'''
Quiz: readable_timedelta
Escreva uma função chamada readable_timedelta que receba um argumento, um número inteiro days, e devolva uma string que
diz quantas semanas e dias esse número representa. Por exemplo, readable_timedelta(10) deve devolver, "1 week(s) and 3
day(s)."
'''
# write your function here
def readable_timedelta(days):
    semana = days // 7 # parte inteira
    dia = days % 7
    return "{} semana(s) e {} dia(s)".format(semana, dia)

# test your function
print(readable_timedelta(50))