from PIL import Image
from random import randint
from xlwt import *
from xlrd import *

def convertPic2Excel(inFileName=0, outFileName=0, parseRGB=False):

    im = Image.open('Picture1.jpg', 'r')
    pix_val = list(im.getdata())


    print(im.size)
    parsed = parseRGBOut(pix_val)

    wb = Workbook()
    
    sheet1 = wb.add_sheet('Sheet 1')
    sheet2 = wb.add_sheet('Sheet 2')
    
    for j in range(0, im.size[1]):
        for i in range(0, im.size[0]):
            dataPoint = str(pix_val[i])
            sheet1.write(i, j, dataPoint)

    wb.save("pictureData{}.xlsx".format(randint(1,1000))) 
    print("done")


def openDataFile(inputFile="data.xlsx", sheetInd=0, dataCol=2, rowStart=9, rowEnd=108):
    book = xlrd.open_workbook(inputFile)
    outputList = []
    for i in range(rowStart, rowEnd):
        sheet = book.sheet_by_index(sheetInd)
        readCell = sheet.cell(i,dataCol)
        outputList.append(readCell.value)

    return (outputList)

def parseRGBOut(inputMatrix):
    print(inputMatrix[0][2])
    newMatrix = []
    for i in range(0, len(inputMatrix)-1):
        for j in range(0, 2):
            newMatrix.append(inputMatrix[i][j])
    return newMatrix
    print(newMatrix[0])

convertPic2Excel()
