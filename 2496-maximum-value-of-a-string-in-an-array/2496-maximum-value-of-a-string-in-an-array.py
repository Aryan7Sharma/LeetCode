class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_leng = 0
        for i in strs:
            if i.isnumeric():
                max_leng = max(max_leng, int(i))
            else:
                max_leng = max(max_leng, len(i))
        return max_leng