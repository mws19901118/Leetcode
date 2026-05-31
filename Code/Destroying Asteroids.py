class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()                        #Sort asteroids.
        for i, x in enumerate(asteroids):       #Traverse asteroids.
            if mass < x:                        #If mass < x, return false.
                return False
            mass += x                           #Add x to mass.
        return True                             #Return true at the end.
