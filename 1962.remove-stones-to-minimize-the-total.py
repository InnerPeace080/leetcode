#
# @lc app=leetcode id=1962 lang=python3
#
# [1962] Remove Stones to Minimize the Total
#

# @lc code=start

import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-1*i for i in piles]
        heapq.heapify(heap)

        for i in range(k):
            heapq.heapreplace(heap, heap[0] + (-heap[0] // 2))

        return sum(heap) * -1


# @lc code=end
