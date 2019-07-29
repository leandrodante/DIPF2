# CREATED BY: LEANDRO DANTE
# 08/10/2018
import functions
import numpy
import class_util
from PIL import Image
from scipy.misc import imsave
import numpy
import webbrowser
import pytesseract
import time
import pyautogui
import matplotlib.pyplot as plt
import os
from statistics import mode

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
DIR_NAME = 'C:/Users/leand/Desktop/DIP_OCR/OCR_DATABOOK/docs_show'
IDX_FILE = 1
files = os.listdir(DIR_NAME)
files = sorted(files)

def get_parser():
    """Get parser object for script xy.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--in",
                        dest="name",
                        help="read this file",
                        metavar="FILE",
                        required=True)
    parser.add_argument("-f", "--if",
                        dest="format",
                        help="write binarized file hre",
                        metavar="FILE",
                        required=True)
    return parser

def find_nearest(array, value):
    array = numpy.asarray(array)
    idx = (numpy.abs(array - value)).argmin()
    return idx

#args = get_parser().parse_args()
#
#IMAGE_NAME = args.name
#IMAGE_FORMAT = args.format

pxs = []

arrayFixed = class_util.Array()

for fileu in files:
    pxs = []
    IMAGE_NAME,IMAGE_FORMAT = fileu.split(".")
    pxs.append(functions.analysisAlgorithimic(IMAGE_NAME,100,"."+IMAGE_FORMAT)/10)
    pxs.append(functions.analysisAlgorithimic(IMAGE_NAME,120,"."+IMAGE_FORMAT)/10)
    pxs.append(functions.analysisAlgorithimic(IMAGE_NAME,150,"."+IMAGE_FORMAT)/10)
    pxs.append(functions.analysisAlgorithimic(IMAGE_NAME,170,"."+IMAGE_FORMAT)/10)
    pxs.append(functions.analysisAlgorithimic(IMAGE_NAME,200,"."+IMAGE_FORMAT)/10)
    pxs.append(functions.analysisAlgorithimic(IMAGE_NAME,220,"."+IMAGE_FORMAT)/10)
    pxs.append(functions.analysisAlgorithimic(IMAGE_NAME,250,"."+IMAGE_FORMAT)/10)
    print(IMAGE_NAME)
    print(pxs)

    x = [100,120,150,170,200,220,250]


    function = numpy.polyfit(x, pxs, 6)
    print(function)

    results = []

    print(find_nearest(arrayFixed.col1,function[1-1]), end=" ")
    results.append(find_nearest(arrayFixed.col1,function[1-1]))
    print(find_nearest(arrayFixed.col2,function[2-1]), end=" ")
    results.append(find_nearest(arrayFixed.col2,function[2-1]))
    print(find_nearest(arrayFixed.col3,function[3-1]), end=" ")
    results.append(find_nearest(arrayFixed.col3,function[3-1]))
    print(find_nearest(arrayFixed.col4,function[4-1]), end=" ")
    results.append(find_nearest(arrayFixed.col4,function[4-1]))
    print(find_nearest(arrayFixed.col5,function[5-1]), end=" ")
    results.append(find_nearest(arrayFixed.col5,function[5-1]))
    print(find_nearest(arrayFixed.col6,function[6-1]), end=" ")
    results.append(find_nearest(arrayFixed.col6,function[6-1]))
    print(find_nearest(arrayFixed.col7,function[7-1]))
    results.append(find_nearest(arrayFixed.col7,function[7-1]))
    print("RESULTS:")
    print(mode(results))
    result = mode(results)
    print(arrayFixed.tipo[result])
    print("_________________________________")


    #i = 1
    #for coe in function:
    #    #print(format(coe,'.40f'))
    #    if i == 1:
    #        col1_tmp.append(coe)
    #    elif i == 2:
    #        col2_tmp.append(coe)
    #    elif i == 3:
    #        col3_tmp.append(coe)
    #    elif i == 4:
    #        col4_tmp.append(coe)
    #    elif i == 5:
    #        col5_tmp.append(coe)
    #    elif i == 6:
    #        col6_tmp.append(coe)
    #    elif i == 7:
    #        col7_tmp.append(coe)
    #
    #    i = i + 1

    
    IDX_FILE = IDX_FILE + 1
    plt.close("all")


    #
    #print(find_nearest(arrayFixed.col1,9.04508547*pow(10,-9)))
    #print(find_nearest(arrayFixed.col2,-9.65131777*pow(10,-6)))
    #print(find_nearest(arrayFixed.col3,4.18875482*pow(10,-3)))
    #print(find_nearest(arrayFixed.col4,-9.45177644*pow(10,-1)))
    #print(find_nearest(arrayFixed.col5,1.16716447*pow(10,2)))
    #print(find_nearest(arrayFixed.col6,-7.45453313*pow(10,3)))
    #print(find_nearest(arrayFixed.col7,1.92167595*pow(10,5)))
    #


