import numpy

from classes.database import Database


class Classify:

    @staticmethod
    def crispKnn(compareVector, k):     # knn ohne Membership

        def getKey(item):   # wird genutzt um nach Distanz zu sortieren
            return item[2]

        def euclid(vectorA, vectorB):   # eigener Euklid
            euclideanDistance = 0

            if len(vectorA) == len(vectorB):    # prüfen ob die Merkmalsvektoren gleich lang sind
                for iEuc in range(len(vectorA)):    # step für step die Merkmalsvektoren durchlaufen
                    singleDistance = (vectorA[iEuc] - vectorB[iEuc])**2
                    euclideanDistance += singleDistance
                euclideanDistance = euclideanDistance**0.5
            else:   # falls die Vektoren unterschiedlich lang sind.
                print("Vectors are of different length.")

            return euclideanDistance

        database = Database()
        database.loadDatabase()     # Datenbank initialisieren

        labeledVectors = []     # Liste für alle Merkmalsvektoren und deren Klasse vorbereiten

        featureVectors = database.readFeatureVectors()
        for char in featureVectors:
            for char_vector_count in featureVectors[char]:
                oneLabeledVector = []
                oneLabeledVector.append(char)       # label merken
                oneLabeledVector.append(featureVectors[char][char_vector_count])  # Merkmalsvector merken

                labeledVectors.append(oneLabeledVector)     # den einen gelabelten vector in die Sammlung werfen.

        distances = []
        neighbours = []

        # durchläuft alle Merkmalsvectoren der db und berechnet ihre distanz zum neuen Wert
        for entry in labeledVectors:
            distance = euclid(compareVector, entry[1])
            distances.append([entry[0], entry[1], distance])
            # jetzt enthält distances alle Merkmalsvectoren und deren Klasse
            # und bei jedem der Vektoren steht die distanz zum zu vergleichenden Vektor

        distances.sort(key=getKey)  # sortiere nach der errechneten distanz

        i = 0

        for x in range(k):      # nehme nur die k nächsten Nachbarn
            neighbours.append(distances[i])
            i += 1

        mostFrequentLabelCount = 0

        for a in neighbours:    # zähle welches Label das häufigste ist
            count = 0
            for b in neighbours:
                if b[0] == a[0]:
                    count = count + 1
            if mostFrequentLabelCount < count:
                mostFrequentLabel = a[0]
                mostFrequentLabelCount = count
        #print("Class of Comparevector: ")
        print(mostFrequentLabel, end='')



