import pandas as pd
import pathlib


def main():
    data_path = pathlib.Path().resolve().absolute().joinpath('data/cwur_2019.csv')
    ranking = pd.read_csv(data_path)
    print(f"Headers: {', '.join(ranking.columns.values)}")
    print(f'Columns: {len(ranking.columns)}')
    print(f'Rows: {len(ranking)}')


if __name__ == '__main__':
    main()
