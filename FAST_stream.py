import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(1)

# Create a FAST object with default parameters
fast = cv2.FastFeatureDetector_create()

# Get the default parameter values
print("Threshold:", fast.getThreshold())
print("Non-max Suppression:", fast.getNonmaxSuppression())
print("Type:", fast.getType())

while True:
    check, frame = cap.read()
    # Convert image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Display original and gray image using OpenCV
    cv2.imshow('original', image)

    # Detect keypoints with non-max suppression
    keypoints_with_nonmax = fast.detect(gray, None)

    image_with_nonmax = np.copy(image)

    # Draw keypoints on top of the input image
    cv2.drawKeypoints(image, keypoints_with_nonmax, image_with_nonmax, color=(0, 255, 0),
                    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Display images with non-max suppression
    cv2.imshow('image_with_nonmax', image_with_nonmax)
    print("Number of Keypoints Detected In The Image With Non Max Suppression: ", len(keypoints_with_nonmax))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
