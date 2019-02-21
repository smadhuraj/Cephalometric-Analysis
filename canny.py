import cv2
import numpy as np
import imutils
import random
from scipy.ndimage import rotate
from matplotlib import pyplot as plt


class Newclass:

	###################################################################
	def findExtRight(edges):# find Right extream point from the canny filtered image
		height = np.size(edges, 0)# get height of the image
		width = np.size(edges, 1)# get width of the image
		extRigth_x = 0
		extRigth_y = 0
		rotate_img = rotate(edges, 90)
		for a in range(35,width-1): # some X ray has scall in right top corner  between  0-35 pixel
			for b in range(1,height-1):
				if rotate_img[a][b] == 255:
					extRigth_x = a
					extRigth_y = b
					break
			if extRigth_x !=0 or extRigth_y !=0:
				break
		point_3_x = extRigth_y
		point_3_y = width - extRigth_x

		return point_3_x, point_3_y
	#############################################
	def findExLeft(edges):# find left extream point from the canny filtered image 
		extLeft_x = 0
		extLeft_y = 0
		height = np.size(edges, 0)# get height of the image
		width = np.size(edges, 1)# get width of the image
		rotate_img = rotate(edges, 270)
		for a in range(1 ,width-1):
			for b in range(1,height-1):
				if rotate_img[a][b] == 255:
					extLeft_x = a
					extLeft_y = b
					break
			if extLeft_x !=0 or extLeft_y !=0:
				break
		# print('new')
		# print(extLeft_x, extLeft_y)

		point_2_x = height-extLeft_y
		point_2_y = extLeft_x

		return point_2_x, point_2_y

	#############################################

	def findPogPoint(img, y_1, y_2):
		height = np.size(img, 0)
		y = int(y_1 +(y_2 - y_1)/2) # pogonian X coordinate  of the skul is placed above exacty between extream right point and extream left point
		k = 0
		for i in range(1,height):# to find pogonian Y coodinate go top to buttom throught Y (IN ABOVE MENTION*******) 
			if img[i][y] > 250:
				k = i
				break
		return y, k


	#############################################
	#find N point of the skull (top of the nose)
	def findNPoint(edges, x_2, y_2):

		test_point = y_2
		return_point_x = 0
		return_point_y = 0
		height = np.size(edges, 0)# get height of the image
		width = np.size(edges, 1)# get width of the image
		for i in range(x_2, height-1):
			for j in range(test_point-3, test_point+3):
				if edges[i+1][j] == 255:
					test_point = j
					# print(j)
					break
					
				if j == test_point + 2 and edges[i+1][j] == 0:
					return_point_y = j-3
					return_point_x = i-1
					break

			if return_point_x != 0:
				break
		return return_point_x, return_point_y

	############################################

	def findBPoint(newImage):

		height = np.size(newImage, 0)# get height of the image
		width = np.size(newImage, 1)# get width of the image
		h = int(height/2)
		w = int(width/2)
		crop_img = newImage[h:h+h, w:w+w]
		crop_img = rotate(crop_img, 180)
		
		res = False
		for i in range(1, h):
			for j in range(1, w):
				if crop_img[i][j] > 180:
					bot_x = i
					bot_y = j
					
					res = True
					break
			if res == True:
				break
		crop_img = rotate(crop_img, 180)
		bot_x = h - bot_x
		bot_y = w - bot_y
		return_x = 0
		return_y = 0
		res = False
		for y in range(bot_y,bot_y+50):
			for x in range(bot_x-80,bot_x):
				if crop_img[y][x] < 160:
					# cv2.circle(crop_img,(y, x), 5, (255,255,255), -1)
					return_x = x
					return_y = y
					print(x,y)
					res = True
					break
			if res == True:
				break

		return return_x, return_y
		
	############################################
	

	def showImg(img_1, edges):
	
		cv2.imshow('img',edges)# show canny filtered image
		cv2.imshow('img_1',img_1)# show input image (X ray image)

		cv2.waitKey(0)
		cv2.destroyAllWindows() # wait until some key is press.....
		# THE END



