import cv2
import numpy as np
import math

class Manual:
	
	def xxx():
		lst_x = [None] * 4
		lst_y = [None] * 4
		imgColor = cv2.imread('scull.jpg',1)
		def set_point(event, x, y, flags, params):
			if event == cv2.EVENT_LBUTTONDOWN:#when click set the point to the fixed length array ( for 4 point)
				if lst_x[0] == None:
					lst_x[0] = y# when clicking return the possion cordinte as (y,x)
					lst_y[0] = x# therefore x and y have been interchanged 

				elif lst_x[1] == None:
					lst_x[1] = y
					lst_y[1] = x

				elif lst_x[2] == None:
					lst_x[2] = y
					lst_y[2] = x

				else:
					lst_x[3] = y
					lst_y[3] = x
					m1 = (lst_y[1]-lst_y[0])/(lst_x[1]-lst_x[0])#angle between pog and N point
					
					m2 = (lst_y[1]-lst_y[2])/(lst_x[1]-lst_x[2])#angle between N and B point
					
					m3 = (lst_y[1]-lst_y[3])/(lst_x[1]-lst_x[3])# angle between N and A point
					theeta_pnb = math.atan((m1-m2)/(1+(m1*m2)))
					theeta_pna = math.atan((m1-m3)/(1+(m1*m3)))

					print(abs(math.degrees(theeta_pnb)))
					print(abs(math.degrees(theeta_pna)))

					cv2.destroyAllWindows()
					drowLine(lst_x, lst_y)
				
				

		def drowLine(arr_x, arr_y):	
			cv2.line(imgColor, (arr_y[0], arr_x[0]), (arr_y[1], arr_x[1]), (0, 0, 255), thickness=1, lineType=8)
			cv2.line(imgColor, (arr_y[1], arr_x[1]), (arr_y[2], arr_x[2]), (0, 0, 255), thickness=1, lineType=8)
			cv2.line(imgColor, (arr_y[1], arr_x[1]), (arr_y[3], arr_x[3]), (0, 0, 255), thickness=1, lineType=8)
			cv2.imshow('final image', imgColor)
			cv2.waitKey(0)
			cv2.destroyAllWindows()

		def setImage():

			img = cv2.imread('scull.jpg',cv2.IMREAD_GRAYSCALE)
			laplacian = cv2.Laplacian(img,cv2.CV_64F)#inbuild funtion
			cv2.imshow('laplacian',laplacian)

			cv2.namedWindow("laplacian")
			cv2.setMouseCallback("laplacian", set_point)

		setImage()

	

		# def laplacianFunction(mat):#created funtion for laplacian filter
		# 	ker_h = 3
		# 	ker_w = 3
		# 	kernal = np.array([[0,1,0],
		# 					[1,-4,1],
		# 					[0,1,0]])

		# 	img_con = np.zeros(img.shape)

		# 	for i in range(1,height-1):
		# 		for j in range(1,width-1):
		# 			sum = 0

		# 			for m in range(ker_h):
		# 				for n in range(ker_w):
		# 					sum = sum + kernal[m][n]*img[i-1+m][j-1+n]
		# 			img_con[i][j] = sum

		# 	return img_con


		
