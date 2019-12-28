# coding=utf-8

'''
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
    
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
    
    示例：
    
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/add-two-numbers
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # (2 -> 4 -> 3) + (5 -> 6 -> 4)
        return_data = ListNode(0)
        next_return = return_data
        wei = 0
        while (l1 or l2):
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val = l1_val + l2_val + wei
            next_return.val = val % 10
            wei = val // 10
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
            if (l1 or l2):
                next_return.next = ListNode(0)
                next_return = next_return.next
        if wei:
            next_return.next = ListNode(wei)
        return return_data
