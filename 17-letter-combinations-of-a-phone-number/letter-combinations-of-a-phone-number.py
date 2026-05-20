class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        combe = list(phone[digits[0]])
        for i in range(1,len(digits)):
            result = [] 
            for j in phone[digits[i]]:
                for com in combe:result.append(com+j)
            combe = result
        return combe  
