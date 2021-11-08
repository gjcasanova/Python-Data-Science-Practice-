# import numpy as np
# import pandas as pd
# import pathlib


# def main():
#     data_path = pathlib.Path().resolve().absolute().joinpath('data/cwur_2019.csv')
#     ranking = pd.read_csv(data_path)
#     mean_per_country = ranking.groupby('location').agg(mean=pd.NamedAgg(
#         'score', np.mean)).sort_values(by='mean', ascending=False)
#     print(mean_per_country.head(1))


# if __name__ == '__main__':
#     main()
