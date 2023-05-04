'''
    Setup file for the package creation.
'''
import os
import setuptools

# Read package README as long description
with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# Setuptools setup
setuptools.setup(
    name='yolov7wrapper',
    version='0.0.1',
    description='Wrapper for YOLOv7 model and original code',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/folkien/yolov7wrapper',
    author='Sławomir Paszko',
    author_email='kontakt@aisp.pl',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    packages=setuptools.find_packages(exclude=['tests','env3.11','env3.8']),
)