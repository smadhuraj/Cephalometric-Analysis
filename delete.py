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

	# print(point_1_x,point_1_y)

	cv2.circle(img,(point_1_y, point_1_x), 5, (255,255,255), -1)
#####################################################################################################
findPo(edges) #call the function that find pogonion point on the skull
