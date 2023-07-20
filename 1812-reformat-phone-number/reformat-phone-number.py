class Solution:
    def reformatNumber(self, number: str) -> str:
        number = "".join([n  for n in number if n.isalnum()])
        print(number)
        l = len(number)
        i = 0
        formatedNumber = ""
        while i<l-4:
            formatedNumber+=number[i:i+3]+'-'
            i+=3
        if l-i==4:formatedNumber+= number[i:i+2]+ '-' + number[i+2:]
        else:formatedNumber+=number[i:]
        return formatedNumber