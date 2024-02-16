import cv2
import matplotlib.pyplot as plt

# Read an image from file
img = cv2.imread('image.jpg')

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
