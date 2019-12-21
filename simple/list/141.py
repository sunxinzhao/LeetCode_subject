# coding=utf-8
'''
    给定一个链表，判断链表中是否有环。
    
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
    
     
    
    示例 1：
    
    输入：head = [3,2,0,-4], pos = 1
    输出：true
    解释：链表中有一个环，其尾部连接到第二个节点。
    
    
    示例 2：
    
    输入：head = [1,2], pos = 0
    输出：true
    解释：链表中有一个环，其尾部连接到第一个节点。
    
    
    示例 3：
    
    输入：head = [1], pos = -1
    输出：false
    解释：链表中没有环。
    
    
     
    
    进阶：
    
    你能用 O(1)（即，常量）内存解决此问题吗？
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/linked-list-cycle
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list_data = []
        while head:
            if head in list_data:
                return True
            else:
                list_data.append(head)
                head = head.next
        return False


# 将访问过的值置空
class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if not head.val:
                return True
            else:
                head.val = None
                head = head.next
        return False


# 快慢指针
class Solution3(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        fast = head.next
        slow = head
        while slow != fast:
            if not fast or not fast.next:
                return False

            fast = fast.next.next
            slow = slow.next
        return True
