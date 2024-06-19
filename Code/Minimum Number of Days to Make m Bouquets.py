class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        @cache                                                                    #Cache result.
        def canMakeBouquets(threshold: int) -> bool:                              #Determine if it is possible to make bouquets with current days threshold.
            bouquet, flowers = 0, 0                                               #Count bouquet and consecutive flowers. 
            for x in bloomDay:                                                    #Traverse bloomDay.
                if x <= threshold:                                                #If x is not greater than threshold, increase cound of consecutive flowers.
                    flowers += 1
                else:                                                             #Otherwise, reset it to 0.
                    flowers = 0
                if flowers == k:                                                  #If there are k consecutive flowers, reset it to 0 and increase bouquet.
                    flowers = 0
                    bouquet += 1
                if bouquet == m:                                                  #If we have m bouquets already, return true.
                    return True
            return False                                                          #Return false if cannot make m bouquets.

        if k * m > len(bloomDay):                                                 #If the required flowers is more than total flowers, return -1.
            return -1
        start, end = min(bloomDay), max(bloomDay)                                 #Get the min value and max value in bloomDay.
        while start <= end:                                                       #Binary search for the min days needed.
            mid = (start + end) // 2
            if canMakeBouquets(mid) and not canMakeBouquets(mid - 1):
                return mid
            elif canMakeBouquets(mid - 1):
                end = mid - 1
            else:
                start = mid + 1
