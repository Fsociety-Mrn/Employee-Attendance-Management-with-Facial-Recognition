import cv2
import numpy as np
import urllib.request

url='http://192.168.100.61/1600x1200.jpg' # esp url

import cv2


def cam(name): 
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")
    img_counter = 0
    
    while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgnp,-1)
        imgS = cv2.resize(img,(0,0),None,0.50,0.50)
        frame = cv2.flip(imgS, 1) # Flip camera vertically


        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            
            cam.release()
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "imgs/" + name + ".png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            cv2.waitKey()
            cv2.destroyAllWindows()
            img_counter +=1


    cam.release()
    cv2.destroyAllWindows()
    