class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            sortedi = "".join(sorted(i))
            d[sortedi].append(i)
        return list(d.values())