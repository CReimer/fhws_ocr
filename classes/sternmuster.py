class Sternmuster:
    # Das Ausgangsbild muss auf den Rand genau zugeschnitten und binarisiert sein
    def __init__(self, img):
        print("Init Sternmuster")
        self.img = img
        self.rows = len(img[0])
        self.lines = len(img)
        self.rowM = int(self.rows / 2)
        self.linM = int(self.lines / 2)
        self.minR = 0
        self.minL = 0
        self.maxR = self.rows
        self.maxL = self.lines
        self.counter = 0

    @property
    def sternMit8vongMitteAus(self):
        momentanR = self.rowM
        momentanL = self.linM
        if momentanL < momentanL:
            momentanG = momentanL
        else:
            momentanG = momentanR

        # Mitte->min/min		-1/-1
        for punkt in range(momentanG):
            if self.img[momentanR][momentanL] == 0:
                self.counter = self.counter + 1
            momentanR = momentanR - 1
            momentanL = momentanL - 1

        momentanR = self.rowM
        momentanL = self.linM

        # Mitte->min/max:2   -1/+0
        for punkt in range(self.rowM):
            if self.img[momentanR][momentanL] == 0:
                self.counter = self.counter + 1
            momentanR = momentanR - 1

        momentanR = self.rowM
        # Mitte->min/max		-1/+1
        for punkt in range(momentanG):
            if self.img[momentanR][momentanL] == 0:
                self.counter = self.counter + 1
            momentanR = momentanR - 1
            momentanL = momentanL + 1

        momentanR = self.rowM
        momentanL = self.linM

        # Mitte->max:2/max	+0/+1
        for punkt in range(self.lines - self.linM):
            if self.img[momentanR][momentanL] == 0:
                self.counter = self.counter + 1
            momentanL = momentanL + 1

        momentanL = self.linM

        # Mitte->max:2/min	+0/-1
        for punkt in range(self.rowM):
            if self.img[momentanR][momentanL] == 0:
                self.counter = self.counter + 1
            momentanL = momentanL - 1

        momentanL = self.linM

        # Mitte->max/max:2	+1/+0
        for punkt in range(self.rows - self.rowM):
            if self.img[momentanR][momentanL] == 0:
                self.counter = self.counter + 1
            momentanR = momentanR + 1

        momentanR = self.rows - self.rowM
        momentanL = self.lines - self.linM
        if momentanL < momentanR:
            momentanG = momentanL
        else:
            momentanG = momentanR

        # Mitte->max/max		+1/+1
        for punkt in range(momentanG):
            if self.img[momentanR][momentanL] == 0:
                self.counter = self.counter + 1
            momentanR = momentanR + 1
            momentanL = momentanL + 1

        momentanR = self.rows - self.rowM
        momentanL = self.lines - self.linM

        # Mitte->max/min 		+1/-1
        for punkt in range(momentanG):
            if self.img[momentanR][momentanL] == 0:
                self.counter = self.counter + 1
            momentanR = momentanR + 1
            momentanL = momentanL - 1

        return self.counter
