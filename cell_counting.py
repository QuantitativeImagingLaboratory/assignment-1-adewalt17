from collections import Counter
#import matplotlib.pyplot as plt #MAY NEED TO UNCOMMENT THIS
#import numpy as np    MAY NOT NEED TO IMPORT THIS HERE
class cell_counting:

    def blob_coloring(self, image):

        #regions = dict()
        (row,col) = image.shape
        regions = np.zeros(row,col,dtype = np.uint32) #make this uint32
        dictionary = {}
        k = 1
        for i in range(row):
            for j in range(col):
                current=image[i,j]
                left=image[i,j-1]
                top=image[i-1,j]
                if current == 1 and left == 0 and top == 0:
                    regions[i,j] = k
                    dictionary[k] = set([i,j]) # NEW   may not need to be [] around i,j
                    k += 1
                elif current == 1 and left == 0 and top == 1: #bottom left in pic
                    regions[i,j] = regions[i-1,j] #R[c] = R[n]
                    region_dict[regions[i,j]].add(i,j) # for the k value in regions matrix(key) add the coordinate tuple to the list of values associated with the key
                elif current == 1 and left == 1 and top == 0:
                    regions[i,j] = regions[i,j-1]
                    dictionary[regions[i,j]].add(i,j) #top right in pic
                elif current == 1 and left == 1 and top == 1:
                    regions[i, j] = regions[i - 1, j]  # R[c] = R[n]
                    if regions[i-1,j] == regions[i,j-1]: # if the pixels are black AND the regions are the same
                        dictionary[regions[i,j]].add(i,j)
                        continue
                    for r in dictionary[regions[i,j-1]]:
                        regions[r[0],r[1]] = regions[i,j] #LOOK AGAIN
                    union = dictionary[regions[[i-1,j]]] or dictionary[regions[i,j-1]]
                    union.add(i,j)
                    dictionary[regions[i,j-1]].clear() #SHOULD THIS BE DEL INSTEAD OF CLEAR??
                    dictionary[regions[i,j]] = union
                if regions[i,j-1] != regions[i-1,j]: # if pixels (left and top) are black and regions are different, make regions the same
                    regions[i,j-1] = regions[i-1,j]



        return dictionary

    def compute_statistics(self, region_dict):

        minimum_area = 15
        stats = {}
        for k,pixels in dictionary.items():
            area = len(pixels)
            if area < minimum_area:
                continue
            (si,sj) = (0,0)
            for (i,j) in pixels:
                si += i
                sj += j
            si /= area
            sj /= area
            stats[k] = {'x':sj,'y':si, 'area':area}

        print(stats)



        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return 0

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        return image


