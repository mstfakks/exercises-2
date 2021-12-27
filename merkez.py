# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:34:03 2021

@author: MUSTAFA
"""

import cv2
import numpy as np
import utm





image = cv2.imread("C:\\Users\\MUSTAFA\\Desktop\\cim.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)

contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

blank = np.zeros(thresh.shape[:2], dtype='uint8')

cv2.drawContours(blank, contours, -1, (255, 0, 0), 1)


for i in contours:
	M = cv2.moments(i)
	if M['m00'] != 0:
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
	print("Kırmızı alanın merkez x koordinatı: ",cx,"\nKırmızı Alanın Merkez y koordinatı: ",cy)
    
ref_lat = 40.996207
ref_lon = 29.060491
x, y, zone, ut = utm.from_latlon(ref_lat,ref_lon)
print(x,y,zone,ut)


cx_m = cx * 0.0102645833
cy_m = cy * 0.0102645833

lat,lon = utm.to_latlon(cx_m+x , cy_m+y, zone, ut)
print(lat,lon)






    
