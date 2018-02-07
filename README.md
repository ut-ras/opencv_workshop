# OpenCV Workshop
Example code and installation instructions for an OpenCV workshop. This workshop is designed to be performed as a live coding exercise that builds up to 6_object_tracking_basic.py line by line. The attached slides were used during the first iteration of this workshop and may be helpful for future iterations.

## Installing OpenCV

### Mac:

Read the [instructions file](https://github.com/ut-ras/opencv_workshop/blob/master/macos_installation_instructions).

### Windows:

First you'll need to get python. Click [this link](https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi) and run the installer it downloads. When you get to the step that looks like this:

![Oh hi there](https://i.imgur.com/TdE9t9M.png)

Make sure you enable the option to Add python.exe to Path. Other than that the default options are fine. Hit next until it closes.

Now open up a command prompt and enter `python -V`. If it says "Python 2.7.14", you're all good.

Next we can use pip to install OpenCV and its dependencies. In the command prompt enter
```
pip install numpy
pip install matplotlib
pip install opencv-python
```
and hopefully everything will have installed correctly. To test it, start python (just type python in the command prompt) and enter these lines:
```
import numpy
import matplotlib
import cv2
```
If nothing happens... you did everything right! OpenCV and python are ready to go on your computer.
