class Solution(object):
    # def isValidSerialization(self, preorder):
    #     need = 1
    #     for val in preorder.split(','):
    #         if not need:
    #             return False
    #         need -= ' #'.find(val)
    #     return not need
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for vertex in preorder.split(','):
            if vertex != '#':
                stack.append(vertex)
            else:
                if stack and stack[-1] == '#':
                    stack.append('#')
                    while len(stack) >= 2 and stack[-1] == stack[-2] == '#':
                        stack.pop(-1)
                        stack.pop(-1)
                        if not stack or stack[-1] == '#':
                            return False
                        else:
                            stack[-1] = '#'
                else:
                    stack.append('#')
        return stack == ['#']


a = Solution()
print(a.isValidSerialization('#'))
