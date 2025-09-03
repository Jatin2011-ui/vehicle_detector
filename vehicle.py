import cv2
import numpy as np  

#web camera 
cap = cv2.VideoCapture('video.mp4')

min_width_react = 80
min_height_react = 80

count_line_position = 550
#count_line_position = int(cap.get(3) * 0.55) #

#initaize subtractor 
algo = cv2.createBackgroundSubtractorMOG2()

counter = 0

def center_handle(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=x+x1
    cy=y+y1
    return (cx,cy)

detect = [] 
offset = 6 #allow error between pixel                

cv2.namedWindow("Video Original", cv2.WINDOW_NORMAL)
#cv2.setWindowProperty("Video Original", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


while True:
    ret, frame1 = cap.read()
    if not ret:
        break
    
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3,3),5)
    #applying on each frame 
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_OPEN, kernel)
    counterShape,h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#counting line 
    cv2.line(frame1, (25, count_line_position), (1800, count_line_position), (255, 127,3),3)

    for (i,c) in enumerate(counterShape):
        (x,y,w,h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_react) and (h >= min_height_react)
        if not validate_counter:
            continue

        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0),2)   
        cv2.putText(frame1, "VEHICLE COUNT: " +str(counter),(450,70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),5)

        center = center_handle(x,y,w,h)
        detect.append(center)
        cv2.circle(frame1, center,4,(0,0,255),-1)

        #for (cx, cy) in detect:
        #    if cy < (count_line_position + offset) and cy > (count_line_position - offset):
         #       counter += 1
          #  cv2.line(frame1,(25, count_line_position), (1800, count_line_position),(0,127,255),3)
     #   detect.remove((cx, cy)) # remove to double count
      #  print("Vehicle Counter: " + str(counter))
        for (cx, cy) in detect:
            if (count_line_position - offset) < cy < (count_line_position + offset):
                counter += 1
                cv2.line(frame1, (25, count_line_position), (1800, count_line_position), (0,127,255), 3)
                detect.remove((cx, cy))   # ✅ remove right here
                print("Vehicle Counter: " + str(counter))



    cv2.putText(frame1, "VEHICLE COUNT: " +str(counter),(450,70),
                 cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),5)


    #cv2.imshow('Detector', dilatada)

   #if not ret:
        #break
    
    cv2.imshow("Video Original", frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()        