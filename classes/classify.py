
import numpy

from classes.featureExtraction import FeatureExtraction
from classes.database import Database


class Classify:
    def __init__(self, img):    # copied from Pre-Processing
        print("Init Classification")
        self.img = img
        self.rows = len(img[0])
        self.lines = len(img)

    @staticmethod
    def myKnn(matrix, compareVector):
        compareVector = numpy.array(compareVector)  # holding Incoming Value

        shortestDistance = 99999

        for row in matrix:
            currentVector = numpy.array(row)
            distance = numpy.linalg.norm(currentVector - compareVector)  # numpy provides method for euclidean distance
            if shortestDistance > distance:
                nextNeighbour = row
                shortestDistance = distance

        return nextNeighbour

    def compare_with_database_pixelAverage(self):   # muss man hier schon details zur Datenbank anhängen?
        print("Start Comparing")

        extractor = FeatureExtraction(self.img)
        incoming_average = extractor.getpixelaverage()
        key_of_incoming_average = X

        best_hit = 300
        best_key = X            # was wäre hier das NULL ?
        second_hit = 300
        second_key = X
        third_hit = 300
        third_key = X

        database = Database()
        database.initializeEmpty()

        for key in database:
            average_value_array = database.read(key, "average")
            for value in average_value_array:
                if abs(value - incoming_average) < best_hit:
                    third_hit = second_hit
                    third_key = second_key
                    second_hit = best_hit
                    second_key = best_key
                    best_hit = abs(value - incoming_average)
                    best_key = key
                elif abs(value - incoming_average) < second_hit:
                    third_hit = second_hit
                    third_key = second_key
                    second_hit = abs(value - incoming_average)
                    second_key = key
                elif abs(value - incoming_average) < third_hit:
                    third_hit = abs(value - incoming_average)
                    third_key = key

        error = 2   # Fehlertoleranz (evtl nett... war ne Idee ^^")

        if third_hit-second_hit <= error and second_hit-best_hit <= error:
            if second_key == third_key:             # keys dieser beiden, nicht die Vergleichswerte selbst
                key_of_incoming_average = second_key
            else:
                key_of_incoming_average = best_key

        return key_of_incoming_average







