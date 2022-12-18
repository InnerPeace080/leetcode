#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        numberOfSolider = [sum(row) for row in mat]
        print(numberOfSolider)
        result = []

        for i in range(k):
            minRowIndex = numberOfSolider.index(min(numberOfSolider))
            result.append(minRowIndex)
            # numberOfSolider = numberOfSolider[:minRowIndex] + numberOfSolider[minRowIndex + 1:]
            numberOfSolider[minRowIndex] = sys.maxsize
            # print(minRowIndex, numberOfSolider)

        return result

# @lc code=end
