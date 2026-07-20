# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treelist(self,root):
        if not root:
            return ['#']
        return [root.val] + self.treelist(root.left) + self.treelist(root.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        plist = self.treelist(p)
        qlist = self.treelist(q)
        return plist == qlist
        