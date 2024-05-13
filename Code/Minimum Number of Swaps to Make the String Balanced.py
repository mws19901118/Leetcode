class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0                           #Use count to all unmatched '['.
        for x in s:                         #Traverse s.
            if count and x == ']':          #If count is greater than 0 and x is ']', decrease count.
                count -= 1
            elif x == '[':                  #If x is '[', increase count.
                count += 1
        return (count + 1) // 2             #After traversing and removing all matched pairs, the remain is exactly count ']' then count '[' because their total count is same. So, one swap count balance 2 pairs, and it there is a final pair left, it requires one more swap. Thus, total swap needed is (count + 1) // 2.
