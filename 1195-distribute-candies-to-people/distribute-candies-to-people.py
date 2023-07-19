class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        finalDistriOfCandies = [0]*num_people
        lastcandiedist = 0
        while candies>0:
            for i in range(len(finalDistriOfCandies)):
                if candies>lastcandiedist:finalDistriOfCandies[i]+=lastcandiedist+1
                else:
                    finalDistriOfCandies[i]+=candies
                    candies-=candies
                    break
                lastcandiedist+=1
                candies-=lastcandiedist
        return finalDistriOfCandies

