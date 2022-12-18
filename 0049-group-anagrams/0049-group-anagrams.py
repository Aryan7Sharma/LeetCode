class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dicts=defaultdict(list)
        for i in strs:
            dicts["".join(sorted(i))].append(i)
        return dicts.values()