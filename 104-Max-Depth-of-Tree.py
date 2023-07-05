# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        head = root
       
        if(head):
            depth_left = 1 + self.maxDepth(head.left)
            depth_right = 1 + self.maxDepth(head.right)
            if(depth_left > depth_right):
                return depth_left
            else:
                return depth_right
        else:
            return 0
        