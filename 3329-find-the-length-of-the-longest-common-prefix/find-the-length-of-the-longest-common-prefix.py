class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        longestPrefixLen = 0
        arr1_prefix = set()
        for val in arr1:
            while val not in arr1_prefix and val>0:
                arr1_prefix.add(val)
                val//=10
                
        for val in arr2:
            while val not in arr1_prefix and val>0:
                val//=10
            if val>0:
                longestPrefixLen = max(longestPrefixLen, len(str(val)))
                
        return longestPrefixLen
