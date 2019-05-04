# Using OpenCV library, PySerial library and Numpy .


import cv2
import numpy as np
import serial


def nothing(x):
    pass

# Serial Connection to communicate Arduino


ser = serial.Serial('COM8', 38400)

# Decide what Camera to USE :

# cap = cv2.VideoCapture('http://192.168.1.2:8080/video')
cap = cv2.VideoCapture(0)

# Using TrackBars To adjust the required HSV values needed for the desired Color

cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)

cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)

cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)

cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)

cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)

cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)


while True:
    # reading the video into frames
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - H", "Trackbars")

    l_s = cv2.getTrackbarPos("L - S", "Trackbars")

    l_v = cv2.getTrackbarPos("L - V", "Trackbars")

    u_h = cv2.getTrackbarPos("U - H", "Trackbars")

    u_s = cv2.getTrackbarPos("U - S", "Trackbars")

    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

# Using the Lower And Upper Blue range HSV

    lower_blue = np.array([l_h, l_s, l_v])

    upper_blue = np.array([u_h, u_s, u_v])

    # The Frames needed for the operation

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Edge Detection Using Canny function

    edges = cv2.Canny(mask, 100, 200)

    # Convert RGB Frame To Gray Scale

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 127, 255, 0)


# Using Erosion And Dilation Cases to reduce the Noise:

    # Case 1:

    # kernel = np.ones((25, 25), np.uint8)

    # erosion = cv2.erode(result, kernel, iterations=12)

    # dilation = cv2.dilate(result, kernel, iterations=10)

    # Case 2: Worked better Opening And Closing

    kernel = np.ones((15, 15), np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Finding Contours Using find_contour function

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    # cnt = contours[0]

# Using Center to determine the Circle

    center = None

    # only proceed if at least one contour was found

    if len(contours) > 0:

        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid

        c = max(contours, key=cv2.contourArea)

        ((x, y), radius) = cv2.minEnclosingCircle(c)

        M = cv2.moments(c)

        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size

        if radius > 40:

            # draw the circle and centroid on the frame,
            # then update the list of tracked points

            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 3)

            cv2.circle(frame, center, 3, (0, 0, 255), -1)

            cv2.putText(frame, "centroid", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

            cv2.putText(frame, "(" + str(center[0]) + "," + str(center[1]) + ")", (center[0] + 10, center[1] + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

            if ( x > 200 and x < 400 and y > 200 and y < 400):

                # Stop The Motor
                  ser.write(b'S')

                  cv2.circle(frame, (10,10), 20, (0, 0, 255), 3)

            else:

                # Power the Motor

                  cv2.circle(frame, (10, 10), 20, (255, 0, 0), 3)

                  ser.write(b'P')

# Approximation technique fot the contour

    # epsilon = 0.1 * cv2.arcLength(cnt, True)

    # approx = cv2.approxPolyDP(cnt, epsilon, True)

# Drawing Contours

    con = cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

# Showing Results

    cv2.imshow("frame", frame)

    cv2.imshow("contour", mask)

    cv2.imshow("result", result)

    cv2.imshow("edge", edges)

# halt the Operation when Press "ESC"

    key = cv2.waitKey(1)

    if key == 27:

        break


cap.release()

cv2.destroyAllWindows()