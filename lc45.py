class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        step = 0
        step_range = 0
        p = 0
        for i in range(n):
            if i + nums[i] >= p:
                if i + nums[i] >= n - 1:
                    return step + 1
                for j in range(i + nums[i] - p):
                    step.append(step + 1)
                p = i + nums[i]


a = Solution()
print(a.jump([0]))