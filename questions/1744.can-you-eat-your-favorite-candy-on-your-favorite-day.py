#
# @lc app=leetcode id=1744 lang=python3
#
# [1744] Can You Eat Your Favorite Candy on Your Favorite Day?
#

# @lc code=start
from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        result = []
        for query in queries:
            type = query[0]
            days = query[1]
            daily_cap = query[2]
            total_other = 0
            max_candies = (days + 1) * daily_cap
            for j in range(0, type):
                total_other += candiesCount[j]

            previousFinished = max_candies > total_other
            minFinished = total_other + candiesCount[type] > days

            if previousFinished and minFinished:
                result.append(True)
            else:
                result.append(False)

        return result


# @lc code=end

sol = Solution()
res = sol.canEat(
    [
        46,
        5,
        47,
        48,
        43,
        34,
        15,
        26,
        11,
        25,
        41,
        47,
        15,
        25,
        16,
        50,
        32,
        42,
        32,
        21,
        36,
        34,
        50,
        45,
        46,
        15,
        46,
        38,
        50,
        12,
        3,
        26,
        26,
        16,
        23,
        1,
        4,
        48,
        47,
        32,
        47,
        16,
        33,
        23,
        38,
        2,
        19,
        50,
        6,
        19,
        29,
        3,
        27,
        12,
        6,
        22,
        33,
        28,
        7,
        10,
        12,
        8,
        13,
        24,
        21,
        38,
        43,
        26,
        35,
        18,
        34,
        3,
        14,
        48,
        50,
        34,
        38,
        4,
        50,
        26,
        5,
        35,
        11,
        2,
        35,
        9,
        11,
        31,
        36,
        20,
        21,
        37,
        18,
        34,
        34,
        10,
        21,
        8,
        5,
    ],
    [[85, 54, 42]],
)

print(res)
