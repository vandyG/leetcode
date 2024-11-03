#
# @lc app=leetcode id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from typing import Optional


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        number = 0
        while curr:
            number = number*10 + curr.val
            curr = curr.next
        
        number = number * 2
        prev = None

        if number == 0:
            return ListNode(number)

        while number:
            remainder = number % 10
            number = number // 10

            node = ListNode(remainder)
            node.next = prev
            prev = node

        return prev

# @lc code=end

