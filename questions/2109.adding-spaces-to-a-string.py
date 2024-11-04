#
# @lc app=leetcode id=2109 lang=python3
#
# [2109] Adding Spaces to a String
#

# @lc code=start


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index = 0
        result = []

        for space in spaces:
            result.append(s[index:space])
            result.append(" ")
            index = space
        else:
            result.append(s[index:])

        return "".join(result)


# @lc code=end
