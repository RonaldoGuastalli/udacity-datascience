import pandas as pd


def load_data_csv(nome_arquivo):
    """
    load do arquivo para análise
    :param nome_arquivo: str nome do arquivo para load
    :return: data frame (df)
    """
    df = pd.read_csv(nome_arquivo, sep=',')
    return df


def check_types(df):
    """
    check dos dados do data frame
    :param df: data frame
    :return: tipo dados das colunas
    """
    for column in df.columns:
        print('coluna: {0}, tipo: {1}'.format(column, type(df[column][0])))


def valores_ausentes(df):
    """
    verifique se quaisquer colunas do data frame têm valores nulos
    :param df: data frame fornecido
    :return: soma valores ausentes
    """
    resultado = "Não há colunas com valores nulos!!!"
    if(df.isnull().sum().any()):
        print('Colunas apresentam valores nulos, seguem abaixo:')
        resultado = df.isnull().sum()
    return resultado

def valores_distintos(df):
    """
    Retorna a série com o número de observações distintas sobre o eixo solicitado
    :param df: data frame
    :return: variaveis e seus valores distintos
    """
    linhas_distintos = df.nunique()
    sum_linhas_distintas = df.nunique().sum()
    print("Número de observações distintas no data frame:\n{0}, \n***Total*** {1}".format(linhas_distintos, sum_linhas_distintas))


def renomeando_colunas(df):
    """substituir espaços por rótulos com underline e letras minúsculas para o conjunto de dados de 2008"""
    df.rename(columns=lambda x: '_'.join(x.strip().lower().split()), inplace=True)
    return df


