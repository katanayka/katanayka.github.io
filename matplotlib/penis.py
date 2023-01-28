import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main():
    df = pd.read_csv("09.txt", sep="	", header=None)
    print(df)
    print(df.columns)
    df.to_csv("09.csv", index=False)
    df1 = df[df[7] == 1]
    df2 = df[df[7] == 2]
    df3 = df[df[7] == 3]
    df1.to_csv("09_1.csv", index=False)
    df2.to_csv("09_2.csv", index=False)
    df3.to_csv("09_3.csv", index=False)
    for i in range(7):
        print("Column", i)
        print("Mean:", df[i].mean())
        print("Median:", df[i].median())
        print("Min:", df[i].min())
        print("Max:", df[i].max())
    sns.heatmap(df.corr(), annot=True, fmt=".2f")
    plt.show()
    for i in range(7):
        df[i] = (df[i] - df[i].mean()) / df[i].std()
    print(df)
    X_train, X_test, y_train, y_test = train_test_split(df.drop(7, axis=1), df[7], test_size=0.2, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    print("Accuracy:", knn.score(X_test, y_test))


if __name__ == "__main__":
    main()
