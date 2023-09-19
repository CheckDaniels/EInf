import pandas as pd
import sklearn.neighbors as nb

column_names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "species"]
iris_data_set = pd.read_csv("iris.csv", names=column_names)

print(iris_data_set.head())
print(iris_data_set.tail())
print(iris_data_set.describe())

X = iris_data_set[["sepal-length", "sepal-width", "petal-length", "petal-width"]]
y = iris_data_set["species"]

classifier = nb.NearestCentroid()
# Fit the NearestCentroid model according to the given training data.
# => Berechne die "Zentrumsvektoren". Diese werden dann abgespeichert, sprich das ist das Modell der Daten.
classifier.fit(X, y)

averages = X.mean()
x_star = pd.DataFrame(averages).T
print(x_star)
vorhergesagte_klasse = classifier.predict(x_star)
print(vorhergesagte_klasse)