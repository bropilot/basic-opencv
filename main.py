#Matplot lib stuff
#Matplot will be used for non dimensonal arrays, understanding the shape of the array, and also getting the axis of a ray, also this will be using numpy 
#numpy will help to write my code more efficiently, accurate, and detailed

#both numbers have to euqal the first number to make your shape
#This is a numpy array
"""import numpy as np
a = np.arange(20).reshape(5, 4)
print(a)"""

#We will come back to this when we need it

import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile('grasss.png'))

if img is None:
  sys.exit('Could not read the image.')

cv.imshow('Cove School Project', img)
k = cv.waitKey(0)

if k == ord('s'):
  cv.imwrite('grasss.png', img)

#This is so when I run the project, it can be presentable:
print("\nignore this for now\nHere is how opencv went:\nI first, blah...blah; Add more here!\nI then compared\n(List a github project here), with (List another github project) and both had, blah...blah; Add more here!\nHere is my final project:\nWhat it does is blah...blah; Add the last step here! How it realates to my evrey day is, blah...blah; add more here")