class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)                            #Sort piles in descending order.
        start, end, result = 0, len(piles) - 1, 0             #Since we always got the middle of 3 piles, we should always choose the largest 2 piles and the smallest pile in remaining piles. So, initialize pointer from start and end; also initialize result.
        while start < end:                                    #Iterate while start hasn't meet end yet.
            result += piles[start + 1]                        #Add piles[start + 1](the middle pile) tp result.
            start += 2                                        #Move the largest 2 piles out.
            end -= 1                                          #Move the smallest pile out.
        return result
