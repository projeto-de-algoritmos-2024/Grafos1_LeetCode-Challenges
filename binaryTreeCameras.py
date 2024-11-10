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
    self.camera = 0
    self.val = [len(self.root) * 0]

    def minCameraCover(self, root):
        if not root:
            return 0
        self.minCameraCover_recursive(root)

    def minCameraCover_recursive(self, root):
        if root: 
            if self.val[root.val] != 1:
                self.val[root] = 1
                if self.val[root.val-1] is not None and self.val[(root.val-1)/2] != -1 and root.left or root.right:     
                        self.camera += 1
                        self.val[root] = -1 # marcando como camera
                        self.minCameraCover_recursive(root.left)
                        self.minCameraCover_recursive(root.right)
                else:
                    if root.letf or root.right:
                        self.minCameraCover_recursive(root.left)
                        self.minCameraCover_recursive(root.right)
                        
        return self.camera 
