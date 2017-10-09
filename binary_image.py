import numpy as np

class binary_image:

    def compute_histogram(self, image):

        (row, col) = image.shape
        hist = [0]*256
        for i in range(row):
            for j in range(col):
                hist[image[i, j]] += 1

        return hist

    def expected_value(self, pdf, offset, total):
        exp = 0
        for i, val in enumerate(pdf):
            exp += (i+offset)*val/total
        return exp

    def find_optimal_threshold(self, hist):

        threshold = int(len(hist)/2)
        pixelnum = sum(hist)
        (uprev,vprev) = (0,0)
        u = exp_val(hist[:threshold],0,pixelnum)
        v = exp_val(hist[t:],threshold,pixelnum)
        threshold = int((u+v)/2)
        (du,dv) = (u-uprev,v-vprev)
        while du != 0 and dv != 0:
            (uprev, vprev) = (u, v)
            u = exp_val(hist[:threshold], 0, pixelnum)
            v = exp_val(hist[t:], threshold, pixelnum)
            threshold = int((u + v) / 2)
            (du, dv) = (u - uprev, v - vprev)

        return threshold

    def binarize(self, image):

        bin_image = image.copy()
        hist = compute_histogram(image)
        a = find_optimal_threshold(hist)
        for i in range(row):
            for j in range(col):
                if image[i,j] <= a:
                    bin_image[i,j] = 0
                else:
                    bin_image[i,j] = 255

        return bin_image


