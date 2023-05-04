''' 
    Test packaged version of the module.

'''
import os
import pytest
from yolov7wrapper.wrapper import ModelLoad, ModelDetect, DrawDetections, Cv2ImageToNetworkInput


def test_yolov7_coco():
    ''' Test of loading yolov7. '''
    # Load yolov7 model
    model = ModelLoad(directoryPath='yolov7wrapper/zoo/yolov7coco/',
                                    modelFilename='yolov7.pt',)
    assert(model is not None)

if __name__ == '__main__':
    test_yolov7_coco()