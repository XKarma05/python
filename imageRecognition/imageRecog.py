from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce
from collections import Counter


def createExamples():
    numberArrayExamples = open('numArEx.txt', 'a')
    numbersWeHave = range(0,10)
    versionsWeHave = range(1,10)

    for eachNum in numbersWeHave:
        for eachVer in versionsWeHave:
            imgFilePath = 'images/numbers/' + str(eachNum) + '.' + str(eachVer) + ".png"
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            lineToWerite = str(eachNum) + '::' + eiarl + '\n'
            numberArrayExamples.write(lineToWerite)



def threshold(imageArray):
    balanceAr  = []
    newAr = imageArray
    avgNum = 0

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPix[:3]/3)
            balanceAr.append(avgNum)

    avgNum = reduce(lambda x, y: x + y, balanceAr)/len(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if(reduce(lambda x, y: x + y, eachPix[:3]/3) > avgNum):
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255

    return newAr


def whatNumIsThis(filePath):
    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')

            eachPixInQ = inQuestion.split('],')

            x = 0

            while(x < len(eachPixEx)):
                if(eachPixEx[x] == eachPixInQ[x]):

                    matchedAr.append(int(currentNum))
                x += 1

    x = Counter(matchedAr)
    print(x)


whatNumIsThis('images/test1.png')
whatNumIsThis('images/test2.png')
whatNumIsThis('images/test3.png')
whatNumIsThis('images/test4.png')
whatNumIsThis('images/test5.png')
whatNumIsThis('images/test6.png')
whatNumIsThis('images/test7.png')
whatNumIsThis('images/test8.png')
whatNumIsThis('images/test9.png')


'''
i1 = Image.open('images/numbers/0.1.png')
iar1 = np.array(i1)
i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)
i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)
i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)

createExamples()


threshold(iar1)
threshold(iar2)
threshold(iar3)
threshold(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan = 4, colspan = 3)
ax2 = plt.subplot2grid((8,6), (4,0), rowspan = 4, colspan = 3)
ax3 = plt.subplot2grid((8,6), (0,3), rowspan = 4, colspan = 3)
ax4 = plt.subplot2grid((8,6), (4,3), rowspan = 4, colspan = 3)

ax1.imshow(iar1)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()
'''
