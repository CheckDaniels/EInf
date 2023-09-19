import pandas as pd
import numpy as np
import statistics

AnzahlNeighbours = 3
column_names = ["Kelchblattlänge", "Kelchblattbreite", "Kronblattlänge", "Kronblattbreite", "Art"]

iris_data_set = pd.read_csv("iris.csv", names=column_names)

# eine mehrdimensionale Matrix/Array, nxm-Matrix
X = iris_data_set [[ "Kelchblattlänge" , "Kelchblattbreite" , "Kronblattlänge" , "Kronblattbreite" ]].values #enfernt die Spaltenzahl
y = iris_data_set ["Art"].values

x_star = np.mean(X, axis=0) # axis = 0 -> [a1],[b1], ..., [z1] - Mittelwert

A = X - x_star # ergibt den Abstandsvektor zu x_star
B = np.linalg.norm(A, axis=1) # axis = 1 -> [n1, n2, n3, n4] - Satz des Pythagoras - Betrag

temp = np.copy(B) # Kopie
votes = [] # hält die Abstandswerte der nähersten Nachbarn fest

for i in range(AnzahlNeighbours):
    nächster_Nachbar = np.argmin(temp) #die Nachbarn mit geringstem Abstand
    Klasse_Nachbar = y[nächster_Nachbar] #Bestimmt die Art des Nachbarn
    votes.append(Klasse_Nachbar) #fügt die Pflanzenart hinzu
    # Nähersten Nachbarn aus der Kopie löschen, dann kann der zweitnäherste Nachbar auf dieselbe Weise bestimmt werden.
    np.delete(temp, nächster_Nachbar)
# Bestimmte die Klasse die am häufigsten vorkommt.
vorhergesagte_klasse = statistics.mode(votes)
print(vorhergesagte_klasse)