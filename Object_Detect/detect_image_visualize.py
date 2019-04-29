import numpy as np
from PIL import Image
from detecter_image import get_detect_image
from detecter import Detecter
import cv2.cv2

# 테스트 이미지 파일 리스트
TEST_IMAGE_PATHS = [ './test_images/image7.jpg']
THRESHOLD = 0.3

detecter = Detecter()
detecter.setup('./frozen_inference_graph.pb', './mscoco_label_map.pbtxt')

for image_path in TEST_IMAGE_PATHS:
    image, image_ex = get_detect_image(image_path)
    (boxes, scores, classes, num) = detecter.detect(image_ex)
    print('object num', num)
    (boxes, scores, classes) = (np.squeeze(boxes), np.squeeze(scores), np.squeeze(classes).astype(np.uint8))

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    detecter.visualize(image, boxes, classes, scores, THRESHOLD)
    cv2.imshow(image_path, image)


cv2.waitKey()
cv2.destroyAllWindows()

