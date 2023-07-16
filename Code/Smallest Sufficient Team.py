class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skillMasks = {}                                                                          #Store bit masks for each skill.
        currentMask = 1
        for x in req_skills:                                                                     #Traverse req_skills and assign one bit mask to each skill. 
            skillMasks[x] = currentMask
            currentMask <<= 1
        allRequiredMask = currentMask - 1                                                        #The bit mask for all required skill is the OR result of all the bit masks of skills.
        peopleMasks = [0] * len(people)                                                          #Store bit masks for the skills of each person.
        for i, p in enumerate(people):                                                           #Traverse people and compute the OR result of skills of the person as its mask.
            for x in p:
                peopleMasks[i] |= skillMasks[x]

        @cache                                                                                   #Cache result.
        def dp(index: int, mask: int) -> List[int]:                                              #DP to find the smallest sufficient team in people[index:] with a mask of already found skills.
            if mask == allRequiredMask:                                                          #If current mask equals to allRequiredMask, we already found a sufficient team, return an empty list.
                return []
            if index == len(people):                                                             #Otherwise if index reaches the end of people, there is no valid team, return none.
                return None
            pick, notPick = dp(index + 1, mask | peopleMasks[index]), dp(index + 1, mask)        #Find the team of picking and not picking current person respectively.
            if pick is not None and (notPick is None or len(pick) + 1 < len(notPick)):           #If the team of picking is valid and the team of not picking is invalid or the team of picking plus one is smaller than the team of not picking, return current person with team of picking.
                return [index] + pick
            else:                                                                                #Otherwise, return the team of not picking.
                return notPick
        
        return dp(0, 0)                                                                          #Return dp(0, 0).
