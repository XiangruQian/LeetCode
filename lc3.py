class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            dup = set()
            for j in range(i, len(s)):
                if s[j] not in dup:
                    dup.add(s[j])
                else:
                    break
            ans = max(ans, len(dup))
        return ans


a = Solution()
print(a.lengthOfLongestSubstring(" "))