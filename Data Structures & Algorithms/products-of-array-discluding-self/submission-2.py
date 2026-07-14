class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for i in nums:
            if len(set(nums)) == 1 and 0 in set(nums) or nums.count(0) > 1:
                prod = 0    
            else:
                if i != 0:
                    prod *= i
        res = nums
        for i in range(len(nums)):
            if nums[i] != 0:
                if 0 not in nums:
                    res[i] = prod // nums[i]
                else:
                    res[i] = 0
            else:
                res[i] = prod
        return res