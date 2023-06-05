import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(1)
check , frame = cap.read()
# Load the image
#image1 = cv2.imread('C:\\Users\\ROM\\Desktop\\VisualStudio\\catkin_ws\\my_project\\pic\\Real01.jpg')

width = 640
height = 480
dim = (width, height)
 
# resize image
#resized = cv2.resize(image1, dim, interpolation = cv2.INTER_AREA)

# Convert  image to RGB
image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Convert image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Display image and gray image
fx, plots = plt.subplots(1, 2, figsize=(20,10))

#plots[0].set_title("Orignal Image")
#plots[0].imshow(image)
cv2.imshow('original', image)
#plots[1].set_title("Gray Image")
#cv2.imshow(gray, cmap="gray")
#cv2.imshow('gray', gray)
'''
key = cv2.waitKey(0)
if key & 0xFF == ord('q') or key == 27:
    cv2.destroyAllWindows()
'''

fast = cv2.FastFeatureDetector_create() 

# Detect keypoints with non max suppression
keypoints_with_nonmax = fast.detect(gray, None)

# Disable nonmaxSuppression 
#fast.setNonmaxSuppression(False)

# Detect keypoints without non max suppression
#keypoints_without_nonmax = fast.detect(gray, None)

image_with_nonmax = np.copy(image)
image_without_nonmax = np.copy(image)

# Draw keypoints on top of the input image
cv2.drawKeypoints(image, keypoints_with_nonmax, image_with_nonmax, color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#cv2.drawKeypoints(image, keypoints_without_nonmax, image_without_nonmax, color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display image with and without non max suppression
fx, plots = plt.subplots(1, 2, figsize=(20,10))
 
cv2.imshow('image_with_nonmax', image_with_nonmax)
#plots[0].set_title("With non max suppression")
#plots[0].imshow(image_with_nonmax)

#cv2.imshow('image_without_nonmax', image_without_nonmax)
#plots[1].set_title("Without non max suppression")
#plots[1].imshow(image_without_nonmax)

key = cv2.waitKey(1)
if key & 0xFF == ord('q') or key == 27:
    cv2.destroyAllWindows()

# Print the number of keypoints detected in the training image
print("Number of Keypoints Detected In The Image With Non Max Suppression: ", len(keypoints_with_nonmax))


# Print the number of keypoints detected in the query image
#print("Number of Keypoints Detected In The Image Without Non Max Suppression: ", len(keypoints_without_nonmax))