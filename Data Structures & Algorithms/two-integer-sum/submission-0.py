class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        ind = []
        for i in range(0, l):
            for j in range(0, i):
                if i != j:
                    if ((nums[i] + nums[j]) == target):
                        if j < i:
                            ind.append(j)
                            ind.append(i)
                            return ind
                        else:
                            ind.append(i)
                            ind.append(j)
                            return ind
                else:
                    j += 1
            i += 1