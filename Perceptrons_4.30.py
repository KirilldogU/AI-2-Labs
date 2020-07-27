import sys
import random
import matplotlib.pyplot as pl
import math

def perceptron(A, w, b, x):
    sumTup = b
    for index in range(len(w)):
        sumTup += ((x[-index]*w[-index]))
    return(A(sumTup))
    #return A(resultingTuple)


def truth_table(bits, n):
    numTuples = 2 ** bits
    tupleList = []
    firstTuple = (1,)*bits
    tupleList.append(firstTuple)
    for x in range((numTuples)-1):
        previousTuple = tupleList[-1]
        index = -1
        indexList = []
        newTuple = []
        for item in previousTuple:
            newTuple.append(item)
        while previousTuple[index] !=1:
            indexList.append(index)
            index -=1
        newTuple[index] = 0
        for indexPast in indexList:
            newTuple[indexPast] = 1
        newTupleT = tuple(newTuple)
        tupleList.append(newTupleT)
    binaryofNumber = list(bin(n))
    tupleSolution = ()
    while len(binaryofNumber)!=2:
        binaryResult = int(binaryofNumber.pop())
        tupleSolution = (tupleList.pop(), binaryResult) + tupleSolution
    while len(tupleList) != 0:
        tupleSolution = (tupleList.pop(), 0) + tupleSolution
    finalSolution = list()
    for x in range(len(tupleSolution)):
        if (x % 2) == 0:
            finalSolution.append((tupleSolution[x], tupleSolution[x+1]))
    return finalSolution

def pretty_print_tt(table): #table is a list of elements, where element is a tuple of a tuple a value
    print("TUPLE TABLE:")
    for element in table:
        tupleE, value = element
        print(str(tupleE) + "   VALUE  " + str(value))
    print()

def step(num):
    #print(num)
    if num > 0:
        return 1
    return 0

k = 3.7

def sigmoid(num):#returns 0-1, decimal
    #print(k)
    temp = 1 + math.e ** (-(k*4)*(num))
    temp = 1 / (temp)
    return temp

def set_k(num):#returns 0-1, decimal
    global k
    k = num

def check(n, w, b):
    bits = len(w)
    tableArr = truth_table(bits, n)
    #print("CHECKING")
    pretty_print_tt(tableArr)
    correctOutputs = 0
    wrongOutputs = 0
    for tupleInput, answerValue in tableArr:
        judgedValue = perceptron(A, w, b, tupleInput)
        error = answerValue - judgedValue
        if error == 0:
            correctOutputs +=1
        else:
            wrongOutputs+=1
    accuracy = (correctOutputs)/(correctOutputs+wrongOutputs)
    #print("ACCURACY CALCULATED: " + str(accuracy))
    return accuracy

def findNumOutputs(inputLen):
    maxNum = 2 ** (2 ** inputLen)
    #print(maxNum)
    correctNum = 0
    correctNumList = []
    for num in range(maxNum):
        w, b = train(inputLen, num)
        if check(num, w, b) == 1:
            correctNum += 1
            correctNumList.append(num)
    #print("NUM CORRECT: " + str(correctNum))

def train(inputLen, num):   #inputLen is num Bits
    w = tuple([0] * inputLen)
    b = 0
    epochList = truth_table(inputLen, num)
    for attempt in range(100 * len(epochList)):
        index = attempt % (len(epochList))
        x, correctValue = epochList[index]
        judgedValue = perceptron(A, w, b, x)
        error = correctValue - judgedValue
        b += error
        wList = list(w)
        for index in range(len(wList)):
            wList[index] = w[index] + x[index] * error
        w = tuple(wList)
    return w, b


def initXYList(): #part3
    x = -2.0
    xyList = list()
    while x <= 2.0:
        y = -2.0
        while y <= 2.0:
            xyList.append((x, y))
            y += .10
            y = round(y, 1)
        xyList.append((x,y))
        x += .10
        x = round(x, 1)
    return xyList

