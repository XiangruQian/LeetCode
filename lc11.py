class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area


a = Solution()
print(a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
