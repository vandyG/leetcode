# %% [markdown]
# # 872. Leaf-Similar Trees

# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# 
# 
# 
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# 
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# 
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
# 
#  
# 
# Example 1:
# 
# 
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
# Example 2:
# 
# 
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#  
# 
# Constraints:
# 
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].
# %%
# Solution 1
# Definition for a binary tree node.
# This solution is BFS (Breadth First Search) and doesn't 
# work with our question as it requires DFS.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        pass
    
    def leafNodes(self, tree):

        leaves = []
        root = tree[0]

        length = len(tree)

        for index in range(length//2):

            if tree[index] and tree[2*index + 1] == None \
                and tree[2*index +2] == None:

                leaves.append(tree[index])

        else:
            leaves.extend([node for node in tree[length//2:] if node is not None])
        
        return leaves
# %%
sol = Solution()
sol.leafNodes([3,5,1,6,2,9,8,None,None,7,4])
# %%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if self.leafNodes(root1,0) == self.leafNodes(root2, 0):
            return True

    def leafNodes(self, tree, index):

        if index >= len(tree) or tree[index] == None:
            return []
        if tree[index] and index >= len(tree)//2:
            return [tree[index]]
        
        leaves = []

        if tree[index] and tree[2*index + 1] == None \
                and tree[2*index +2] == None:
            leaves.append(tree[index])
        
        nodes1 = self.leafNodes(tree, 2*index +1)
        nodes2 = self.leafNodes(tree, 2*index +2)

        leaves.extend(nodes1)
        leaves.extend(nodes2)

        return leaves

# %%
sol=Solution()
sol.leafNodes([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8],0)
# %%
# Using TreeNode class

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node: return
            if not node.left and not node.right: return [node.val]
            return dfs(node.left) + dfs(node.right)
    
        return dfs(root1) == dfs(root2)
# %%
sol=Solution()
sol.leafSimilar([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8],0)

# %%
