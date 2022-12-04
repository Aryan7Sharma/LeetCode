class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        skills.sort()
        print(skills)
        l=1
        r=len(skills)-2
        temp=skills[0]+skills[-1]
        ans=skills[0]*skills[-1]
        while l<r:
            if temp == skills[l]+skills[r]:
                ans+=skills[l]*skills[r]
                l+=1
                r-=1
            else:
                return -1
        return ans