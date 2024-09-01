class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        cheeses = sorted([(x - y, x, y) for x, y in zip(reward1, reward2)], reverse = True)      #Sort the rewards by the more points mouse 1 can get more than mouse 2 in desending order.
        return sum(x for _, x, y in cheeses[:k]) + sum(y for _, x, y in cheeses[k:])             #For first k cheeses, let mouse 1 eat them; then let mouse 2 eat the rest.
