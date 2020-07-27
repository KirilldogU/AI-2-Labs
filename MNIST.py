import numpy as np
import math
import random
import csv
import pickle
import decimal

decimal.getcontext().prec = 100

locTest = "mnist_test.csv"
locTrain = "mnist_train.csv"
inputOutputList = list()

with open(locTrain) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        output = int(row[0])
        outputList = [0.0]*10
        outputList[output] = 1.0
        inputList = list()
        for col in range(1, len(row)):
            inputList.append(float(row[col]) / 256.0)
        inputOutputList.append(tuple((inputList, outputList)))


def create_network(architecture_list):
    # IN WEIGHTS MATRIX:
    # amount of cols =  number
    # amount of rows = previous number
    # IN BIASES MATRIX:
    # ROWS = 1, COLUMNS = number
    structure_list = list()
    inputMatrix = np.matrix(2 * np.random.rand(1, architecture_list[0]) - 1)
    for index in range(1, len(architecture_list)):
        w = np.matrix(2 * np.random.rand(architecture_list[index - 1], architecture_list[index]) - 1)
        b = np.matrix(2 * np.random.rand(1, architecture_list[index]) - 1)
        structure_list.append(tuple((w, b)))
    return inputMatrix, structure_list


MNIST_structure = [784, 500, 400, 300, 100, 10]
inputMat, networkWB = create_network(MNIST_structure)


def sigmoid(x):
    return 1 / (1 + math.e ** (-x))


vec_sig = np.vectorize(sigmoid)


def sig_prime(x):
    return (math.e ** (-x)) / ((1 + math.e ** (-x)) ** 2)


vec_sigprime = np.vectorize(sig_prime)
lambo = 0.1

filename = 'weightBias'
outfile = open(filename, 'wb')
pickle.dump(networkWB, outfile)
infile = open(filename, 'rb')
infile.close()
outfile.close()

epoch = 0
while True:
    epoch = 0
    numCorrect = 0
    totalError = 0.0
    print("Training")
    for inputs, out in inputOutputList:
        a0 = np.matrix(inputs)
        y = np.matrix(out)
        aList = list()  # a0, a1, a...
        aList.append(a0)
        dotList = list()
        dotList.append("")  # blank, dot1, dot2
        for level in range(len(networkWB)):  # forward PROP
            w, b = networkWB[level]
            prevA = aList[len(aList) - 1]
            a = vec_sig(prevA * w + b)
            aList.append(a)
            dot = prevA * w + b
            dotList.append(dot)
        deltaListBacktoFront = list()
        alast = aList[len(aList) - 1]
        deltaN = np.multiply(vec_sigprime(dotList[len(aList) - 1]), y - alast)
        deltaListBacktoFront.append(deltaN)
        for index in range(len(aList) - 2, 0, -1):
            deltaL = np.multiply(vec_sigprime(dotList[index]),
                                 deltaListBacktoFront[len(deltaListBacktoFront) - 1] * networkWB[index][0].transpose())
            deltaListBacktoFront.append(deltaL)
        deltaList = deltaListBacktoFront[::-1]  # THE
        for index in range(0, len(aList) - 1):
            wOld, bOld = networkWB[index]
            wIndex = wOld + lambo * aList[index].transpose() * deltaList[index]
            bIndex = bOld + lambo * deltaList[index]
            networkWB[index] = tuple((wIndex, bIndex))
    for input, output in inputOutputList:
        a0 = np.matrix(input)
        y = np.matrix(output)
        aList = list()  # a0, a1, a...
        aList.append(a0)
        dotList = list()
        dotList.append("")  # blank, dot1, dot2
        for level in range(len(networkWB)):  # forward PROP
            w, b = networkWB[level]
            prevA = aList[len(aList) - 1]
            a = vec_sig(prevA * w + b)
            aList.append(a)
            dot = prevA * w + b
            dotList.append(dot)
        lastA = aList[len(aList) - 1]
        if (y == np.round(lastA)).all():
            numCorrect += 1
        secondERR = .5 * np.linalg.norm(y - lastA) ** 2
        totalError += secondERR
    outfile = open(filename, 'wb')
    pickle.dump(networkWB, outfile)
    outfile.close()
    print()
    print("NUM CORRECT: " + str(numCorrect))
    print("TOTAL ERROR: " + str(totalError))