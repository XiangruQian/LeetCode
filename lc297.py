# Definition for a binary tree node.
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
        if root == None:
            return '[]'
        height = self.get_height(root)
        queue = [root]
        tree = []
        while queue:
            v = queue.pop(0)
            if len(tree) + 1 < 2 ** (height - 1):
                if v is None:
                    tree.append('null')
                    queue.append(None)
                    queue.append(None)
                else:
                    tree.append(v.val)
                    if v.left is not None:
                        queue.append(v.left)
                    else:
                        queue.append(None)

                    if v.right is not None:
                        queue.append(v.right)
                    else:
                        queue.append(None)
            else:
                if v is not None:
                    tree.append(v.val)
                else:
                    tree.append('null')
        return tree.__str__().replace('\'', '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        tree = data.strip('[]').replace(' ', '').split(',')
        root = TreeNode(int(tree[0]))
        queue = [root]
        tree = [None] + tree
        for i in range(1, int(len(tree) / 2)):
            v = queue.pop(0)
            if v is not None:
                if tree[2 * i] != 'null':
                    v.left = TreeNode(int(tree[2 * i]))
                if tree[2 * i + 1] != 'null':
                    v.right = TreeNode(int(tree[2 * i + 1]))
                queue.append(v.left)
                queue.append(v.right)
        return root

    def get_height(self, vertex):
        if vertex is None:
            return 0
        else:
            return max(self.get_height(vertex.left), self.get_height(vertex.right)) + 1


# Your Codec object will be instantiated and called as such:

root = TreeNode(1)
# root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.left = TreeNode(4)
codec = Codec()
print(codec.deserialize('[1,2,null,3,null,4,null,5]'))

