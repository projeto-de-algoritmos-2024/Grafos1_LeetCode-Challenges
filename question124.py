# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path_sum = float('-inf')
    
    def maxPathSum(self, root) -> int:
        if root and not root.left and not root.right:
            return root.val
        
        self.maxPathSum_recursive(root)
        return self.path_sum  
             
    def maxPathSum_recursive(self, root) -> int:
        if not root:
            return 0
        
        if root:
            left_path = max(self.maxPathSum_recursive(root.left), float('-inf'))
            right_path = max(self.maxPathSum_recursive(root.right), float('-inf'))
        
        current_path = root.val + left_path + right_path
        
        self.path_sum = max(current_path, self.path_sum)
        
        return root.val + max(left_path, right_path)