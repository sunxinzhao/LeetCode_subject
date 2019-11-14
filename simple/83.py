# coding=utf-8

'''
    问题：给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
    
    示例 1:
        输入: 1->1->2
        输出: 1->2
        
    示例 2:
        输入: 1->1->2->3->3
        输出: 1->2->3
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        index = head
        next_data = head.next
        while next_data:
            if next_data.next == None:
                index.next = next_data.next
            if index.val != next_data.val:
                index.next = next_data
                index = next_data
            next_data = next_data.next
        return head
