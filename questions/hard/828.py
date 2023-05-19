# %% [markdown]

# # 828. Count Unique Characters of All Substrings of a Given String

# Let's define a function `countUniqueChars(s)` that returns the number of 
#   unique characters on `s`.

# * For example, calling `countUniqueChars(s)` if `s = "LEETCODE"` then 
# `"L"`, `"T"`, `"C"`, `"O"`, `"D"` are the unique characters since they 
# appear only once in `s`, therefore `countUniqueChars(s) = 5`.
# 
# Given a string `s`, return the sum of `countUniqueChars(t)` where `t` is a 
# substring of `s`. The test cases are generated such that the answer fits 
# in a 32-bit integer.
# 
# Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
# 
# **Example 1:**
# ```
# Input: s = "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Every substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
# ```
# **Example 2:**
# ```
# Input: s = "ABA"
# Output: 8
# Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
# ```
# 
# **Example 3:**
# ```
# Input: s = "ABA" except countUniqueChars("ABA") = 1.
# ```

# %%
class Solution:
    def uniqueLetterString(self,s: str) -> int:
        us = set()
        return self.uls(s.lower(), us)
    
    def uls(self, s: str, unique_strs) -> int:

        if s in unique_strs:
            return 0
        
        len_str = len(s)
        unique_strs.add(s)
        
        if len_str == 1:
            return 1


        str1 = s[0:len_str-1]
        str2 = s[1:len_str]


        s_count = self.countUniqueChars(s)
        curr_count = s_count + self.uls(str1, unique_strs) + self.uls(str2, unique_strs)

        return curr_count

    def countUniqueChars(slef, t:str) -> int:

        char_freq = {}

        for i in t:
            if i not in char_freq.keys():
                char_freq[i] = 1
            else:
                char_freq[i] += 1

        total = 0
        for count in char_freq.values():
            if count < 2:
                total += count
        
        return total
# %%
sol = Solution()
# %%
sol.countUniqueChars("LEETCODE")
# %%
sol.uniqueLetterString("ABA")

# %% [markdown]
# ## The above solution doesn't work. The problem is to count only unique 
# occurences of a character. If it's present twice in a substring it's contri
# is 0

# %%
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        res = 0
        aap = [(0,-1) for _ in range(26)]

        temp = 0

        for i in range(len(s)):
            pos = ord(s[i]) - ord("A")
            pre, prepos = aap[pos]

            temp += (i-prepos) - pre
            res += temp
            aap[pos] = (i-prepos, i)
        return res
# %%
class Solution:
    def uniqueLetterString(self, s: str) -> int:

        # https://www.youtube.com/watch?v=JT1NDR-M_8A
        
        # For ex: s = "Hello"
        # char_occurances = {"H": [0], "E":[1], "L": [2,3], "O":[4]}

        str = s.upper()
        
        char_occurences = {}

        for index, char in enumerate(s):
            if char not in char_occurences.keys():
                char_occurences[char] = [index]
            else:
                char_occurences[char].append(index)
        
        str_len = len(s)

        for char, indices in char_occurences.items():
            
