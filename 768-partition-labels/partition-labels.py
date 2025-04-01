class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {char: i for i, char in enumerate(s)}  # Store last occurrence of each character
        partitions = []
        start, end = 0, 0
        
        for i, char in enumerate(s):
            end = max(end, last_index[char])  # Extend partition to include last occurrence
            if i == end:  # If current index matches end, finalize partition
                partitions.append(end - start + 1)
                start = i + 1  # Start new partition
        
        return partitions
