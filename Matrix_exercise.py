#   BACK PROP LAB

import numpy as np
import math
import random

#       PART 1
# def A(x):
#     return 1/(1+ math.e**(-x))
#
# vec_f = np.vectorize(A)
#
# w0 = np.matrix([[-1, -0.5],
#                [1, 0.5]])
# b1 = np.matrix([1, -1])
#
# w1 = np.matrix([[1, 2],
#                [-1, -2]])
#
# b2 = np.matrix([-0.5, 0.5])
# x = np.matrix([2,3])
# y = np.matrix([0.8, 1])
# a0 = x
# a1 = vec_f(a0*w0 + b1)
# print(a1)
# a2 = vec_f(a1*w1 + b2)
# print(a2)
# firstERR = .5 * (np.linalg.norm(y - a2)**2)
# def A_prime(x):
#     return (math.e**(-x))/((1+math.e**(-x))**2)
#
# vef_f_aprime = np.vectorize(A_prime)
#
# trianglar2 = np.multiply(vef_f_aprime(a1*w1 + b2), y - a2)
# trianglar1 = np.multiply(vef_f_aprime(a0*w0+b1), trianglar2*w1.transpose())
# lambo = 0.1
# w0 = w0 + lambo*a0.transpose()*trianglar1
# b1 = b1 + lambo*trianglar1
# w1 = w1 + lambo*a1.transpose()*trianglar2
# b2 = b2 + lambo*trianglar2
# a1 = vec_f(a0*w0+b1)
# a2 = vec_f(a1*w1+b2)
# secondERR = .5 * np.linalg.norm(y - a2)**2
# print("FIRST ERROR " + str(firstERR))
# print("SECOND ERROR " + str(secondERR))


#                   PART 2
# def step(x):
#     if x > 0:
#         return 1
#     return 0
#
#
# inputVals = [0,0]
# #ouput should be 0, 1, 1, 0
#
# vec_step = np.vectorize(step)
# x = np.matrix(inputVals)
# w0 = np.matrix([[-1,1],[-2,1]])
# b1 = np.matrix([3,0])
# w1 = np.matrix([[1],[2]])
# b2 = np.matrix([-2])
# a1 = vec_step((x*w0)+b1)
# a2 = vec_step((a1*w1)+b2)
# print(step(a2))

# part 3
# def sigmoid(x):
#     return 1/(1+ math.e**(-x))
# vec_sig = np.vectorize(sigmoid)
#
# def sig_prime(x):
#     return (math.e**(-x))/((1+math.e**(-x))**2)
# vec_sigprime = np.vectorize(sig_prime)
#
# inputs = [[1,1],[1,0],[0,1],[0,0]]
# outputs = [[1,0],[0,1],[0,1],[0,0]]
# weights_biases = list()
# for temp in range(12):
#     weights_biases.append(random.random())
# error = 1000
# w0Major = np.matrix([[weights_biases[0], weights_biases[1]], [weights_biases[2], weights_biases[3]]])
# b1Major = np.matrix([weights_biases[4], weights_biases[5]])
# w1Major = np.matrix([[weights_biases[6], weights_biases[7]], [weights_biases[8], weights_biases[9]]])
# b2Major = np.matrix([weights_biases[10], weights_biases[11]])
#
# while True:
#     totalError = 0.0
#     for index in range(4):
#         w0 = w0Major
#         b1 = b1Major
#         w1 = w1Major
#         b2 = b2Major
#         x = np.matrix(inputs[index])
#         y = np.matrix(outputs[index])
#         a0 = x
#         a1 = vec_sig(a0 * w0 + b1)
#         a2 = vec_sig(a1 * w1 + b2)
#         firstERR = .5 * (np.linalg.norm(y - a2) ** 2)  #
#         trianglar2 = np.multiply(vec_sigprime(a1 * w1 + b2), y - a2)
#         trianglar1 = np.multiply(vec_sigprime(a0 * w0 + b1), trianglar2 * w1.transpose())
#         lambo = 0.1
#         w0 = w0 + lambo*a0.transpose()*trianglar1
#         b1 = b1 + lambo*trianglar1
#         w1 = w1 + lambo*a1.transpose()*trianglar2
#         b2 = b2 + lambo*trianglar2
#         w0Major = w0
#         b1Major = b1
#         w1Major = w1
#         b2Major = b2
#         a1 = vec_sig(a0*w0+b1)
#         a2 = vec_sig(a1*w1+b2)
#         secondERR = .5 * np.linalg.norm(y - a2)**2
#         totalError+=secondERR
#     print(totalError)
#     if totalError < 0.1:
#         break
#
# for index in range(4):
#     w0 = np.round(w0Major)
#     b1 = np.round(b1Major)
#     w1 = np.round(w1Major)
#     b2 = np.round(b2Major)
#     x = np.matrix(inputs[index])
#     y = np.matrix(outputs[index])
#     print("INPUT")
#     print(x)
#     a0 = x
#     a1 = vec_sig(a0 * w0 + b1)
#     a2 = vec_sig(a1 * w1 + b2)
#     print("OUTPUT")
#     print(np.round(a2))

# PART 4
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


def sigmoid(x):
    return 1 / (1 + math.e ** (-x))


vec_sig = np.vectorize(sigmoid)


def sig_prime(x):
    return (math.e ** (-x)) / ((1 + math.e ** (-x)) ** 2)


vec_sigprime = np.vectorize(sig_prime)
weights_biases = list()
for temp in range(12):
    weights_biases.append(random.random())
error = 1000
w0Major = np.matrix([[random.random(),  random.random(), random.random(),  random.random(), random.random(),  random.random(), random.random(),  random.random()], [
    random.random(),  random.random(),   random.random(),  random.random(), random.random(),  random.random(),   random.random(),  random.random()]])
b1Major = np.matrix([random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()])
w1Major = np.matrix([[random.random()], [random.random()], [random.random()], [random.random()], [random.random()], [random.random()], [random.random()], [random.random()]])
b2Major = np.matrix([random.random()])
lambo = 0.5

while True:
    numCorrect = 0
    totalError = 0.0
    for val in training_set:
        w0 = w0Major
        b1 = b1Major
        w1 = w1Major
        b2 = b2Major
        x = np.matrix(val[0])
        y = np.matrix(val[1])
        a0 = x
        a1 = vec_sig(a0 * w0 + b1)
        a2 = vec_sig(a1 * w1 + b2)
        print(a2)
        a2round = np.round(a2)
        print(a2round)
        if int(a2round) == int(y):
            numCorrect += 1
        firstERR = .5 * (np.linalg.norm(y - a2) ** 2)
        trianglar2 = np.multiply(vec_sigprime(a1 * w1 + b2), y - a2)
        trianglar1 = np.multiply(vec_sigprime(a0 * w0 + b1), trianglar2 * w1.transpose())
        w0 = w0 + lambo * a0.transpose() * trianglar1
        b1 = b1 + lambo * trianglar1
        w1 = w1 + lambo * a1.transpose() * trianglar2
        b2 = b2 + lambo * trianglar2
        w0Major = w0
        b1Major = b1
        w1Major = w1
        b2Major = b2
        a1 = vec_sig(a0 * w0 + b1)
        a2 = vec_sig(a1 * w1 + b2)
        secondERR = .5 * np.linalg.norm(y - a2) ** 2
        totalError += secondERR
    if 9300 < numCorrect < 9900:
        lambo = lambo * 0.99
    if 9900 <= numCorrect:
        lambo = lambo * .999
    print("CORRECT: " + str(numCorrect))
    print("TOTAL ERROR: " + str(totalError))
    print("LAMBDA: " + str(lambo))
    if numCorrect > 9950:
        break