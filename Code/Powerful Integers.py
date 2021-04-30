class Solution:
    def findPowerUnderBound(self, num: int, bound: int) -> List[int]:
        powers = [1]                                                                            #Initialize powers with 1.
        if num > 1:                                                                             #If num > 1, find all pwers of num under bound.
            p = num
            while p < bound:
                powers.append(p)
                p *= num
        return powers
    
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        expx, expy = self.findPowerUnderBound(x, bound), self.findPowerUnderBound(y, bound)     #Find all the powers of x and y which is not larger than bound respectively.
        powerful = set()                                                                        #Use a set to store all possible powerful integers.
        for i in expx:
            for j in expy:
                if i + j <= bound:
                    powerful.add(i + j)                                                         #Traverse each pair of power of x and power y, if the sum of them is not larger than bound, add to the set.
                else:
                    break
        return list(powerful)                                                                   #Return the set as list.
