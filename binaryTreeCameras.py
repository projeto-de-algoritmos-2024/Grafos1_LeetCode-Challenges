# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#  0: não foi visitado
#  1: quem é camera
#  2: já foi visitado

class Solution:
    def minCameraCover(self, root):
        self.camera = 0

        def dfs(node):
            if not node:
                return 2

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                self.camera += 1
                return 1

            if left == 1 or right == 1:
                return 2
            return 0
        if dfs(root) == 0:
            self.camera += 1
        return self.camera
