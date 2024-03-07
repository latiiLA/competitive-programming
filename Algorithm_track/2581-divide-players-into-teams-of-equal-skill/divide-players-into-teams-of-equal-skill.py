class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()

        left = 0
        right = len(skill) - 1

        totalSkill = 0
        size = skill[left] + skill[right]

        while left < right:
            temp = skill[left] + skill[right]
            if temp == size:
                totalSkill += (skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                return -1
        
        return totalSkill