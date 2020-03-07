# coding=utf-8
'''
    反转一个单链表。
    
    示例:
    
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
    进阶:
    你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/reverse-linked-list
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 申请新的链表
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list = ListNode(None)
        while head:
            # 在新的列表中从头部插入
            in_node = ListNode(head.val)
            in_node.next = new_list.next
            new_list.next = in_node
            head = head.next
        return new_list.next


# 利用双指针
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_pre = None
        while head:
            # 记录head的下一个值
            new_tmp = head.next

            head.next = new_pre

            new_pre = head

            head = new_tmp
        return new_pre


# 递归
class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        cur = Solution2().reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur
