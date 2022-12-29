#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#

import heapq
import inspect
import json
from typing import List

from timebudget import timebudget

# @lc code=start


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        queue = []
        timeCounter = 1
        busy = 0
        taskByTimeDict = {}

        for task in enumerate(tasks):
            if task[1][0] not in taskByTimeDict.keys():
                taskByTimeDict[task[1][0]] = []

            taskByTimeDict[task[1][0]].append(task)

        taskOrder = []
        sortedTime = sorted(taskByTimeDict.keys())

        while True:
            if (len(queue) == 0 and len(sortedTime) == 0):
                break

            if busy == 0:
                next_time = sortedTime[0]
            else:
                next_time = timeCounter+busy
            # push task into queue
            while len(sortedTime) > 0 and sortedTime[0] <= next_time:
                tasksNeedGotoQueueArr = taskByTimeDict[sortedTime[0]]
                sortedTime.pop(0)

                for tasksNeedGotoQueue in tasksNeedGotoQueueArr:
                    heapq.heappush(queue, (tasksNeedGotoQueue[1][1], tasksNeedGotoQueue[0], tasksNeedGotoQueue))

            timeCounter = next_time
            busy = 0

            # pick task to process
            if (len(queue) == 0):
                continue

            (_, _, task) = heapq.heappop(queue)

            busy = task[1][1]

            taskOrder.append(task[0])

        return taskOrder
# @lc code=end


e = open("1834", 'r')
lines = e.readlines()
numberOfInput = len(inspect.signature(Solution.getOrder).parameters)-1
testCaseInputs = []
for testCaseIndex in range(len(lines)//numberOfInput):
    testCaseInputs.append([json.loads(lines[testCaseIndex*numberOfInput + i]) for i in range(numberOfInput)])
e.close()

# print('testCaseInputs', testCaseInputs)

s = Solution()
for testCaseInput in testCaseInputs:
    print(s.getOrder(*testCaseInput))
    # timebudget.report('getOrder')
