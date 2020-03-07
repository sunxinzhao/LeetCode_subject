# coding=utf-8
'''- 题⽬五 单链表处理 假设线性表 L = {A1, A2, A3, A4, …, An-2, An-1, An}，
采⽤带头节点的单链表保存。链接节点定义如 下： 
typedef struct node { 
    int data;
    struct node * next; 
    } NODE; 
请设计⼀个算法，编程实现，重新排列 L 中的各节点，
得到线性表 L’ = {A1, An, A2, An-1, A3, An2, … }。 
'''

class Solution1(object):
    def hasCycle(self, head):
        if not head or not head.next or not head.next.next:
            return head

        p = head.next.next
        reverse = node()
        # 反转链表
        while p:
            reverse.next = node()