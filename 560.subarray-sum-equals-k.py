#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

import heapq
import inspect
import json
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        total = 0
        count = 0
        totalDict = {}

        for num in nums:
            total += num

            if totalDict.get(total-k) != None:
                count += totalDict[total - k]

            totalDict[total] = (totalDict[total] + 1) if totalDict.get(total) != None else 1

            # print(totalDict)

            if (total == k):
                count += 1

        return count
# @lc code=end
