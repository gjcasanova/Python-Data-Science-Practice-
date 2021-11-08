import numpy as np
import pandas as pd
import pathlib


def main():
    # Obtenemos la ruta absoluta del dataset
    data_path = pathlib.Path().resolve().absolute().joinpath('data/cwur_2019.csv')
    # Cargar los datos en memoria usando un dataframe
    ranking = pd.read_csv(data_path)

    # Con groupby agrupamos por pais, con agg obtenemos el promedio en una nueva columna
    # con sort_values ordenamos por la columna mean
    mean_por_country = ranking.groupby('location').agg(mean=pd.NamedAgg(
        'score', np.mean)).sort_values(by='mean', ascending=False)

    # Mostramos el primero en el dataframe
    print(mean_por_country.head(1))


if __name__ == '__main__':
    main()
