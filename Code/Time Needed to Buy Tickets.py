class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(x, tickets[k]) for x in tickets[:k + 1]) + sum(min(x, tickets[k] - 1) for x in tickets[k + 1:])          #For all people at k or in front of k will buy at most tickets[k] tickets to buy and all people after k will buy at most tickets[k] - 1 tickets.
