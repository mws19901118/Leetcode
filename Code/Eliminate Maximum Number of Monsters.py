class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrivingTime = sorted([ceil(d / s) for d, s in zip(dist, speed)])        #Sort the arriving minutes of each monster in asending order.
        for i, x in enumerate(arrivingTime):                                     #Eliminate the monsters arriving sooner first.
            if x <= i:                                                           #If x <= i, cannot eliminate current monster before it arrives, so return i.
                return i
        return len(arrivingTime)                                                 #Return len(arrivingTime) if we can eliminate all monsters.
