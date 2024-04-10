class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()                                        #Sort deck.
        result = [0] * len(deck)                           #Initialize result.
        q = deque([i for i in range(len(deck))])           #Store the indexes in a queue.
        index = 0                                          #Pointer in deck.
        while q:                                           #Iterate while q is not empty.
            i = q.popleft()                                #Pop left from queue to take the top card of deck.
            result[i] = deck[index]                        #Assign current smallest number here.
            index += 1                                     #Move to next.
            if q:                                          #If queue is not empty, pop left then append it to the tail.
                q.append(q.popleft())
        return result
