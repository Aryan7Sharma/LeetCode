class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        lastNum = -1
        s = s.split(' ')
        for i in s:
            if i.isdigit():
                if int(i)<=lastNum:return False
                else:lastNum = int(i)
        return True