# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        result = []
        path = []

        def dfs(node, curr_sum):
            if not node:
                return
            
            # Choose
            path.append(node.val)
            curr_sum += node.val
            
            # If leaf and sum matches, record path
            if not node.left and not node.right and curr_sum == targetSum:
                result.append(list(path))
            
            # Explore
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            # Un-choose (backtrack)
            path.pop()
        
        dfs(root, 0)
        return result
