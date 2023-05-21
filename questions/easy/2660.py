# %% [markdown]
# You are given two 0-indexed integer arrays player1 and player2, that represent the number of pins that player 1 and player 2 hit in a bowling game, respectively.

# The bowling game consists of n turns, and the number of pins in each turn is exactly 10.

# Assume a player hit xi pins in the ith turn. The value of the ith turn for the player is:

# 2xi if the player hit 10 pins in any of the previous two turns.
# Otherwise, It is xi.
# The score of the player is the sum of the values of their n turns.

# Return

# 1 if the score of player 1 is more than the score of player 2,
# 2 if the score of player 2 is more than the score of player 1, and
# 0 in case of a draw.
# 
# Example 1:
# ```
# Input: player1 = [4,10,7,9], player2 = [6,5,2,3]
# Output: 1
# Explanation: The score of player1 is 4 + 10 + 2*7 + 2*9 = 46.
# The score of player2 is 6 + 5 + 2 + 3 = 16.
# Score of player1 is more than the score of player2, so, player1 is the winner, and the answer is 1.
# ```
# Example 2:
# ```
# Input: player1 = [3,5,7,6], player2 = [8,10,10,2]
# Output: 2
# Explanation: The score of player1 is 3 + 5 + 7 + 6 = 21.
# The score of player2 is 8 + 10 + 2*10 + 2*2 = 42.
# Score of player2 is more than the score of player1, so, player2 is the winner, and the answer is 2.
# ```
# Example 3:
# ```
# Input: player1 = [2,3], player2 = [4,1]
# Output: 0
# Explanation: The score of player1 is 2 + 3 = 5
# The score of player2 is 4 + 1 = 5
# The score of player1 equals to the score of player2, so, there is a draw, and the answer is 0.
# ```
# %%
from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        score1 = 0
        score2 = 0

        flag1 = 0
        flag2 = 0

        N = len(player2)

        for i in range(N):
            
            score2 += 2*player2[i] if flag2 > 0 else player2[i]
            score1 += 2*player1[i] if flag1 > 0 else player1[i]

            flag1 -= 1
            flag2 -= 1
            
            if player1[i] == 10:
                flag1 = 2
            if player2[i] == 10:
                flag2 = 2
            
        
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0
# %%
sol = Solution()
sol.isWinner([10,2,2,3], [3,8,4,5])

# %%
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        isTen1 = isTen2 = wasTen1 = wasTen2 = False
        diff = 0

        for n1, n2 in zip(player1, player2):

            diff+= (1+(wasTen1|isTen1))*n1 - (1+(wasTen2|isTen2))*n2
 
            isTen1,isTen2, wasTen1, wasTen2 = n1 == 10, n2 == 10,isTen1,isTen2 

        return  (diff < 0) + (diff != 0)