class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        unique_nums = list(set(nums))
        return unique_nums
sol = Solution()
print(sol.removeDuplicates([0,0,2,3,5,4,5,1,1,1,2,2,3,3,4]))
