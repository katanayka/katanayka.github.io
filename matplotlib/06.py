import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
def main():
    df = pd.read_csv("06.txt", sep=",", header=None)
    print(df)
    print(df.columns)
    df.to_csv("06.csv", index=False)
    sns.heatmap(df.corr(), annot=True, fmt=".2f")
    plt.show()
    for i in range(4):
        df[i] = (df[i] - df[i].mean()) / df[i].std() #нормализация
    print(df)
    X_train, X_test, y_train, y_test = train_test_split(df.drop(4, axis=1), df[4], test_size=0.3, random_state=42)
# опорных векторов
    clf = svm.SVC()
    clf.fit(X_train, y_train)
    print("Accuracy:", clf.score(X_test, y_test))
# к ближайших соседей
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    print("Accuracy:", knn.score(X_test, y_test))
#деревья
    tree = DecisionTreeClassifier()
    tree.fit(X_test, y_test)
    print("Accuracy:", tree.score(X_test, y_test))

if name == "main":
    main()

