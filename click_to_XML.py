import argparse
import cv2

# Init points that will be used to store the data,
# and bool of if the mouse is press or not
refPts = []
mouseDown = False

def click_boundary(event, x, y, flags, param):
    # Grab reference to the global variable
    global refPts, mouseDown

    # If the mouse is pressed, take down the
    # x and y coord

    if event == cv2.EVENT_LBUTTONDOWN:
        refPts.append(x)
        refPts.append(y)
        mouseDown = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPts.append(x)
        refPts.append(y)
        mouseDown = False

        # Draw a rect around the region of interest...
        cv2.rectangle(image, refPts[0], refPts[1], (0, 255, 0), 2)
        cv2.imshow('image', image)

# Construct the argument parser and parse argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="/home/julien/Pictures/Chair/")
imageName = "/home/julien/Pictures/Chair/0001.jpg"
args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_boundary)

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()
        
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break
    
    # if there are two reference points, then crop the region of interest
    # from teh image and display it
    if len(refPts) == 2:
        roi = clone[refPts[0][1]:refPts[1][1], refPts[0][0]:refPts[1][0]]
        cv2.imshow("ROI", roi)
        cv2.waitKey(0)
        
# close all open windows
cv2.destroyAllWindows()
        
