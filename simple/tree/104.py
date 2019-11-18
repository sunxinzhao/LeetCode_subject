# coding=utf-8
'''
    给定一个二叉树，找出其最大深度。
    
    二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
    
    说明: 叶子节点是指没有子节点的节点。
    
    示例：
    给定二叉树 [3,9,20,null,null,15,7]，
    
        3
       / \
      9  20
        /  \
       15   7
    返回它的最大深度 3 。
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 递归找出最大值
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 二叉树的层序遍历
        depth = 0
        parent = [root]
        while (parent):
            child_node_list = []
            # 获取到子节点
            for node in parent:
                if node:
                    child_node_list.append(node.left)
                    child_node_list.append(node.right)
            parent = child_node_list
            # 如果有子节点，则深度加1
            if parent:
                depth += 1
        return depth
