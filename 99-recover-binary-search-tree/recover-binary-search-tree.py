# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root):
        # Initialize variables to keep track of swapped nodes
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))  # Previous node in inorder traversal

        # Inorder traversal to find the two nodes
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            # Detect swapped nodes
            if self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev  # First violation
                self.second = node        # Second violation (could be updated if non-adjacent)
            self.prev = node
            inorder(node.right)

        inorder(root)
        # Swap the values of the two nodes
        self.first.val, self.second.val = self.second.val, self.first.val
