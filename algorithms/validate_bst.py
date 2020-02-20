class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

cclass Solution:
    def isValidBST(self, root: TreeNode, floor = float('-inf'), ceil = float('inf')) -> bool:        
        if root is None:
            return True
        if root.val <= floor or root.val >= ceil:
            return False        
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceil)

