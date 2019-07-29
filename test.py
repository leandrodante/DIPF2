import os

DIR_NAME = "/home/dante/Área de Trabalho/DIP_OCR/OCR_DATABOOK/DOCS"
files = os.listdir(DIR_NAME)
files = sorted(files)
print(files)