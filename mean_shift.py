import cv2
import numpy as np

# video = cv2.VideoCapture('lenovo_box.avi') #From video clip
video = cv2.VideoCapture(0) #From webcam in real

# _, first_frame = video.read()
first_frame = cv2.imread("box.jpg", cv2.IMREAD_COLOR)

#Box logo coordinates 900,300 880,510
# x = 270
# y = 120
# width = 780
# height = 510
x = 510
y = 375
width = 230
height = 160
roi = first_frame[y: y + height, x : x + width]
#Back projection via HSV colorspace
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi],[0],None, [180],[0,180])
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

term_criteria = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 1000, 10)
#Meanshift algo


while True:

    _ , frame = video.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv],[1], roi_hist, [100,180],3)
    _, track_window = cv2.meanShift(mask,(x,y,width,height),term_criteria)
    x,y,w,h = track_window
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(frame,'Tablet Box', (x+180,y+200), cv2.FONT_ITALIC, 1, (0,140,255),2)
    print(track_window)
    # cv2.imshow("Roi",roi)
    cv2.imshow("Mask",mask)
    cv2.imshow("Frame",frame)

    key = cv2.waitKey(20) #Show a frame each () milisecond!
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()