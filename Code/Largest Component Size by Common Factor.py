class UnionFind:                                                                            #Union Find.
    def __init__(self, val):
        self.val = val
        self.parent = self
        
    def union(self, uf):
        uf.find().parent = self.find()
        
    def find(self):
        if self.parent == self:
            return self
        self.parent = self.parent.find()
        return self.parent
    
class Solution:
    @cache
    def primeSet(self, n) -> set:                                                           #Find all prime factors of n with cache.
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return self.primeSet(n // i) | set([i])
        return set([n])
    
    def largestComponentSize(self, A: List[int]) -> int:
        unionFinds = {x: UnionFind(x) for x in A}                                           #Initialize union find for each number.
        numbersThatThisPrimeIsAFactor = defaultdict(list)                                   #Store all numbers that can be divided by each prime in dict. Key is prime, value is number list.
        for x in A:
            primes = self.primeSet(x)                                                       #Find the prime factors of number x.
            for p in primes:                                                                #Append x to the list of each prime factor.
                numbersThatThisPrimeIsAFactor[p].append(x)
        
        for _, p in numbersThatThisPrimeIsAFactor.items():                                  #Within the number list of each prime, union the union find representing each number.
            for i in range(len(p) - 1):
                unionFinds[p[i]].union(unionFinds[p[i + 1]])
        
        return max(Counter([unionFinds[x].find().val for x in A]).values())                 #Calculate the max count of individual union find group.
