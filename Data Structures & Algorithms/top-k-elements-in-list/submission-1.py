from typing import  List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        bucket = [[] for j in range(n + 1)]
        for key in d:
            bucket[d[key]].append(key)

        res = []
        for i in range(n, 0, -1):
            if len(res) >= k:
                break
            for val in bucket[i]:
                res.append(val)
        return res