import progressXML as pXML
import argparse
import cv2

from os import listdir
from os.path import isfile, join

# Init points that will be used to store the data,
# and bool of if the mouse is press or not
refPts = [(0, 0), (0, 0)]
mouseDown = False

def click_boundary(event, x, y, flags, param):
    # Grab reference to the global variable
    global refPts, mouseDown

    # If the mouse is pressed, take down the
    # x and y coord

    if event == cv2.EVENT_LBUTTONDOWN:
        refPts[0] = (x, y)
        mouseDown = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPts[1] = (x, y)
        mouseDown = False

        # Draw a rect around the region of interest...
        cv2.rectangle(image, refPts[0], refPts[1], (0, 255, 0), 2)
        cv2.imshow('image', image)


# Construct the argument parser and parse argument
ap = argparse.ArgumentParser()
ap.add_argument("-ip", "--imagepath", required=True, help="Path to directory with images")
ap.add_argument("-dp", "--directorypath", required=True, help="Path of where to put xml files")
args = vars(ap.parse_args())

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_boundary)

onlyfiles = [f for f in listdir(args['imagepath']) if isfile(join(args['imagepath'], f))]

# This will iterate through all the files in the directory
fileNumber = 0

# keep looping until the 'q' key is pressed
while True:
    imageName = args['imagepath'] + onlyfiles[fileNumber]
    print(imageName)

    # load the image, clone it, and setup the mouse callback function
    image = cv2.imread(imageName)
    clone = image.copy()

    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()
        
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break
    
    # If their are two ref points, take the points and save them to an
    # XML file
    if len(refPts) == 2:
        height, width, channels = image.shape
        pXML.createXML('progress', imageName.split('/')[-1], width, height, 3, 'chair',
                       refPts[0][0], refPts[0][1], refPts[1][0], refPts[1][1], args['directorypath'])

        # roi = clone[refPts[0][1]:refPts[1][1], refPts[0][0]:refPts[1][0]]
        # cv2.imshow("ROI", roi)
        fileNumber += 1
        cv2.waitKey(0)
        
# close all open windows
cv2.destroyAllWindows()
        
