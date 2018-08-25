class Solution:

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.ans = []
        if digits != '':
            self.recursive_comb(digits, '')
        return self.ans

    def recursive_comb(self, digits, s):
        if digits == '':
            self.ans.append(s)
            return
        keypad = [[' '], [''], ['a','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l'], ['m','n','o'], ['p','q','r','s'], ['t','u','v'],['w','x','y','z']]
        k = int(digits[0])
        for j in keypad[k]:
            self.recursive_comb(digits[1:], s+j)



a = Solution()
print(a.letterCombinations(""))