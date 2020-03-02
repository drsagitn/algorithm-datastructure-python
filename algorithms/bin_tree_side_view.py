"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \\
2     3         <---
 \     \\
  5     4       <---
"""
class TreeNode:
    def __init__(self, x):        
        self.val = x
        self.left = None
        self.right = None    

class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        # if not root:
        #     return []
        # right = self.rightSideView(root.right)
        # left = self.rightSideView(root.left)
        # return [root.val] + right + left[len(right):]
        if root is None:
            return []        
        hm = {0: root.val}
        def addVal(node, level):
            if node is None:
                return
            if node.right is not None and hm.get(level) is None:
                hm[level] = node.right.val
            elif node.left is not None and hm.get(level) is None:
                hm[level] = node.left.val
            addVal(node.right, level+1)
            addVal(node.left, level+1)                        
        addVal(root, 1)        
        return hm.values()

s = Solution()

tree = TreeNode(4)
tree.left = TreeNode(3)
tree.right = TreeNode(6)
tree.left.left = TreeNode(1)
tree.left.right = None
tree.right.left = TreeNode(5)
tree.right.right = None
tree.left.left.left = None
tree.left.left.right = TreeNode(2)

print(s.rightSideView(tree))