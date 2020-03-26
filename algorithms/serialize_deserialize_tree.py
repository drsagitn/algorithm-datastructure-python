"""

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """        
        def addToString(node):
            nonlocal s
            if s != "":
                s += ","
            if node is None:
                s += str("null")
            else:
                s += str(node.val)
                addToString(node.left)
                addToString(node.right)
        s = ""
        addToString(root)
        return s
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.        
        
        :type data: str
        :rtype: TreeNode
        """        
        def createNode():
            nonlocal arr
            if len(arr) == 0:
                return None
            val = arr.pop(0)
            if val == 'null':
                return None
            node = TreeNode(val)
            node.left = createNode()
            node.right = createNode()
            return node
        arr = data.split(",")
        return createNode()
            
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.left = TreeNode(4)
c = Codec()
c.deserialize(c.serialize(root))