# %% [markdown]
# # 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# 
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# 
# Return the head of the merged linked list.
# 
#  
# 
# Example 1:
# 
# 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# 
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
# 
# Input: list1 = [], list2 = [0]
# Output: [0]
#  
# 
# Constraints:
# 
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# %%
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#     
#     def __str__(self) -> str:
#         
#         curr = self
#         str = ""
#         while curr != None:
#             str += f"{curr.val}" + "->"
#             curr = curr.next
#         
#         return str
# 

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def asList(node):
            new = []
            
            while node != None:
                new.append(node.val)
                node = node.next
                    
            return new
        
        new = asList(list1) + asList(list2)
        new.sort()
        return self.toLL(new)
    


# %%
list1 = [1,2,4]
list2 = [1,3,4]

sol = Solution()
ll1 = toLL(list1)
ll2 = toLL(list2)
res = sol.mergeTwoLists(ll1,ll2)

# %% [markdown]
# The above solution doesn't work as it is general
# and qusetion says we have sorted linked lists
# %%
# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = dummy = ListNode()

        while list2 and list1:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        
        if list1 or list2:
            curr.next = list1 if list1 else list2

        return dummy.next