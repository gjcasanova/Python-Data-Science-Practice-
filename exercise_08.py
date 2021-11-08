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
    labels = medal_table['country']
    gold = medal_table['gold']
    silver = medal_table['silver']
    bronze = medal_table['bronze']

    figure, axes = plt.subplots(figsize=(10, 10))
    figure.subplots_adjust(bottom=0.3)
    axes.bar(labels, bronze, align='center', color='brown', label='Bronze')
    axes.bar(labels, silver, align='center', color='gray', bottom=bronze, label='Silver')
    gold_bars = axes.bar(labels, gold, align='center', color='gold', bottom=bronze+silver, label='Gold')

    axes.bar_label(gold_bars)
    axes.set_title('Tokyo 2020')
    axes.set_xlabel('Countries')
    axes.set_ylabel('Medals')
    axes.legend()

    plt.xticks(rotation=45)
    plt.show()


if __name__ == '__main__':
    main()
