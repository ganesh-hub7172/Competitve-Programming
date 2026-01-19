# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        def helper(node, low, high):
            if not node:
                return True
            # The current node must be strictly between low and high
            if not (low < node.val < high):
                return False
            # Recursively check left and right subtrees
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        return helper(root, float('-inf'), float('inf'))
