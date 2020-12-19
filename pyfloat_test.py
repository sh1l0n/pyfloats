#!/usr/bin/env python
#
# Copyright author 2020
# Created by __sh0l1n@
#
from random import seed, random, randint
import sys
from pyfloat import PyFloat
import math


def testIntSum(i, j):
    target = PyFloat(str(i + j))
    iStr = PyFloat(str(i))
    jStr = PyFloat(str(j))
    value = iStr + jStr
    assert target == value, (str(iStr)  + " + " + str(jStr) + " should be " + str(target) + " and is " + str(value))

def testIntSub(i, j):
    target = PyFloat(str(i - j))
    iStr = PyFloat(str(i))
    jStr = PyFloat(str(j))
    value = iStr - jStr
    assert target == value, (str(iStr)  + " - " + str(jStr) + " should be " + str(target) + " and is " + str(value))

def testIntMul(i, j):
    target = PyFloat(str(i * j))
    iStr = PyFloat(str(i))
    jStr = PyFloat(str(j))
    value = iStr * jStr
    assert target == value, (str(iStr)  + " * " + str(jStr) + " should be " + str(target) + " and is " + str(value))

# def testIntPow(i, j):
#     target = str(pow(i,j))
#     iStr = str(i)
#     value = pyfloat.pow(iStr, j)
#     assert target == value, ("pow("+iStr  + ", " + str(j) + ") should be " + str(target) + " and is " + str(value))

def getDecimals(a):
    aS = a.split(".")
    return 0 if len(aS)==1 else len(aS[1])

def testIntSumDecimals(a, b):
    decimalsToCheck = 6
    value = str( PyFloat(str(a)) + PyFloat(str(b)) )
    target = str( PyFloat.parseFromDouble(str(a + b)) )
    value = value[0:decimalsToCheck]
    target = target[0:decimalsToCheck]
    assert (value == target), ("Decimal -> " + str(a) + " + " + str(b) + " should be [" + target + "] and is [" +  value + "]")

def testIntSubDecimals(a, b):
    decimalsToCheck = 6
    value = str( PyFloat(str(a)) - PyFloat(str(b)) )
    target = str( PyFloat.parseFromDouble(str(a - b)) )
    valueS = value[0:decimalsToCheck]
    targetS = target[0:decimalsToCheck]
    assert (valueS == targetS), ("Decimal -> " + str(a) + " - " + str(b) + " should be [" + target + "] and is [" +  value + "], valueS : " + valueS + " targetS " + targetS)

def testIntMulDecimals(a, b):
    decimalsToCheck = 6
    value = str( PyFloat(str(a)) * PyFloat(str(b)) )
    target = str( PyFloat.parseFromDouble(str(a * b)) )
    value = value[0:decimalsToCheck]
    target = target[0:decimalsToCheck]
    assert (value == target), ("Decimal -> " + str(a) + " * " + str(b) + " should be [" + target + "] and is [" +  value + "]")

# def testIntDiv(i, j):
#     target = str(i / j)
#     iStr = str(i)
#     jStr = str(j)
#     value = div(iStr, jStr)
#     assert target == value, (iStr  + " / " + jStr + " should be " + str(target) + " and is " + str(value))

def randomInteger(min=-sys.maxsize, max=sys.maxsize):
    return randint(min, max)

if __name__ == "__main__":
    seed(1)

    for i in range(0, 100000):
        a = randomInteger()
        b = randomInteger()
        ar = random()
        br = random()
        testIntSum(a, b)
        testIntSub(a, b)
        testIntMul(a, b)
        # testIntPow(a, randomInteger(0, 10))
        testIntSumDecimals(ar, br)
        testIntSubDecimals(ar, br)
        testIntMulDecimals(ar, br)
        # testIntDiv(a, b)
        
