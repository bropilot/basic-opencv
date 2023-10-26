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
import numpy as np
import sys

#This is how to draw on the img
#We'll come back to drawing shapes
"""img = np.zeros((200, 200, 3), np.uint8)
cv.line(img, (0, 0), (199, 199), (255, 0, 0), 5)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)"""

#This is for how to load images
"""img = cv.imread(cv.samples.findFile('grasss.png'))

if img is None:
  sys.exit('Could not read the image.')

cv.imshow('Cove School Project', img)
k = cv.waitKey(0)

if k == ord('s'):
  cv.imwrite('grasss.png', img)"""

#This is so when I run the project, it can be presentable:
print("\nignore this for now\nHere is how opencv went:\nI first, blah...blah; Add more here!\nI then compared\n(List a github project here), with (List another github project) and both had, blah...blah; Add more here!\nHere is my final project:\nWhat it does is blah...blah; Add the last step here! How it realates to my evrey day is, blah...blah; add more here")

#This is to store all the events in openCV
events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

drawing = False
mode = True
ix, iy = -1, -1

#Mouse callback function
def draw_circle(event, x, y, flags, param):
  global ix, iy, drawing, mode
  if event == cv.EVENT_LBUTTONDOWN:
    drawing = True
    ix, iy = x, y
  elif event ==  cv.EVENT_MOUSEMOVE:
    if drawing == True:
      if mode == True:
        cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
      else:
        cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:
      drawing = False
    if mode == True:
      cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
    else:
      cv.circle(img, (x, y), 5, (0, 0, 255), -1)         

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while(1):
 cv.imshow('image', img)
 k = cv.waitKey(1) & 0xFF
 if k == ord('m'):
  mode = not mode
 elif k == 5:
  break
cv.destroyAllWindows()