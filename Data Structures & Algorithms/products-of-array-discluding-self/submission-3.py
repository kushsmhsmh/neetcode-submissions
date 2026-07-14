class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        leftpass = 1
        for i in range(n):
            ans[i] = leftpass
            leftpass *= nums[i]

        rightpass = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= rightpass
            rightpass *= nums[i]
        
        return ans