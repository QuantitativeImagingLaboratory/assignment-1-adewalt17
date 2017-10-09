Report:

The compute the histogram function calculates the number of occurrances of intensities in the image. It takes the
image and determines how many times the intensity value occurs in the image. To compute the optimal threshold I initialized
the k value to k/2 to set the threshold to the middle value. Next, I adjusted it using expected value of the left and right hand side
then averaged the two. Until the threshold remain constant, it is continuously reevaluated. To binarize the image, I
took all values less than the computed threshold and assigned them to black for those that are greater I made them white.

For blob coloring I created an array and populated it with zeros of the dimension of the image. Now that there is a matrix with zeros, I
created an empty dictionary, and initialized the k(region number every time you encounter a new region add to k) value to one,
determine if the adjacent pixels are black or white. Based off of this information, you convert it to a dictionary then compute
the statistics and return the area of each blob(number of pixels that are colored). The compute statistics function accepts the
dictionary for the regions that we found for blob coloring. It iterates through the dictionary and eliminate the regions whose pixels
are less than 15.

