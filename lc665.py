class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return True
        pivot = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot += 1
                if pivot == 2:
                    return False
                if (i > 0 and nums[i - 1] > nums[i + 1]) and (i < len(nums) - 1 and nums[i] > nums[i + 2]):
                    return False
        return True


a = Solution()
print(a.checkPossibility([2,3,3,2,4]))