import cv2
import numpy as np
import imutils
from scipy.ndimage import rotate
from matplotlib import pyplot as plt
from canny import Newclass

class Main:

    path ="C:/Users/Shashintha Madhuraj/Desktop/python/project/img/scull.jpg" 

    def mainMehod(path):
        img = cv2.imread(path,0)# read the X ray image in gray scale
        img_1 = cv2.imread(path,1)
        edges = cv2.Canny(img,100,200) # apply Canny filter to loded image

        left_x, left_y = Newclass.findExLeft(edges)#find the extream left point of the image
        right_x, right_y = Newclass.findExtRight(edges)#find the extream right point of the image

        pog_y, pog_x = Newclass.findPogPoint(img, left_y, right_y)

        N_point_x, N_point_y = Newclass.findNPoint(edges, right_x, right_y)

        cv2.line(img_1, (pog_y, pog_x), (N_point_y, N_point_x), (0, 0, 255), thickness=1, lineType=8)#draw line between POG and N        

        cv2.imshow("result image", img_1)

        Newclass.findBPoint(img, edges)
     

