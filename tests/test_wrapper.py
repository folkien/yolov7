'''
    Test of YOLOv7 wrapper
'''

import logging
import os
import sys
import time
import pytest
import cv2
from yolov7 import ModelYOLOv7

def test_model_loaddetect():
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
    assert(image is not None)

    # Image : save.
    cv2.imwrite('output.jpeg', image)

def test_model_fps_teoretical():
    ''' Test teoretical fps '''
    # Create yolov7
    model = ModelYOLOv7(path='zoo/yolov7coco/')
    assert (model.IsLoaded() == False)

    # Load model
    model.Init()
    assert (model.IsLoaded() == True)

    # Image : Load image
    image = cv2.imread('inference/images/bus.jpg')

    # Model : Detect objects in image
    startTime = time.time()
    for i in range(1000):
        detections = model.Detect(image)

    # FPS : Calculate
    endTime = time.time()
    fps = 1000 / (endTime - startTime)
    logging.info('FPS: %f.', fps)

    # FPS : Save in json file.
    with open('tests/test_model_fps_teoretical.json', 'w') as file:
        file.write('{"fps": %f}' % fps)

if __name__ == '__main__':
    test_model_fps_teoretical()
    test_model_loaddetect()