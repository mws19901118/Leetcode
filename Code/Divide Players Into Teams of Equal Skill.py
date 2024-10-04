class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = sum(skill)                                  #Calculate sum of skills.
        if s % (len(skill) // 2):                       #If sum cannot be divided by (n // 2), return -1.
            return -1
        target = s // (len(skill) // 2)                 #Calculate the target sum of each team.
        if max(skill) >= target:                        #If any skill is not smaller than target, return -1.
            return -1
        teams = Counter()                               #Count the unmatched teams by the skill of its first player.
        chemistry = 0
        for i, x in enumerate(skill):                   #Traverse skill.
            if teams[target - x]:                       #If current player can find a match in unmatched teams, match them as a team.
                chemistry += x * (target - x)           #Add the product of skills in team to chemistry.
                teams[target - x] -= 1                  #Decrease the count of unmatched teams.
            else:                                       #Otherwise, creat an unmatched team for current player.
                teams[x] += 1
        if any(x for x in teams.values()):              #If there are still unmatched team, return -1.
            return -1
        return chemistry
