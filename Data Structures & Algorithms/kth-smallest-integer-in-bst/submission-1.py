# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treelist(self,root):
        if not root:
            return []
        return self.treelist(root.left) + [root.val] + self.treelist(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        tree = self.treelist(root)
        #tree = sorted(tree)
        return tree[k-1]
        
        