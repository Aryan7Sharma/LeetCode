class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length =  len(arr)
        i = 0
        while i<length:
            if arr[i] == 0:
                arr[:] = arr[:i+1] + arr[i:length-1]
                i+=1
            i+=1