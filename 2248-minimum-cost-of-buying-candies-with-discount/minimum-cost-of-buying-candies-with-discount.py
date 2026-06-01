class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        total_cost = 0
        took=0
        for i in range(len(cost)-1,-1,-1):
            if took==2:
                took=0
            else:
                total_cost+=cost[i]
                took+=1
        return total_cost