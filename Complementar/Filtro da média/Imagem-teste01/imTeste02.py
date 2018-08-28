##########################################################################################
##########################################################################################
############################################# PDI ########################################
##########################################################################################
# Just opne imagem using cv2, matplotlib e cv2
#
# Navar M M N
# 02-10-2016
##########################################################################################
##########################################################################################
# Load necessary module
import cv2
import numpy as np
import matplotlib.pyplot as plt
##########################################################################################
# Open imagem:

#img = cv2.imread('lena.png',cv2.IMREAD_GRAYSCALE)

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)

    cv2.imshow('image 01', frame)
    cv2.imshow('image 02', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Plot image
#plt.imshow(cap, cmap='gray')
#plt.show()

"""
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""