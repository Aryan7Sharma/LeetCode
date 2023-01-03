class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        from itertools import chain
        decompressList = []
        for i in range(0, len(nums), 2):
            decompressList.append([nums[i+1]]*nums[i])
        return list(chain(*decompressList))
        