# coding=utf-8

'''
    删除链表中等于给定值 val 的所有节点。
    
    示例:
    
    输入: 1->2->6->3->4->5->6, val = 6
    输出: 1->2->3->4->5

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 添加哨兵借点
        sentinel = ListNode(0)
        sentinel.next = head
        previous_node = sentinel  # 1 2 6
        while head:  # 1 2 6
            if head.val == val:
                previous_node.next = head.next
            else:
                previous_node = previous_node.next
            head = head.next
        return sentinel.next if sentinel.next else []