def generateValues(numberSolution, xyTupleList):
    blueVals = list()
    redVals = list()
    inputLen = 2
    w,b = train(inputLen, numberSolution)
    if check(numberSolution, w, b) == 1.0:  #can be modeled
        for x, y in xyTupleList:
            if perceptron(A, w, b, (x,y)) == 1:
                blueVals.append((x,y))
            else:
                redVals.append((x,y))
    return redVals, blueVals

def XOR_Network(initXYlist):
    A = step
    blueVals = list()
    redVals = list()
    wNANDperceptron, bNANDperceptron = train(2, 7)
    wORperceptron, bORperceptron = train(2, 14)
    wANDperceptron, bANDperceptron = train(2, 8)
    print("YALLA")
    print(wNANDperceptron)
    print(bNANDperceptron)
    print(wORperceptron)
    print(bORperceptron)
    print(wANDperceptron)
    print(bANDperceptron)
    for x0,y0 in initXYlist:
        x1 = perceptron(A, wNANDperceptron, bNANDperceptron, (x0, y0))
        y1 = perceptron(A, wORperceptron, bORperceptron, (x0, y0))
        if perceptron(A, wANDperceptron, bANDperceptron, (x1, y1)) == 1:
            blueVals.append((x0, y0))
        else:
            redVals.append((x0, y0))
    return redVals,blueVals

A = step

def plotNum(tupleList, color):
    for element in tupleList:
        x, y = element
        if (x == 0) and (y == 0):
            pl.scatter(x, y, s = 15, c = color, alpha = 1)
        if (x == 0) and (y == 1):
            pl.scatter(x, y, s = 15, c = color, alpha = 1)
        if (x == 1) and (y == 0):
            pl.scatter(x, y, s = 15, c = color, alpha = 1)
        if (x == 1) and (y == 1):
            pl.scatter(x, y, s = 15, c = color, alpha = 1)
        else:
            pl.scatter(x, y, s= 5, c=color, alpha=0.5)

def shouldInside(element):
    x,y = element
    if (x**2)+(y**2) >= 1:
        return True
    return False

def generateColorsPart5(totalXYList, insideVals, outsideVals):
    darkBlueL = list()
    lightBlueL = list()
    darkGreenL = list()
    lightGreenL = list()
    for element in totalXYList:
        if (element not in insideVals) and (shouldInside(element) == False):
            darkBlueL.append(element)
        if (element in insideVals) and (shouldInside(element) == False):
            lightBlueL.append(element)
        if (element in insideVals) and (shouldInside(element) == True):
            darkGreenL.append(element)
        if (shouldInside(element) == True) and (element in outsideVals):
            lightGreenL.append(element)
    plotNum(darkGreenL, "darkgreen")
    plotNum(lightBlueL, "lightblue")
    plotNum(darkBlueL, "darkblue")
    plotNum(lightGreenL, "lightgreen")


#PART 1
#table = truth_table(2, 5)
#pretty_print_tt(table)
#output = perceptron(step, (1, 1), 1, (0, 0))
#check(60800, (3,2,3,1), -5)     #part 1

#PART 2
#lenInput = 3
#findNumOutputs(lenInput)

#PART 3
initXYlist = initXYList()
#for x in range(16):         #conical number of solution
#    redVal, blueVal = generateValues(x, initXYlist)
#    print(x)
#    plotNum(redVal, "red")
#    plotNum(blueVal, "blue")
#    pl.show()

#PART 4
# redVal, blueVal = XOR_Network(initXYlist)
# plotNum(redVal, "red")
# plotNum(blueVal, "blue")
# pl.show()

#PART 5
insideVals = list()
outsideVals = list()
for x,y in initXYlist:
    perceptron1 = perceptron(A, (-1, 0), 1, (x, y))
    perceptron2 = perceptron(A, (0, -1), 1, (x, y))
    perceptron3 = perceptron(A, (1, 0), 1, (x, y))
    perceptron4 = perceptron(A, (0, 1), 1, (x, y))
    perceptronOutput = perceptron(A,(1,1,1,1), -3.5, (perceptron1, perceptron2, perceptron3, perceptron4))
    #(perceptronOutput)

    if perceptronOutput > 0.5:
        insideVals.append((x,y))
    else:
        outsideVals.append((x,y))
