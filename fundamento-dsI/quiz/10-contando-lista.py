eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# Modifique essa linha para que imprima (print) os últimos 3 elementos da lista
#primeira possibilidades
tamanho_lista = len(eclipse_dates)
eclipse_dates = eclipse_dates[(tamanho_lista)-3: ]
print('resultado de eclipse_dates[(tamanho_lista)-3: ] -> ', eclipse_dates)

#ou desta forma
eclipse_dates[-3: ]
print('resultado de eclipse_dates[-3: ] -> ', eclipse_dates)