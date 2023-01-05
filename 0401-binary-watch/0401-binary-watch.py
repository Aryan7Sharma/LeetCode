class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for hour in range(12):
            for mins in range(60):
                if  (bin(hour)+bin(mins)).count('1') == turnedOn:
                    time = '%d:%02d'%(hour,mins)
                    res.append(time)
        return res
        