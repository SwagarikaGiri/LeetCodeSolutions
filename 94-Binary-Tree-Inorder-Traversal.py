# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res =[]
        stack =[(root,False)]
        while stack:
            node, visited = stack.pop()
            #just print
            if node:
                if visited:
                    res.append(node.val)
                #left , node, right so enter in stack in opposite order
                else:
                    stack.append((node.right,False))
                    stack.append((node,True))
                    stack.append((node.left,False))
        return res


