class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = set(nums)
        longest = 0
        for num in l:
            if num - 1 not in l:
                curr = num
                streak = 1

                while curr + 1 in l:
                    curr += 1
                    streak += 1
                
                longest = max(longest, streak)

        return longest