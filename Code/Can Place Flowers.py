class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lastFlower = -2                                           #Imagine there is a plated spot and an empty spot on the left of flowerbed, so the extended array always starts with 1 but the total flower can plated stay same. 
        for i, x in enumerate(flowerbed):                         #Traverse through flower bed.
            if x:                                                 #If current flower is plated, get the distance between current spot and last spot of plated flower.
                n -= (i - lastFlower - 2) // 2                    #We can plan as many as (distance - 1) // 2 flowers in between.
                lastFlower = i                                    #Update last spot of plated flower.
        n -= (len(flowerbed) + 1 - lastFlower - 2) // 2           #Imagine there is an empty spot and a plated spot on the right of flowerbed, so the extended array always ends with 1 but the total flower can plated stay same. 
        return n <= 0                                             #If n <= 0, all flowers can be plated; otherwise cannot.
