# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        head = root  # start of current level
        
        while head:
            dummy = Node(0)  # dummy node for next level
            prev = dummy
            curr = head
            
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next  # move along current level
            
            head = dummy.next  # move to the start of next level
        
        return root
