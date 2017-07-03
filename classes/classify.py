
import numpy

from classes.database import Database


class Classify:

    @staticmethod
    def crispKnn(compareVector, k):     # knn ohne Membership. Sollte so funktionieren

        def getKey(item):   # wird genutzt um nach Distanz zu sortieren
            return item[1]

        def euclid(vectorA, vectorB):
            if len(vectorA) == len(vectorB):

                euclideanDistance = 0

                for iEuc in range(len(vectorA)):
                    singleDistance = (vectorA[iEuc] - vectorB[iEuc])**2
                    euclideanDistance += singleDistance

                euclideanDistance = euclideanDistance**0.5

            return euclideanDistance

        database = Database()
        database.loadDatabase()

        labeledVectors = []

        featureVectors = database.readFeatureVectors()
        for char in featureVectors:
            for char_vector_count in featureVectors[char]:
                oneLabeledVector = []
                oneLabeledVector.append(char)       # label merken
                oneLabeledVector.append(char_vector_count)  # Merkmalsvector merken

                labeledVectors.append(oneLabeledVector)     # den einen gelabelten vector in die Sammlung werfen.

        # compareVector = numpy.array(compareVector)  # hält eingehenden Merkmalsvector als numpy Array
        distances = []
        neighbours = []


        # durchläuft alle Merkmalsvectoren der db und berechnet ihre distanz zum neuen Wert
        for entry in labeledVectors:
            # currentVector = numpy.array(entry[1])     # entry[1], weil dort der Merkmalsvector ist
            # distance = numpy.linalg.norm(currentVector - compareVector)
            distance = euclid(compareVector, entry[1])
            distances.append(labeledVectors[entry], distance)
            # jetzt enthält distances alle gelabelten merkmalsvectoren
            # und bei jedem der Vectoren steht die distanz zum neuen wert

        distances.sort(key=getKey)  # sortiere nach der errechneten distanz

        i = 0

        for x in range(k):      # nehme nur die k nächsten Nachbarn
            neighbours.append(distances[i])
            i += 1

        mostFrequentLabelCount = 0

        for a in neighbours:    # zähle welches Label das häufigste ist
            count = 0
            for b in neighbours:
                if b[0] == a[0]:    # 0, da dort das label gespeichert ist
                    count = count + 1
            if mostFrequentLabelCount < count:
                mostFrequentLabel = a[0]
                mostFrequentLabelCount = count

        print(mostFrequentLabel)

    @staticmethod
    def classifyTrainingSetSimple(matrix):
        classes = []  # todo array, das alle klassen halten soll

        for row in matrix:
            classMembership = classes
            for eachClass in classes:
                if eachClass == row.placeHolder:    # placeHolder = klasse von row abfragen   todo
                    membership = 1
                else:
                    membership = 0

                classMembership[eachClass].append(membership)   # hier soll jedem slot im array die membership zur
                                                                # klasse als zweite dimension gegeben werden...
                                                                # todo ... passt das so?

            matrix[row].append(classMembership)     # weise dem merkmalsvector in einem zusätzlichen slot das
                                                    # 2d array mit der membership in allen klassen zu

    @staticmethod
    def classifyTrainingSetByMean(matrix):  # genauer als simple methode, aber etwas complexer... evtl nicht genug zeit
        classes = []  # todo array, das alle klassen, sowie deren mean halten soll (1 spalte = klasse + merkmalmeans)
        vectorCounterI = 0   # zählt die anzahl der gelernten vectoren pro klasse

        for eachClass in classes:
            for row in matrix:
                if actualClass == eachClass:    # actualClass ersetzen durch abfrage nach der klasse im actuellen vector
                    classes[eachClass].placeHolder  #todo hier soll der merkmalsvector aus row unter der klasse als
                                                    # zweite dimension gespeichert werden. auf den vector soll dabei
                                                    # draufaddiert werden, wenn eine klasse mehrere vectoren hat.
                                                    # (also mehrere merkmalsvectoren)
                    vectorCounterI += 1

            for feature in classes[eachClass]:
                # Ausnahme für das 1. feld, das ja nur die klassenbezeichnung hält (todo... weiß nicht wie, sorry =( )
                classes[eachClass][feature] = feature / vectorCounterI

            vectorCounterI = 0

        # jetzt haben wir ein 2d Array classes[], das alle Klassen und deren Mean enthält

        for row in matrix:
            classMembership = []
            for eachClass in classes:
                vectorA = numpy.array(eachClass)    # todo nur die merkmale nehmen, da die distance berechnet wird
                vectorB = numpy.array(row)          # todo nur die merkmale nehmen, da die distance berechnet wird
                distance = numpy.linalg.norm(vectorA - vectorB)

                classMembership.append(eachClass, 1/distance)
            matrix[row].append(classMembership)

    @staticmethod
    def fuzzyKnn(matrix, compareVector, k):     #sicherheitshalber noch nicht verwenden
        if 1 <= k <= matrix.length():       # haben wir length?
            return

        compareVectorToCalculateDistance = numpy.array(compareVector)  # hält eingehenden vector
        distances = []
        neighbours = []

        def getKey(item):
            return item[1]

        for row in matrix:
            currentVector = numpy.array(row)
            distance = numpy.linalg.norm(currentVector - compareVectorToCalculateDistance)     # distanz mit numpy berechnet.
            distances.append(matrix[row], distance)     # vector in der matrix + dessen distanz in ein array legen

        distances.sort(key=getKey)      # alle vectoren nach distanz sortieren

        i = 0

        for x in range(k):
            neighbours.append(distances[i])
            i += 1

        #jetzt haben wir die k nächsten Nachbarn

        def computeUiX(classI, inputVectorX, weightM):      # berechne membership in einer klasse
            a = 0
            b = 0

            for neighbour in neighbours:
                a += (1 / (neighbours[neighbour][1]**(2/(weightM-1)))) * membershipUij #todo membership korrekt abfragen
                b += 1 / (neighbours[neighbour][1]**(2/(weightM-1)))

            return a/b

        allClasses = []     # todo array, das alle classen enthält

        classMembership = allClasses    # warscheinlich unnötiger zwischenschrit... habs zur lesbarkeit drin gelassen

        for eachClass in allClasses:
            membership = computeUiX(eachClass, compareVector, 2)

            classMembership[eachClass].append(membership)   # hier soll jedem slot im array die membership zur
                                                            # klasse als zweite dimension gegeben werden...
                                                            # todo ... passt das so?

        compareVector.append(classMembership)   # weise dem merkmalsvector in einem zusätzlichen slot das
                                                # 2d array mit der membership in allen klassen zu









