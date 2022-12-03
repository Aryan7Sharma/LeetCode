class Solution:
    def interpret(self, command: str) -> str:
        ind = 0
        res = ""
        while ind<len(command):
            if command[ind] == '(':
                if command[ind+1] == ')':
                    res+="o"
                    ind+=2
                else:
                    res+="al"
                    ind+=4
            else:
                res+="G"
                ind+=1
        return res

