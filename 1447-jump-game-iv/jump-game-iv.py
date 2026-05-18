class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n<=1:return 0
        indexHashTable = {}
        for i in range(n):indexHashTable.setdefault(arr[i], []).append(i)
        
        curr = [0]
        visited = {0}
        steps = 0
        while curr:
            #print("curr", curr)
            nxt = []
            for node in curr:
                if node == n-1:return steps
                for child in indexHashTable[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nxt.append(child)
                indexHashTable[arr[node]].clear()
                for child in [node-1, node+1]:
                    if 0<=child<n and child not in visited:
                        visited.add(child)
                        nxt.append(child)
            curr = nxt
            steps+=1
            
        return -1
