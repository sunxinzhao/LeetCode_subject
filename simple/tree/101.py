# coding=utf-8
'''
    给定一个二叉树，检查它是否是镜像对称的。

    例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    
        1
       / \
      2   2
       \   \
       3    3
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/symmetric-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 层序遍历，查看每一层节点是不是回文
        parent = [root]
        while (parent):
            child_node_list = []
            child_node_list_val = []
            # 获取到子节点并获取到子节点的值
            for node in parent:
                if node:
                    child_node_list.append(node.left)
                    child_node_list.append(node.right)
                    child_node_list_val.append(node.left.val if node.left else None)
                    child_node_list_val.append(node.right.val if node.right else None)
            # 判断节点的值是不是回文
            if child_node_list_val != child_node_list_val[::-1]:
                return False
            parent = child_node_list
        return True


class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 迭代
        def is_equese(root1, root2):
            if not root1 and not root2:
                return True
            if not root2 or not root1:
                return False
            if root1.val != root2.val:
                return False
            return is_equese(root1.left, root2.right) and is_equese(root1.right, root2.left)

        return is_equese(root, root)


class Solution3(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 树的中序遍历，本来想的是树的中序遍历是左子树，根节点，右子树，
        # 也可以通过中序遍历的结果是不是回文来判断数是不是对称，
        # 但是这种方式有问题，在判断完全二叉树可以，在判断非完全二叉树时，中间会有缺省值，造成错误
        # 例如：[1,2,2,2,null,2] ，中序遍历的结果是[2, 2, 1, 2, 2]，他是回文，但是这个树并不是对称二叉树

        data = []

        def mid_seach(node):
            if node == None:
                return False
            mid_seach(node.left)
            data.append(node.val if node.val else None)
            mid_seach(node.right)

        mid_seach(root)
        return data
