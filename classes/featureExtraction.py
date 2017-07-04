class FeatureExtraction:
    def __init__(self, img):
        #print("Init Feature Extraction")
        self.img = img
        self.rows = len(img[0])
        self.lines = len(img)

    def getpixelaverage(self):
        # block_size = 11  # decides the size of neighbourhood area
        # c = -15  # a constant which is subtracted from the mean or weighted mean
        #print("Extracting pixel-average")

        # computing pixel-average
        black = 0
        white = 0
        img = self.img
        for line in range(len(img)):
            for row in range(len(img[line])):
                if img[line][row] == 255:
                    white += 1
                else:
                    black += 1

        amount = black + white
        sum_white = white * 255
        pixel_average = sum_white / amount

        #print("Pixel Average: ")
        #print(pixel_average)

        return pixel_average
