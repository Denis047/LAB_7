import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import collections

data = pd.read_csv('#2_auctions.csv')

print(data.info(memory_usage=False))
print(data.columns)
print(data.Назва[0])
print(data.Стан[0])
print(data.Категорія[0])
print(data.Місцезнаходження[0])
print(data.Переможець[0])
print(data['Номер лота'][0])
print(data['Стартова ціна'][0])
print(data['Ціна продажу'][0])

start = data['Стартова ціна']
sold = data['Ціна продажу']


def analyze_data(column):
    print(f'\n MAX: {column.max()}')
    print(f'\n MIN: {column.min()}')
    print(f'\n MEAN: {column.mean()}')
    print(f'\n MEDIAN: {column.median()}')
    print(f'\n MODE: {column.mode()[0]}')
    print(f'\n MAD: {np.mean(np.abs(column - column.mean()))}')
    print(f'\n IS NORMAL: {column.mean() == column.median() == column.mode()[0]}')


analyze_data(start)

analyze_data(sold)

# sort data
num = sorted(data['Номер лота'][:])
start = sorted(data['Стартова ціна'][:])
sold = sorted(data['Ціна продажу'][:])

num_vec = [i for i in num if not str(i).isdigit()]
start_vec = [i for i in start if not str(i).isdigit()]
sold_test1 = [i for i in sold if not str(i).isdigit()]

num_vec = collections.Counter(num)


sns.scatterplot(data=data, y='Стартова ціна', x=range(len(data['Стартова ціна'])), label='Start')
sns.scatterplot(data=data, y='Ціна продажу', x=range(len(data['Ціна продажу'])), label='Sold')

plt.xlabel('Номер лоту')
plt.ylabel('Ціна')
plt.title('')
plt.legend()

plt.show()

numeric_data = data.select_dtypes(include=[np.number])
corr_matrix = numeric_data.corr()
print(corr_matrix)

sns.heatmap(corr_matrix, annot=True)
plt.show()
