class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        digitLen = len(digits)
        if digitLen<2:return list(phone[digits])
        # 2 digits and 3 digits
        result = []
        if digitLen==2:
            for i in phone[digits[0]]:
                for j in phone[digits[1]]:
                    value = i+j
                    result.append(value)
            return result
        if digitLen==3:
            for i in phone[digits[0]]:
                    for j in phone[digits[1]]:
                        for k in phone[digits[2]]:
                            value = i+j+k
                            result.append(value)
            return result
        for i in phone[digits[0]]:
                for j in phone[digits[1]]:
                    for k in phone[digits[2]]:
                        for l in phone[digits[3]]:
                            value = i+j+k+l
                            result.append(value)
        return result