class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        no_typeCandy = set(candyType)
        AliceEat = len(candyType)//2
        return AliceEat if AliceEat<=len(no_typeCandy) else len(no_typeCandy)
        