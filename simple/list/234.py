# coding=utf-8
'''
    请判断一个链表是否为回文链表。
    
    示例 1:
    
    输入: 1->2
    输出: false
    示例 2:
    
    输入: 1->2->2->1
    输出: true
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 将链表反转，然后遍历比较值是不是相同
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        new_list = ListNode(None)
        new_head = head
        while head:
            # 在新的列表中从头部插入
            in_node = ListNode(head.val)
            in_node.next = new_list.next
            new_list.next = in_node
            head = head.next
        new_list = new_list.next
        while new_head:
            if new_head.val == new_list.val:
                new_head = new_head.next
                new_list = new_list.next
            else:
                return False
        return True


# 遍历链表，将值存入到数组中，然后利用双指针遍历数组
class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        list_data = []
        while head:
            list_data.append(head.val)
            head = head.next
        small_p = 0
        big_p = len(list_data)
        while small_p < big_p:
            if list_data[small_p] == list_data[big_p]:
                small_p += 1
                big_p -= 1
            else:
                return False
        return True
