import cv2
import numpy as np
from pyzbar.pyzbar import decode

image = cv2.imread('5f3c184f765977282084aebf_image.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
decoded_objects = decode(image)
print(decoded_objects)
for obj in decoded_objects:
    data = obj.data.decode('utf-8')
    print(f"QR Code Data: {data}")

cv2.imshow('Preprocessed Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
