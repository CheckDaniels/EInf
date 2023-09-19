import sklearn.neighbors as nb
import pandas as pd

column_names = ["Kelchblattlänge", "Kelchblattbreite", "Kronblattlänge", "Kronblattbreite", "Art"]

iris_data_set = pd.read_csv("iris.csv", names=column_names)

print(iris_data_set.head())
print(iris_data_set.tail())
print(iris_data_set.describe())

X = iris_data_set [[ "Kelchblattlänge" , "Kelchblattbreite" , "Kronblattlänge" , "Kronblattbreite" ]]
y = iris_data_set ["Art"]
print(X)
print(y)


classifier = nb.KNeighborsClassifier(n_neighbors=3)
classifier.fit(X, y)

averages = X.mean()
x_star = pd.DataFrame(averages).T

print(x_star)
vorhergesagte_klasse = classifier.predict(x_star)

print(vorhergesagte_klasse)