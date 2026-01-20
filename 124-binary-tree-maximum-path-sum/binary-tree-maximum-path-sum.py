# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            # Only take positive contributions
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Path through this node
            current_path = node.val + left_gain + right_gain
            
            # Update global max
            self.max_sum = max(self.max_sum, current_path)
            
            # Return max gain to continue upward
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum
