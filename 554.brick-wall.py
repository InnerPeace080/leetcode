#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

import heapq
import inspect
import json
from collections import deque
from typing import List

from timebudget import timebudget


# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        totalWidthDict = {}
        maxTotalWidth = 0
        for row in wall:
            totalWidth = 0
            for brick in row[0:-1:]:
                totalWidth += brick
                if totalWidth not in totalWidthDict:
                    totalWidthDict[totalWidth] = 0
                totalWidthDict[totalWidth] += 1

                maxTotalWidth = max(totalWidthDict[totalWidth], maxTotalWidth)

        return len(wall) - maxTotalWidth
# @lc code=end
