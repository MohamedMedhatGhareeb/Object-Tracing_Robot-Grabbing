
import cv2
import numpy as np


img = cv2.imread('2d images/aa.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
cnt = contours[0]

epsilon = 0.1*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

con = cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)

#hull = cv2.convexHull(con)

cv2.imshow('counter', con)
cv2.imshow('binary', thresh)


M = cv2.moments(cnt)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx, cy)


#cv2.imshow('approxe', epsilon)
cv2.waitKey(0)
cv2.destroyAllWindows()

