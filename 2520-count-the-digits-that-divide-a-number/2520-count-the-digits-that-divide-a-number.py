class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp_num = num
        while temp_num:
            digit = temp_num % 10
            if num%digit == 0:
                count+=1
            temp_num = temp_num//10
        return count
        