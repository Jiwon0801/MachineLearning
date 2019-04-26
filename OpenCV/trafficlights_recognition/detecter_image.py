import numpy as np
import cv2

def image_to_array(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def get_detect_image(image_path):
    image = image_to_array(image_path)
    image_ex = np.copy(image)
    
    # [1, None, None, 3] 형태가 되도록 차원 확대
    return image, np.expand_dims(image_ex, axis=0)