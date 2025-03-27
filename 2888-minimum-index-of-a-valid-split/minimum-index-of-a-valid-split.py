from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the overall dominant element in the entire array
        freq = Counter(nums)
        dominant = max(freq, key=freq.get)  # Most frequent element in the array
        
        total_count = freq[dominant]  # Total occurrences of dominant in nums
        left_count = 0  # Count of dominant element in left subarray
        
        # Step 2: Iterate through the array while updating prefix count
        for i in range(len(nums) - 1):  # Stop at second last element
            if nums[i] == dominant:
                left_count += 1
            
            right_count = total_count - left_count  # Remaining occurrences in right part
            
            # Step 3: Check dominant conditions for valid split
            if (2 * left_count > (i + 1)) and (2 * right_count > (len(nums) - (i + 1))):
                return i
        
        return -1
