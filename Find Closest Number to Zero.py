class Solution(object):
        def findClosestNumber(self, nums):
            if not nums:
                return None
            nums.sort()
            closest = nums[0]
            for i in range(1, len(nums)):
                if abs(nums[i]) < abs(closest):
                    closest = nums[i]
                elif abs(nums[i]) == abs(closest) and nums[i] > closest:
                    closest = nums[i]
            print("Closest number to zero:", closest)
            return closest

sol = Solution()
nums = [2,-1,1]
sol.findClosestNumber(nums)