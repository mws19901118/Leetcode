class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        flowers = sorted([(g, p) for g, p in zip(growTime, plantTime)], reverse = True)         #Sort each (growTime, plantTime) tuple by growTime in descending order.
        result, spent = 0, 0                                                                    #Initialize result and time spect on plant so far. The idea is to plant flowers with longer grow time as earlier as possible.
        for g, p in flowers:                                                                    #Traverse tuples.
            spent += p                                                                          #Add current plant time to spent.
            result = max(result, spent + g)                                                     #The earliest bloom time is spect + grow time and update result if possible.
        return result
