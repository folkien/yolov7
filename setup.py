'''
    Setup file for the package creation.
'''
import os
import setuptools


with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name='yolov7-wrapper',
    version='0.0.1',
    author='Sławomir Paszko',
    description='Wrapper for YOLOv7 model and original code',
    python_requires='>=3.8',
    packages=setuptools.find_packages(exclude=['tests','env3.11']),
)