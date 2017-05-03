class PCA:
    def __init__(self):
        pass

    def trainChar(self, char, img_arr):
        rowvector_arr = []  # Will be multidimensional -> [rows][lines]
        matrix = None  # rows, lines
        for img in img_arr:
            rowvector_arr.append(self.generateRowVector(img))

    @staticmethod
    def generateRowVector(img):
        (lines, rows) = img.shape
        rowvector = []
        for row in range(rows):
            for line in range(lines):
                rowvector.append(img[line][row])
        return rowvector
