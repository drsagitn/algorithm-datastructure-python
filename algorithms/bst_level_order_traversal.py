# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    hashmap = {}
    def addToArr(self, level, node: TreeNode):
        if node is None:
            return
        if self.hashmap.get(level) is None:
            self.hashmap[level] = [node.val]
        else:
            self.hashmap[level].append(node.val)
        self.addToArr(level + 1, node.left)
        self.addToArr(level + 1, node.right)
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:    
        self.hashmap = {}
        self.addToArr(0, root)
        return list(self.hashmap.values())
    