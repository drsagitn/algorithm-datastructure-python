"""
This time tree has no left right order
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathToNode(self, root, node):
        if root is None:
            return None
        if root.val == node.val:
            return [root]
        if root.left is not None:            
            leftPath = self.pathToNode(root.left, node)
            if leftPath is not None:
                leftPath.append(root)
                return leftPath
        if root.right is not None:            
            rightPath = self.pathToNode(root.right, node)
            if rightPath is not None:
                rightPath.append(root)
                return rightPath
        
    # Time O(n): loop through all tree nodes
    # Space O(n): stack of all tree nodes
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        p_path = self.pathToNode(root, p)
        q_path = self.pathToNode(root, q)
        ret = None
        while len(q_path) > 0 and len(p_path) > 0:
            qNode = q_path.pop()
            pNode = p_path.pop()
            if qNode.val == pNode.val:
                ret = qNode
            else:
                break
        return ret

s = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
s.lowestCommonAncestor(root, root.left, root.left.right.right)