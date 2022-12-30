import heapq
import inspect
import json
from collections import deque
from typing import List

from timebudget import timebudget

##

ID = ""
Class = {}
methodName = ""

e = open(ID, 'r')
lines = e.readlines()
numberOfInput = len(inspect.signature(Class[methodName]).parameters)-1
testCaseInputs = []
for testCaseIndex in range(len(lines)//numberOfInput):
    testCaseInputs.append([json.loads(lines[testCaseIndex*numberOfInput + i]) for i in range(numberOfInput)])
e.close()

# print('testCaseInputs', testCaseInputs)

o = Class()
for testCaseInput in testCaseInputs:
    print(o[methodName](*testCaseInput))
    # timebudget.report(methodName)
