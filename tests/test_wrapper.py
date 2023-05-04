'''
    Test of YOLOv7 wrapper
'''

import os
import sys
import pytest
import cv2
from yolov7 import ModelYOLOv7

def test_model_load():
    ''' Test wrapper load '''

    # Create yolov7
    model = ModelYOLOv7(path='zoo/yolov7coco/')
    assert (model.IsLoaded() == False)

    # Load model
    model.Init()
    assert (model.IsLoaded() == True)

    # Image : Load image
    image = cv2.imread('inference/images/bus.jpg')

    # Model : Detect objects in image
    detections = model.Detect(image)
    assert(len(detections) != 0)

    # Image : Draw detections
    image = model.Draw(image, detections)

    # Image : save.
    cv2.imwrite('output.jpeg', image)


if __name__ == '__main__':
    test_model_load()