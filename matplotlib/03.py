```py
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

def main():
    df = pd.read_csv("03.txt", sep=',')
    print(df)
    print(df.columns)
    df.to_csv("03.txt", index=False)
    df.shape
    df.describe(include="all")
    print(df.info())
    df['Class'].value_counts()
    # сумма всех нулевых значений в dataframe
    df.isnull().sum().sum()
    # В каждом столбце нет пропущенных значений, поэтому не будем делить датасет на 2 выборки
    df.isnull().sum()
    # Восстановить пропущенные значения средним по трем ближайшим объектам из подвыборки без пропущеннных значений
    # Мне не нужно этого делать т.к всё окей у меня в датасете, пример ниже
    df['value']=df.groupby(['name','class'])['value'].apply(lambda x:x.fillna(x.mean()))
    # Скопировать данные в разные csv-файлы, при этом данные на файлы разделить по значению целевой переменной
    df1 = df[df['Class'] == 0]
    df2 = df[df['Class'] == 1]
    df1.to_csv("03_0.csv", index=False)
    df2.to_csv("03_1.csv", index=False)
    # для каждого поля необходимо посчитать медиану,среднее значение,наибольшее значение,наименьшее значение
    for i in df:
        print()
        print("Column", i)
        print("Mean:", df[i].mean())
        print("Median:", df[i].median())
        print("Min:", df[i].min())
        print("Max:", df[i].max())
        # тепловая карта
    sns.heatmap(df.corr(), annot=True, fmt='.2f')
    plt.show()
    # Для числовых признаков выполнить стандартизацию значений(матожидание=1,скво=1)
    df_new = df.copy()
    df_new.drop('Class', axis=1, inplace=True)
    df_new
    # Для числовых признаков выполнить стандартизацию значений(матожидание=1,скво=1)
    d = (df_new - df_new.mean()) / df_new.std()
    print(d)
    # Разделить датасет на 2 выборки
    # разделить датасет на 2 выборки в соотношении 70% и 30% так, чтобы по каждому значкению целевой переменной в первую выборку попало
    # 70% записей,а во вторую 30% записей; сохранить полученные выборки

    from sklearn.model_selection import train_test_split

    # get the locations
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    print(X_train)
    print(y_train)
    # запись в csv файл
    X_train.to_csv("X_train.csv")
    y_train.to_csv("y_train.csv")

if __name__ == '__main__':
    main()
```
