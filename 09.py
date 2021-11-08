import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pathlib


def main():
    # Obtenemos la ruta absoluta del dataset
    data_path = pathlib.Path().resolve().absolute().joinpath('data/cwur_2019.csv')
    # Cargar los datos en memoria usando un dataframe
    ranking = pd.read_csv(data_path)
    # Imprimos los datos
    print(f"Headers: {', '.join(ranking.columns.values)}")
    print(f'Columns: {len(ranking.columns)}')
    print(f'Rows: {len(ranking)}')


if __name__ == '__main__':
    main()
