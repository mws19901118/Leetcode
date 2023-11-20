class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefixSum = [0]                                                            #Initialize prefix sum to be the travel time from house 0 to each house.
        for x in travel:                                                           #Populate prefixSum.
            prefixSum.append(prefixSum[-1] + x)
        lastM, lastP, lastG = 0, 0, 0                                              #Initialize the last house having M, P and G respectively.
        count = 0                                                                  #Initialize total time.
        for i, x in enumerate(garbage):                                            #Traverse grabage.
            if 'M' in x:                                                           #Set lastM to i if current house has M.
                lastM = i
            if 'P' in x:                                                           #Set lastP to i if current house has P.
                lastP = i
            if 'G' in x:                                                           #Set lastG to i if current house has G.
                lastG = i
            count += len(x)                                                        #Increase len(x) to count as each garbage requires one minute to collect.
        return count + prefixSum[lastM] + prefixSum[lastP] + prefixSum[lastG]      #Return count plus the sum of travel time to lastM, lastP, lastG respectively.
