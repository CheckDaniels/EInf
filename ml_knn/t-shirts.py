import sklearn.neighbors as nb
import pandas as pd

column_names = ["gewicht", "korpergrosse", "size"] # setzt die Kategorien in eine Liste

tshirt_data_set = pd.read_csv("t-shirts.csv", names=column_names) # liest die t-shirts.csv file und gibt folgende Kategorienamen

# pandas.read_csv.head()
print(tshirt_data_set.head()) #gibt die obersten 5 Daten wieder
print(tshirt_data_set.tail()) #gibt die unterste 5 Daten wieder
print(tshirt_data_set.describe()) #gibt allgemeine statistische Werte der einzelnen Feautures wieder, die Integers sind -> Size also nicht
# (Anzahl, arithm. Mittelwert, Standarabweichung, Minimum, 25%, 50%, 75%, Maximum)

X = tshirt_data_set [[ "gewicht" , "korpergrosse" ]] # sind die Features
y = tshirt_data_set ["size"] # ist die Klasse
print(X)
print(y)

# knn
classifier = nb.KNeighborsClassifier(n_neighbors=3) # initialisiert KNeighborsClassifier
classifier.fit(X, y) # setzt den Classifier auf das pandas_data_set (X, y) an
averages = X.mean() # sucht den Durchschnitt des Datensets, als Beispiel

x_star = pd.DataFrame(averages).T # konvertiert es in Pandasformat und transponiert mit T

print(x_star)
vorhergesagte_klasse = classifier.predict(x_star) # knn-Verfahren für den Durchschnittswert

print(vorhergesagte_klasse)