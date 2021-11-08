import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

medal_table = pd.DataFrame(
    {
        'country': ('USA', 'China', 'Japan', 'Great Britain', 'ROC', 'Australia', 'Netherlands',
                    'France', 'Germany', 'Italy'),
        'gold': (39, 38, 27, 22, 20, 17, 10, 10, 10, 10),
        'silver': (41, 32, 14, 21, 28, 7, 12, 12, 11, 10),
        'bronze': (33, 18, 17, 22, 23, 22, 14, 11, 16, 20),
        'total': (133, 88, 58, 65, 71, 46, 36, 33, 37, 40)
    }
)



def main():
    # Obtenemos los datos por cada columna
    labels = medal_table['country']
    gold = medal_table['gold']
    silver = medal_table['silver']
    bronze = medal_table['bronze']

    # Crear una figura con un subplot
    figure, axes = plt.subplots(figsize=(10, 10))

    # Graficamos las barras
    axes.bar(labels, bronze, color='brown', label='Bronze')
    axes.bar(labels, silver, color='gray', label='Silver', bottom=bronze)
    gold_bars = axes.bar(labels, gold, color='gold', label='Gold', bottom=bronze+silver)

    # Configuramos etiquetas de valores
    axes.bar_label(gold_bars)

    # Configuramos titulos de los ejes y del grafico
    axes.set_xlabel('Countries')
    axes.set_ylabel('Medals')
    axes.set_title('Tokyo 2020')

    axes.legend()

    # Rotamos las etiquetas 45 grados
    plt.xticks(rotation=45)

    # Mostramos el grafico
    plt.show()


if __name__ == '__main__':
    main()
