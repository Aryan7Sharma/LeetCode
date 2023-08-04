class Solution:
    def bestClosingTime(self, customers: str) -> int:
        hashmap = {}
        length = len(customers)
        countY,countN = 0,0
        miniPenHour = 0
        for i in range(length):
            if customers[i]=="Y":countY+=1
            else:countN+=1
            hashmap[i]=[countY,countN]
        #print(hashmap)

        penalty = hashmap[length-1][0]
        for v in range(1,length):
            currpenalty = 0
            if customers[v]=="Y":currpenalty+=1
            #print(v,currpenalty)
            currpenalty+= hashmap[v-1][-1] + (hashmap[length-1][0]-hashmap[v][0])
            #print(v,currpenalty) 
            if  currpenalty<penalty:
                penalty = currpenalty
                miniPenHour = v
        if penalty>hashmap[length-1][-1]:miniPenHour=length
        return miniPenHour



            
