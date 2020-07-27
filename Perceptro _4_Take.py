import numpy as np
import math
import random
import csv
import pickle
import decimal
decimal.getcontext().prec = 100

training_set = []
with open("numPairs.txt", "r") as f:
    for line in f:
        xs, ys = line.split()
        x, y = float(xs), float(ys)
        answer = 1 if x ** 2 + y ** 2 <= 1 else 0
        point = list()
        point.append(x)
        point.append(y)
        answerList = list()
        answerList.append(answer)
        training_set.append(tuple((point, answerList)))
training_set = tuple(training_set)

def create_network(architecture_list):
    #IN WEIGHTS MATRIX:
    #amount of cols =  number
    #amount of rows = previous number
    #IN BIASES MATRIX:
    #ROWS = 1, COLUMNS = number
    structure_list = list()
    inputMatrix = np.matrix(2 * np.random.rand(1, architecture_list[0]) - 1)
    for index in range(1, len(architecture_list)):
        w = np.matrix(2 * np.random.rand(architecture_list[index-1], architecture_list[index]) - 1)
        b = np.matrix(2 * np.random.rand(1, architecture_list[index]) - 1)
        structure_list.append(tuple((w,b)))
    return inputMatrix, structure_list

MNIST_structure = [2, 4, 1]#wrong -irrelelvant
#MNIST_structure = [2,2,2]
inputMat, networkWB = create_network(MNIST_structure)
# networkWB = list()
# w0 = np.matrix([[1, -3],
#                [2, -1]])
# b1 = np.matrix([-2, 5])
#
# w1 = np.matrix([[1, -1],
#                [-2, 3]])
#
# b2 = np.matrix([3, -1])
# networkWB.append(tuple((w0, b1)))
# networkWB.append(tuple((w1, b2)))
def sigmoid(x):
    return 1 / (1 + math.e ** (-x))

vec_sig = np.vectorize(sigmoid)

def sig_prime(x):
    return (math.e ** (-x)) / ((1 + math.e ** (-x)) ** 2)

vec_sigprime = np.vectorize(sig_prime)
lambo = 0.1
filename = 'weightBias'
outfile = open(filename,'wb')
pickle.dump(networkWB, outfile)
infile = open(filename, 'rb')
infile.close()
outfile.close()

x1 = np.matrix([0.8,1])
y1 = np.matrix([0, 1])

while True:
    epoch = 0
    numCorrect = 0
    totalError = 0.0
    print(networkWB)
    for inputOutput in training_set:
        inputs, out = inputOutput
        a0 = np.matrix(inputs)
        y = np.matrix(out)
        aList = list()          #a0, a1, a...
        aList.append(a0)
        dotList = list()
        dotList.append("")  #blank, dot1, dot2
        for level in range(len(networkWB)):         #forward PROP
            w, b = networkWB[level]
            prevA = aList[len(aList)-1]
            a = vec_sig(prevA*w+b)
            aList.append(a)
            dot = prevA*w+b
            dotList.append(dot)
        deltaListBacktoFront = list()
        deltaN = np.multiply(vec_sigprime(dotList[len(aList)-1]), y - aList[len(aList)-1])
        deltaListBacktoFront.append(deltaN)
        for index in range(len(aList)-2, 0, -1):
            deltaL = np.multiply(vec_sigprime(dotList[index]), deltaListBacktoFront[len(deltaListBacktoFront)-1] * networkWB[index][0].transpose())
            deltaListBacktoFront.append(deltaL)
        deltaList = deltaListBacktoFront[::-1]          #THE
        for index in range(0, len(aList)-1):
            wOld, bOld = networkWB[index]
            wIndex = wOld + lambo * aList[index].transpose() * deltaList[index]
            bIndex = bOld + lambo * deltaList[index]
            networkWB[index] = tuple((wIndex, bIndex))
        newAList = list()
        newAList.append(a0)
        for level in range(len(networkWB)):         #forward PROP
            w, b = networkWB[level]
            prevA = newAList[len(newAList)-1]
            a = vec_sig(prevA*w+b)
            newAList.append(a)
    for input, output in training_set:
        a0 = np.matrix(input)
        y = np.matrix(output)
        aList = list()          #a0, a1, a...
        aList.append(a0)
        dotList = list()
        dotList.append("")  #blank, dot1, dot2
        for level in range(len(networkWB)):         #forward PROP
            w, b = networkWB[level]
            prevA = aList[len(aList)-1]
            a = vec_sig(prevA*w+b)
            aList.append(a)
            dot = prevA*w+b
            dotList.append(dot)
        lastA = aList[len(aList)-1]
        secondERR = .5 * np.linalg.norm(y - lastA) ** 2
        totalError += secondERR
        allCorrect = lastA.round() == y.round()
        # print(allCorrect, lastA.round(), y.round())
        if allCorrect.all() == True:
            numCorrect += 1
    outfile = open(filename, 'wb')
    pickle.dump(networkWB, outfile)
    outfile.close()
    print()
    print("NUM CORRECT: " + str(numCorrect))
    print("TOTAL ERROR: " + str(totalError))