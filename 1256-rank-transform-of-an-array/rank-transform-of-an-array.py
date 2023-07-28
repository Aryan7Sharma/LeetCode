class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(arr)
        hashmap = {}
        rank=1
        for i in sortedArr:
            if i not in hashmap:
                hashmap[i]=rank
                rank+=1
        for v in range(len(arr)):
            arr[v] = hashmap[arr[v]]
        return arr