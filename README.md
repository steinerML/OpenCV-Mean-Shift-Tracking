# OpenCV Object Tracking using Mean-Shift algorithm.
### Object Tracking 

In this short coding exercise I have used a basic tracking algorithm of OpenCV called Mean Shift that is mainly used for object tracking, despite having certain limitations when it comes to the bounding rectangle and the total lack of responsiveness when it comes to 'following' the tracked object when the lighting conditions change. 

These are - in a nutshell - the main steps I took to put this small experiment together:

+ **Define Region of Interest (ROI) (Lenovo tablet box)**
+ **Set ROI coordinates**
+ **Set HSV Region of interest**
+ **Initialize mask**
+ **Set tracking window coordinates**
+**Define TermCriteria settings**
+ **Initialize Mean Shift algorithm**
+ **Overall checks**

![Source Image Sequence](box_general.gif)
## Summary : 
Below a summary of the main functions used with the Mean Shift algorithm:

| Function            |Action                                                                        |
|:--------------------|------------------------------------------------------------------------------|
|**cv2.cvtColor()**|Transform ROI into HSV colorspace.|
|**cv2.calcHist()**   |Initialize calculation history with HSV ROI.|
|**cv2.normalize()**|Normalize track window values within 0-255 range.|
|**cv2.TermCriteria_EPS() | cv2.TermCriteria_COUNT()**    | Algorithm termination criteria settings|
|**cv2.calcBackProject()**    | Back Projection settings.|
|**cv2.meanShift()**    | Initialize Mean Shift algorithm.|

## Issues:
The limitations behind the Mean Shift algorithm are pretty clear and self-evident after running the algorithm and focusing on several critical frames where the algorithm terribly fails at tracking. Although several issues can be spotted right away once we run the program, mainly related with the tracking phase and the fact that the bounding rectangle is not adapting to the object size nor the .
![Source Image Sequence](box_popup.gif)
## Summary:

```python
# Define first frame
cv2.imread("box.jpg", cv2.IMREAD_COLOR)
```
```python
# Set ROI coordinates
x = 510
y = 375
width = 230
height = 160
roi = first_frame[y: y + height, x : x + width]
```

```python
# Color space conversion to HSV
cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
```
```python
#Backprojection calcHist
cv2.calcHist([hsv_roi],[0],None, [180],[0,180])
```
```python
#Normalize track window values (0-255)
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
```
```python
#Termination criteria values
term_criteria = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 1000, 10)
```
