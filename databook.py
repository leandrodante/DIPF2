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

DIR_NAME = "/home/dante/Área de Trabalho/DIP_OCR/OCR_DATABOOK/DOCS_1"
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
    parser.add_argument("-q","--qt",
                        dest="quantidade",
                        default=158,
                        type=int,
                        help="Threshold when to show white",
                        required=True)
    return parser

def find_nearest(array, value):
    array = numpy.asarray(array)
    idx = (numpy.abs(array - value)).argmin()
    return idx

#args = get_parser().parse_args()

#IMAGE_NAME = args.name
#IMAGE_FORMAT = args.format
#IMAGE_REPLAY = args.quantidade

pxs = []

tipo = []
col1 = []
col1_tmp = []
col2 = []
col2_tmp = []
col3 = []
col3_tmp = []
col4 = []
col4_tmp = []
col5 = []
col5_tmp = []
col6 = []
col6_tmp = []
col7 = []
col7_tmp = []


arrayFixed = class_util.Array()
IMAGE_NAME_O = ""
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
    print(IMAGE_NAME[:-2])
    print(pxs)

    x = [100,120,150,170,200,220,250]


    function = numpy.polyfit(x, pxs, 6)
    print(function)

    if (IMAGE_NAME_O != "" and IMAGE_NAME_O != IMAGE_NAME[:-2]) or len(files) == IDX_FILE:
        #nova
        tipo.append(IMAGE_NAME_O)
        col1.append(numpy.mean(col1_tmp))
        col2.append(numpy.mean(col2_tmp))
        col3.append(numpy.mean(col3_tmp))
        col4.append(numpy.mean(col4_tmp))
        col5.append(numpy.mean(col5_tmp))
        col6.append(numpy.mean(col6_tmp))
        col7.append(numpy.mean(col7_tmp))

        col1_tmp = []
        col2_tmp = []
        col3_tmp = []
        col4_tmp = []
        col5_tmp = []
        col6_tmp = []
        col7_tmp = []
        
    i = 1
    for coe in function:
        #print(format(coe,'.40f'))
        if i == 1:
            col1_tmp.append(coe)
        elif i == 2:
            col2_tmp.append(coe)
        elif i == 3:
            col3_tmp.append(coe)
        elif i == 4:
            col4_tmp.append(coe)
        elif i == 5:
            col5_tmp.append(coe)
        elif i == 6:
            col6_tmp.append(coe)
        elif i == 7:
            col7_tmp.append(coe)

        i = i + 1

    IMAGE_NAME_O = IMAGE_NAME[:-2]
    IDX_FILE = IDX_FILE + 1
    plt.close("all")



print("RESULT")

print("tipo = [", end =" ") 
for i in tipo:
    print("'"+ i + "',", end=" ")
print("]")

print("col1 = [", end =" ") 
for i in col1:
    print( format(i ,'.40f') + ",", end=" ")
print("]")

print("col2 = [", end =" ") 
for i in col2:
    print( format(i ,'.40f') + ",", end=" ")
print("]")

print("col3 = [", end =" ") 
for i in col3:
    print( format(i ,'.40f') + ",", end=" ")
print("]")

print("col4 = [", end =" ") 
for i in col4:
    print( format(i ,'.40f') + ",", end=" ")
print("]")

print("col5 = [", end =" ") 
for i in col5:
    print( format(i ,'.40f') + ",", end=" ")
print("]")

print("col6 = [", end =" ") 
for i in col6:
    print( format(i ,'.40f') + ",", end=" ")
print("]")

print("col7 = [", end =" ") 
for i in col7:
    print( format(i ,'.40f') + ",", end=" ")
print("]")

#
#print(find_nearest(arrayFixed.col1,9.04508547*pow(10,-9)))
#print(find_nearest(arrayFixed.col2,-9.65131777*pow(10,-6)))
#print(find_nearest(arrayFixed.col3,4.18875482*pow(10,-3)))
#print(find_nearest(arrayFixed.col4,-9.45177644*pow(10,-1)))
#print(find_nearest(arrayFixed.col5,1.16716447*pow(10,2)))
#print(find_nearest(arrayFixed.col6,-7.45453313*pow(10,3)))
#print(find_nearest(arrayFixed.col7,1.92167595*pow(10,5)))
#


