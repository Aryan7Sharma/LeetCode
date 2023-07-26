class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        for i in arr:
            if i in hashmap:hashmap[i]+= 1
            else:hashmap[i] = 1
        largestLuckyNum = -1
        for k,v in hashmap.items():
            if k == v:largestLuckyNum = max(largestLuckyNum,k)
        return largestLuckyNum
