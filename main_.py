from trajectory import trej
from detect import get_image_coordinates
from mapping import robot_map


import cv2
import os
import time


def capture_image():

    cap = cv2.VideoCapture(0)            # video capture source camera (Here webcam of laptop) 
    ret,frame = cap.read()               # return a single frame in variable `frame`
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 820)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 660)
  
                                          #cv2.imshow('img1',frame) #display the captured image
    cv2.waitKey(1) 
    cv2.imwrite('images_1/test.jpg',frame)
     
    
    cap.release()






def main():
    ''' 
    main code executes capaturing of a image, mapping and trajectory
    
    
    
    '''


    path='./images_1/'
    capture_image()
    coord = get_image_coordinates(path)
    os.remove(path+'test.jpg')
    final_locations = robot_map(coord)  # get locations of the objects in robot perspective
    trej(final_locations)
    print('task done')

   