generateColorsPart5(initXYlist, insideVals, outsideVals)
pl.show()
#

def perceptronOutput(tupleXY, wVals):
    x,y = tupleXY
    set_k(wVals[17])
    perceptron1 = perceptron(A, (wVals[0], wVals[1]), wVals[2], (x, y))
    perceptron2 = perceptron(A, (wVals[3], wVals[4]), wVals[5], (x, y))
    perceptron3 = perceptron(A, (wVals[6], wVals[7]), wVals[8], (x, y))
    perceptron4 = perceptron(A, (wVals[9], wVals[10]), wVals[11], (x, y))
    perceptronOutput = perceptron(A, (wVals[12],wVals[13],wVals[14],wVals[15]), wVals[16], (perceptron1, perceptron2, perceptron3, perceptron4))
    if perceptronOutput > wVals[18]:        #this value works 98.93%
        return True
    else:
        return False

training_set = []
with open("10000_pairs.txt", "r") as f:
    for line in f:
        xs, ys = line.split()
        x, y = float(xs), float(ys)
        answer = True if x**2 + y**2 <= 1 else False
        training_set.append(tuple(((x, y), answer)))
training_set = tuple(training_set)

def get_tally_correct(weightsValues): #generates value of 10000 that perceptron Network passes
    tally = 0
    for x_vec, output in training_set:
        trained_out = perceptronOutput(x_vec, weightsValues) # Change this to match your code; True means inside and False means outside!
        if trained_out == output:
            tally += 1
    return tally


valsGeneral = [-1, 0, 1, 0, -1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, -3.5, 3.7, 0.4694]
print("My code got this many correct out of 10,000: %s" % get_tally_correct(valsGeneral))

def HillClimber(training_set, target_correct):
    w = list()
    for x in range(19):
        w.append(random.randint(-1,1))
    w = valsGeneral
    wSuccess = get_tally_correct(w)
    print(wSuccess)
    count = 0
    lambo = .1
    randomVal = random.random()
    #print(w)
    while count < 1000:
        newW = list()
        for index in range(len(w)):
            deltaW = w[index]*lambo
            if w[index] == 0.0:
                deltaW = lambo
            diceRoll = random.random()
            if diceRoll > .5:
                newW.append(w[index] - deltaW)
            else:
                newW.append(w[index] + deltaW)
        #print(newW)
        currentSuccess = get_tally_correct(newW)
        #print(currentSuccess)
        if currentSuccess > target_correct:
            return newW
        if currentSuccess < wSuccess:
            count += 1
        if currentSuccess >= wSuccess:
            count = 0
            w = newW
            wSuccess = currentSuccess
            print(wSuccess)


    # global valsGeneral
    # for x in range(100):        #while not stop_condition
    #     vals = valsGeneral  # weights, b, k, and
    #     madeImprovement = True
    #     lambo = .1
    #     newCorrect = 0
    #     w = random.randint(-1, 1)
    #     for index in range(200):
    #         #for index in range(len(vals)):
    #         #    vals[index] = vals[index] + (random.randint(-1, 1))*lambo
    #         valsNew = list()
    #         for index in range(len(vals)):
    #             valsNew.append(vals[index] + w*lambo)
    #         #oldCorrect = get_tally_correct(vals)
    #         #newCorrect = get_tally_correct(valsNew)
    #         #if newCorrect > target_correct:
    #         #    print("GOT IT")
    #         #    valsGeneral = valsNew
    #         vals = valsNew
    #         #if newCorrect > oldCorrect:
    #         #    print("CORRECTED")
    #         #    vals = list(valsNew)
    #         #    print(newCorrect)
    #     newCorrect = get_tally_correct(valsNew)
    #     print(newCorrect)
    #     if get_tally_correct(vals) > get_tally_correct(valsGeneral):
    #         valsGeneral = vals
    # print("FAILURE")

#HillClimber(training_set, 9950)

















