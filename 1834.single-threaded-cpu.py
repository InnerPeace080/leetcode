#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#

import heapq
import inspect
import json
from collections import deque
from typing import List

from timebudget import timebudget

# @lc code=start


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        queue = []
        timeCounter = 1
        busy = 0

        taskOrder = []

        sortedTaskByTime = deque(sorted([(task[1][0], task) for task in enumerate(tasks)]))

        while True:
            if (len(queue) == 0 and len(sortedTaskByTime) == 0):
                break

            if busy == 0:
                next_time = sortedTaskByTime[0][0]
            else:
                next_time = timeCounter+busy
            # push task into queue
            while len(sortedTaskByTime) > 0 and sortedTaskByTime[0][0] <= next_time:
                tasksNeedGotoQueue = sortedTaskByTime[0][1]
                sortedTaskByTime.popleft()

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
