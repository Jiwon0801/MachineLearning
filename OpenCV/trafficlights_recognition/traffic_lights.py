import numpy as np
from PIL import Image
from detecter_image import get_detect_image
from detecter import Detecter
import cv2

# 테스트 이미지 파일 리스트
TEST_IMAGE_PATHS = [ './test_images/image9.jpg']
THRESHOLD = 0.3

detecter = Detecter()
detecter.setup('./frozen_inference_graph.pb', './mscoco_label_map.pbtxt')

def getCropImage(object_list, image):

    height, width, _  = image.shape
    sub_image = []

    for ix, obj in enumerate(object_list):
        box = obj[0]
        (ymin, xmin, ymax, xmax) = (int(box[0]*height), int(box[1]*width), 
                                    int(box[2]*height), int(box[3]*width))
        sub_image.append(image[ymin:ymax, xmin:xmax])

    return sub_image

##### Crop
for image_path in TEST_IMAGE_PATHS:
    image, image_ex = get_detect_image(image_path)
    #print(image.shape, image_ex.shape)
    (boxes, scores, classes, num) = detecter.detect(image_ex)
    #print('object num',num)


    #일반 방법
    object_list = []
    for output in zip (boxes, scores, classes):
        if( output[1] > THRESHOLD and output[2]==10):
            object_list.append(output)
            print(output)

    
    sub_image = getCropImage(object_list, image)


##### Color    
    i=1
    for ix, image in enumerate(sub_image):
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        h, s, v = cv2.split(hsv)

        lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
        upper_red = cv2.inRange(hsv, (170, 100, 100), (180, 255, 255))
        added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)

        h_yellow = cv2.inRange(h, 8, 30)
        h_green = cv2.inRange(h, 45, 80)

        red = cv2.bitwise_and(hsv, hsv, mask=added_red)
        red = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)
        
        yellow = cv2.bitwise_and(hsv, hsv, mask=h_yellow)
        yellow = cv2.cvtColor(yellow, cv2.COLOR_HSV2BGR)

        green = cv2.bitwise_and(hsv, hsv, mask=h_green)
        green = cv2.cvtColor(green, cv2.COLOR_HSV2BGR)

        # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # cv2.imshow('yellow{}'.format(i), yellow)

        if ix == 1:
            cv2.imshow('yellow{}'.format(i), yellow)
            cv2.imshow('red{}'.format(i), red)   
            cv2.imshow('green{}'.format(i), green)
           
        i=i+1

        cv2.imwrite("./saved_image_yellow.jpg", yellow)
        cv2.imwrite("./saved_image_red.jpg", red)
        cv2.imwrite("./saved_image_green.jpg", green)



##### Circle
img = cv2.imread('./saved_image_green.jpg', 0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1,20,param1=50,param2=50,minRadius=10,maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.imwrite("./saved_circle_image_green.jpg", cimg)
    
    
cv2.waitKey()
cv2.destroyAllWindows()

