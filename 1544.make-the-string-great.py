#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:

        i = 0
        while True:
            if i < len(s)-1:
                if abs(ord(s[i+1])-ord(s[i])) == 32:
                    s = s[0:i:]+s[i+2::]
                    i -= 2
                i = max(i+1, 0)
            else:
                break

        return s

# @lc code=end
