import cv2


def cam(name): 
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")
    img_counter = 0
    while True:
        ret, img = cam.read()
        frame = cv2.flip(img, 1) # Flip camera vertically
        if not ret:
            print("failed to grab frame")
            break
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
    

cam("TimeIn")
    
