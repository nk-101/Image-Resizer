import cv2

#Configuration parameters
source="harry.jpg"
destination="newImage.jpeg"

#percent by which image is resized
scale_percent = 50

src=cv2.imread("harry.jpg",cv2.IMREAD_UNCHANGED)
#cv2.imshow("title",src)

#calculate the 50 percent of original dimensions
new_width=int(src.shape[1]*scale_percent/100)
new_height=int(src.shape[0]*scale_percent/100)

dsize=(new_width,new_height)

#resize image
output=cv2.resize(src,(new_width,new_height))

cv2.imwrite(destination,output)
#cv2.waitKey(0)


'''
import cv2

src=cv2.imread("harry.jpg",cv2.IMREAD_UNCHANGED)
#cv2.imshow("title",src)

scale_percent = 50

new_width=int(src.shape[1]*scale_percent/100)
new_height=int(src.shape[0]*scale_percent/100)

dsize=(new_width,new_height)

output=cv2.resize(src,(new_width,new_height))

cv2.imwrite('new_image.png',output)
cv2.waitKey(0)
'''