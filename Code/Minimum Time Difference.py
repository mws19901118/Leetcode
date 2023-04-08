class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted([int(x[:2]) * 60 + int(x[3:]) for x in timePoints])                #Convert time point to minutes and sort in asending order.
        minutes.append(minutes[0] + 1440)                                                   #Append minutes[0] + 1440 to minutes.
        return min(minutes[i] - minutes[i - 1] for i in range(1, len(minutes)))             #Find the min difference between 2 adjacent minutes and return.
