# coding=utf-8
'''
    给定一个二叉树，返回所有从根节点到叶子节点的路径。
    
    说明: 叶子节点是指没有子节点的节点。
    
    示例:
    
    输入:
    
       1
     /   \
    2     3
     \
      5
    
    输出: ["1->2->5", "1->3"]
    
    解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/binary-tree-paths
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def construct_paths(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += '->'
                    construct_paths(node.left, path)
                    construct_paths(node.right, path)

        paths = []
        construct_paths(root, '')
        return paths


# 迭代
class Solution1:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths
