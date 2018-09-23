class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        k = max(len(i) for i in nums)
        for i in range(len(nums)):
            s = ''.join(nums[i][j % len(nums[i])] for j in range(k * 2))
            nums[i] = (nums[i], s)
        nums = sorted(nums, key=lambda x: x[1])
        s = ''.join(num[0][::-1] for num in nums)
        if s[-1] == '0':
            return '0'
        else:
            return s[::-1]


a = Solution()
print(a.largestNumber([0, 0]))
print(a.largestNumber([3,30,34,5,9]))