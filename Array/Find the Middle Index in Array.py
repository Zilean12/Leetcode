class Solution(object):
    def findMiddleIndex(self, nums):
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
sol = Solution()
nums = [2, 3, -1, 8, 4]
print(sol.findMiddleIndex(nums))
