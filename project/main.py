import cv2
import numpy as np

def set_point(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x,y)

cv2.namedWindow("laplacian")
cv2.setMouseCallback("laplacian", set_point)


img = cv2.imread('scull.jpg',cv2.IMREAD_GRAYSCALE)
sample_1 = cv2.imread('sample_1.png',cv2.IMREAD_GRAYSCALE)#sample_1 read
edges = cv2.Canny(img,100,200)

laplacian = cv2.Laplacian(img,cv2.CV_64F)#inbuild funtion
height = np.size(img, 0)
width = np.size(img, 1)

count =0

for x in range(1,59):
	for y in range(1,59):
		if sample_1[x][y] == 255:
			count = count+1

print(count)## of ones in sample_1 (black pixels)



def laplacianFunction(mat):#created funtion for laplacian filter
	ker_h = 3
	ker_w = 3
	kernal = np.array([[0,1,0],
					   [1,-4,1],
					   [0,1,0]])

	img_con = np.zeros(img.shape)

	for i in range(1,height-1):
		for j in range(1,width-1):
			sum = 0

			for m in range(ker_h):
				for n in range(ker_w):
					sum = sum + kernal[m][n]*img[i-1+m][j-1+n]
			img_con[i][j] = sum

	return img_con


newImage = laplacianFunction(img)

cv2.imshow('laplacian',newImage)
cv2.imshow('img2',img)

# cv2.imshow('sample_1',sample_1)
# cv2.imshow('img',laplacian)


height = np.size(img, 0)
width = np.size(img, 1)

print(height)
print(width)

h = int(height/2)
w = int(width/2)

a = np.zeros([h, w]) 

Matrix_1 = np.zeros(a.shape)
Matrix_2 = np.zeros(a.shape)
Matrix_3 = np.zeros(a.shape)
Matrix_4 = np.zeros(a.shape)
Matrix_1_lap = np.zeros(a.shape)
Matrix_2_lap = np.zeros(a.shape)
Matrix_3_lap= np.zeros(a.shape)
Matrix_4_lap = np.zeros(a.shape)

for i in range(1,height-1):
	for j in range(1,width-1):
		if i<h and j<w:
			Matrix_1[i][j] = edges[i][j]
			Matrix_1_lap[i][j] = newImage[i][j]
		elif i<h and j>w:
			Matrix_2[i][j-w] = edges[i][j]
			Matrix_2_lap[i][j-w] = newImage[i][j]
		elif i>h and j<w:
			Matrix_3[i-h][j] = edges[i][j]
			Matrix_3_lap[i-h][j] = newImage[i][j]
		else:
			Matrix_4[i-h][j-w] = edges[i][j]
			Matrix_4_lap[i-h][j-w] = newImage[i][j]
# print(width,heigth)
cv2.imshow('4-1',Matrix_4)
cv2.imshow('4-1_lap',Matrix_4_lap)

for i in range(1,h-1):
	for j in range(w-1,1):
		print(Matrix_4[i][j])
		 



cv2.imshow('canny',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
