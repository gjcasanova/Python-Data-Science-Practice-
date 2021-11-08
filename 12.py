import numpy as np
import pandas as pd
import pathlib


def main():
    # Obtenemos la ruta absoluta del dataset
    data_path = pathlib.Path().resolve().absolute().joinpath('data/cwur_2019.csv')
    # Cargar los datos en memoria usando un dataframe
    ranking = pd.read_csv(data_path)
    ranking['education_quality'].replace({'-': np.nan}, inplace=True)

    # Creamos una copia con un espacio de memoria independiente
    ranking_copy = ranking.copy()
    # Insertamos una columna llamada education_quality_level con el valor 'Undefined' por defecto
    ranking_copy.insert(5, 'education_quality_level', 'Undefined')

    # Seleccionamos las filas a reemplazar y colocamos los textos solicitados
    ranking_copy.loc[ranking_copy['education_quality'].astype(np.float64) < 100, 'education_quality_level'] = 'High'

    ranking_copy.loc[(100 <= ranking_copy['education_quality'].astype(np.float64)) & (
        300 >= ranking_copy['education_quality'].astype(np.float64)), 'education_quality_level'] = 'Medium'

    ranking_copy.loc[ranking_copy['education_quality'].astype(np.float64) > 300, 'education_quality_level'] = 'Low'

    # Obtenemos y mostramos aquellos que pertenecen a Portugal y tienen un nivel bajo
    print(ranking_copy[(ranking_copy.education_quality_level == 'Low') & (
        ranking_copy.location == 'Portugal')][['institution', 'location', 'education_quality_level']])


if __name__ == '__main__':
    main()
