from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Merge intervals
        meetings.sort(key=lambda x: x[0])
        merged = []
        
        for start, end in meetings:
            if not merged or merged[-1][1] < start - 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        
        # Calculate total meeting days
        total_meeting_days = sum(e - s + 1 for s, e in merged)
        return days - total_meeting_days
