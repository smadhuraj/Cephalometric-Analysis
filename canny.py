import cv2
import numpy as np
import imutils
from scipy.ndimage import rotate
from matplotlib import pyplot as plt


img = cv2.imread('scull.jpg',cv2.IMREAD_COLOR)
edges = cv2.Canny(img,100,200)

height = np.size(img, 0)
width = np.size(img, 1)


extRigth_x = 0
extRigth_y = 0
extLeft_x = 0
extLeft_y = 0

# detecting extream top point of the image
def findPo(edges):##################################################################################
	extTop_x=0 #extream top  point of the skul X
	extTop_y=0 #Y coodinate
	for i in range(1,height):
		for j in range(1,width):
			if edges[i][j] == 255:
				extTop_x = i
				extTop_y = j			
				break
		if extTop_x != 0 or extTop_y != 0:
			break	
	z =0
	for i in range(extTop_y,extTop_y+200):
		if edges[extTop_x][i] != 255 and edges[extTop_x][i+1] != 255:
			z=i
			break

	point_1_y = int(z-(z-extTop_y)/2)

	point_1_x = 0

	for j in range(extTop_x+30,height):
		if edges[j][point_1_y] == 255:
			point_1_x = j
			break

	print(point_1_x,point_1_y)

	cv2.circle(img,(point_1_y, point_1_x), 5, (255,255,255), -1)
#####################################################################################################
findPo(edges) #call the function that find pogonion point on the skull

#detecting extream right corner of the image
rotate_img = rotate(edges, 90)
for a in range(35,width-1):
	for b in range(1,height-1):
		if rotate_img[a][b] == 255:
			extRigth_x = a
			extRigth_y = b
			break
	if extRigth_x !=0 or extRigth_y !=0:
		break

print(extRigth_x, extRigth_y)

point_3_x = extRigth_y
point_3_y = width - extRigth_x
cv2.circle(edges,(point_3_y, point_3_x), 5, (255,255,255), -1)
#############################################

rotate_img = rotate(edges, 270)
for a in range(1 ,width-1):
	for b in range(1,height-1):
		if rotate_img[a][b] == 255:
			extLeft_x = a
			extLeft_y = b
			break
	if extLeft_x !=0 or extLeft_y !=0:
		break
print('new')
print(extLeft_x, extLeft_y)

point_2_x = height-extLeft_y
point_2_y = extLeft_x

print(point_2_x, point_2_y)
cv2.circle(edges,(point_2_y, point_2_x), 5, (255,255,255), -1)
#############################################
y = int(point_2_y +(point_3_y - point_2_y)/2)
cv2.circle(edges,(y, point_2_x), 5, (255,255,255), -1)
print(y)

for i in range(1,height):
	print(i, img[i][point_2_y])

cv2.imshow('img',edges )
cv2.imshow('img_1',img )
# cv2.imshow('scull image',edges)
# cv2.imshow('scull image_rotate',rotate_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

