# coding=utf-8
'''
    给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
    
    例如：
    给定二叉树 [3,9,20,null,null,15,7],
    
        3
       / \
      9  20
        /  \
       15   7
    返回其自底向上的层次遍历为：
    
    [
      [15,7],
      [9,20],
      [3]
    ]
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        parent_list = [root]
        data_list = []
        while(parent_list):
            child_list = []
            list_val = []
            for node in parent_list:
                if node:
                    child_list.append(node.left)
                    child_list.append(node.right)
                    list_val.append(node.val)
            if child_list:
                data_list.insert(0, list_val)
            parent_list = child_list
        return data_list


class Solution2(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        parent_list = [root]
        data_list = []
        while (parent_list):
            child_list = []
            list_val = []
            for node in parent_list:
                if node:
                    child_list.append(node.left)
                    child_list.append(node.right)
                    list_val.append(node.val)
            if child_list:
                data_list.append(list_val)
            parent_list = child_list
        return data_list[::-1]


class Solution3(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = [root]
        res = []

        while len(stack) > 0:
            tmp = []
            res_each = []
            for i in stack:
                if i:
                    res_each.append(i.val)
                    tmp.append(i.left)
                    tmp.append(i.right)
            stack = tmp
            if tmp:
                # res.append(res_each)
                res.insert(0, res_each)
        return res
