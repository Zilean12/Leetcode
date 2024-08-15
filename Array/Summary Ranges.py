class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        res = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                if nums[i - 1] != start:
                    res.append(str(start) + "->" + str(nums[i - 1]))
                else:
                    res.append(str(start))
                start = nums[i]
        if nums[-1] != start:
            res.append(str(start) + "->" + str(nums[-1]))
        else:
            res.append(str(start))
        return res

sol = Solution()
nums = [0,1,2,4,5,7]
print(sol.summaryRanges(nums))
