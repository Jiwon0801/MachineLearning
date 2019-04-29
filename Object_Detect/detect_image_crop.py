import numpy as np
from PIL import Image
from detecter_image import get_detect_image
from detecter import Detecter
import cv2

# 테스트 이미지 파일 리스트
TEST_IMAGE_PATHS = [ './test_images/image7.jpg']
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

    
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    sub_image = getCropImage(object_list, image)
    cv2.imshow('sub_image',sub_image[0])
    

cv2.waitKey()
cv2.destroyAllWindows()

