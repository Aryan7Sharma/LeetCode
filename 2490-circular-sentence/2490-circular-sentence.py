class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(" ")
        if sentence[0][0]!=sentence[-1][-1]:
            print(sentence[0][0],sentence[-1][-1])
            return False
        flag = True
        for i in range(len(sentence)-1):
            if sentence[i][-1]!=sentence[i+1][0]:
                flag = False
                break
        return flag