# CREATED BY: LEANDRO DANTE
# 08/10/2018

from PIL import Image
from pylab import *
import os
import pyautogui
import class_util 

IMAGE_PATH = 'C:/Users/leand/Desktop/DIP_OCR/OCR_DATABOOK/docs_show'
def analysisAlgorithimic(IMAGE_NAME,LEVEL,IMAGE_FORMAT):
    px_return = 0

    IMAGE_OUTPUT = IMAGE_NAME + '_tmp.png'
    IMAGE_ANALYSIS = IMAGE_NAME + IMAGE_FORMAT
    os.chdir(IMAGE_PATH)
    im = array(Image.open(IMAGE_ANALYSIS).convert('L'))
    figure()
    contour(im, levels=[LEVEL], colors='#00ff00', origin='image')
    axis('equal')
    savefig(IMAGE_OUTPUT, bbox_inches='tight')
    im = Image.open(IMAGE_OUTPUT)
    px_count = 0
    for pixel in im.getdata():
        if pixel == (0,255,0,255):
            px_count += 1
        else:
            pass
    px_return = px_count
    #print(px_return)
    return px_return

def matchArray(array):
    arrayFixed = class_util.Array()

def find_nearest(array, value):
    array = numpy.asarray(array)
    idx = (numpy.abs(array - value)).argmin()
    return idx
    
