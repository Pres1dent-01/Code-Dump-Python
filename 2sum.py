class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                myval = nums[i]+nums[j]
                if myval == target:
                    return [i, j]


nums = [2, 7, 9, 11]
target = 9
sol = Solution()
result = sol.twoSum(nums, target)
print(result)
