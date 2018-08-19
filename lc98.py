# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root, -float('Inf'), float('Inf'))

    def check(self, root, lowerBound, upperBound):
        if root is None:
            return True
        if root.left is not None:
            if root.right is not None:
                return root.left.val < root.val < root.right.val and self.check(root.left, lowerBound, root.val) and self.check(root.right, root.val, upperBound)
            else:
                return root.left.val < root.val and self.check(root.left, lowerBound, root.val)
        else:
            if root.right is not None:
                return root.val < root.right.val and self.check(root.right, root.val, upperBound)
            else:
                return lowerBound < root.val < upperBound


tree = TreeNode(1)
tree.right = TreeNode(1)
a = Solution()
print(a.isValidBST(tree))