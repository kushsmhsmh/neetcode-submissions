from typing import  List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqcounter = Counter(nums)
        mostcommon = freqcounter.most_common(k)
        result = [element for element, count in mostcommon]

        return result