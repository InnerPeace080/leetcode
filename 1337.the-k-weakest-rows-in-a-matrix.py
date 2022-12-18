#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        numberOfSolider = [sum(row) for row in mat]
        minRowIndex = numberOfSolider.index(min(numberOfSolider))
        print(minRowIndex)

# @lc code=end
