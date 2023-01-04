class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap = {}
        for i in s1.split(" "):
            hashmap[i] = hashmap.get(i, 0) + 1
        for i in s2.split(" "):
            hashmap[i] = hashmap.get(i, 0) + 1
        return [word for word in hashmap if hashmap[word]==1]
        