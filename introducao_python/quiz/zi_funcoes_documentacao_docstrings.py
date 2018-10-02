'''
Quiz: Escrevendo uma docstring
Escreva uma docstring para a função readable_timedelta definida anteriormente! Lembre-se de que a maneira como você
escreve suas docstrings é bem flexível! Leia as convenções de docstring do Python aqui e confira esta página do Stack
Overflow para se inspirar!
'''
def readable_timedelta(days):
    # insert your docstring here
    """
    Print the number of weeks and days in a number of days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

print(readable_timedelta(10))