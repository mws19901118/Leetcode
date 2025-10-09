class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        prefixSum = [0]                                                              #Initialize perfix sum for skill.
        for x in skill:                                                              #Populate prefixSum.
            prefixSum.append(prefixSum[-1] + x)
        time = [0] * len(skill)                                                      #Initialize finish time of each wizard.
        for x in mana:                                                               #Traverse mana.
            startTime = max(t - prefixSum[i] * x for i, t in enumerate(time))        #For each wizard, to brew current mana after last mana finish time t, the start time has to be at least t - prefixSum[i] * x. So we have to calculate the largest start time.
            for i in range(len(time)):                                               #Then, use the start time to populate the finish time for current mana.
                time[i] = startTime + prefixSum[i + 1] * x
        return time[-1]                                                              #Return the last finish time.
