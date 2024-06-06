class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)                                #Count each card.
        cardValue = sorted(count.keys())                     #Sort card value in asending order.
        for x in cardValue:                                  #Traverse card value.
            if not count[x]:                                 #If current card is processed, skip.
                continue
            currentCount = count[x]                          #Store current count.
            for i in range(groupSize):                       #Traverse the card value that form a group with current value as start.
                if count[x + i] < currentCount:              #If any value has fewer count than current count, return false.
                    return False
                count[x + i] -= currentCount                 #Deduct currentCount from the count of current card.
        return True                                          #Return true at the end.
