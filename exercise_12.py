import numpy as np
import pandas as pd
import pathlib


def main():
    data_path = pathlib.Path().resolve().absolute().joinpath('data/cwur_2019.csv')
    ranking = pd.read_csv(data_path)
    ranking['education_quality'].replace({'-': np.nan}, inplace=True)

    ranking_copy = ranking.copy()
    ranking_copy.insert(5, 'education_quality_level', 'Undefined')

    ranking_copy.loc[ranking_copy['education_quality'].astype(np.float64) < 100, 'education_quality_level'] = 'High'
    ranking_copy.loc[(100 <= ranking_copy['education_quality'].astype(np.float64)) & (
        ranking_copy['education_quality'].astype(np.float64) <= 300), 'education_quality_level'] = 'Medium'
    ranking_copy.loc[ranking_copy['education_quality'].astype(np.float64) > 300, 'education_quality_level'] = 'Low'

    print(ranking_copy[(ranking_copy.education_quality_level == 'Low') & (ranking_copy.location == 'Portugal')])


if __name__ == '__main__':
    main()
