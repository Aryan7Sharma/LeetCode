class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        visited = {}
        count = 0
        for i in word:
            char = ord(i)
            if char not in visited:visited[char]=0
            if char<97:
                if char+32 in visited and visited[char+32]==0:
                    count+=1
                    visited[char]=1
                    visited[char+32]=1
            else:
                if char-32 in visited and visited[char-32]==0:
                    count+=1
                    visited[char]=1
                    visited[char-32]=1
        return count


        