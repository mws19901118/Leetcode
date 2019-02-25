class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W:                                             #If the number of cards is not a multiple of W, return false.
            return False
        d = collections.Counter(hand)                                 #Count each card.
        sortedCards = sorted(d.keys())                                #Sort unique card.
        sortedCards = collections.deque(sortedCards)
        while len(d) > 0:                                             #While there are cards remanining.
            minCard = sortedCards[0]                                  #Find the smallest card.
            temp = d[minCard]                                         #Use a temp value to store current count of smallest card.
            for i in range(W):                                        #For W consecutive number starting from the smallest card.
                if minCard + i not in d or d[minCard + i] < temp:     #If it's not in hand or its count is smaller than the smallest card, the cards cannot form satisfied group for all smallest card, then return false.
                    return False
                d[minCard + i] -= temp                                #Subtracting the count of smallest card from each card to get the remain card.
                if d[minCard + i] == 0:                               #If no card remain, delete it from d and pop left of sorted cards(it is guarenteed to be the current smallest card).
                    del d[minCard + i]
                    sortedCards.pop(0)
        return True
