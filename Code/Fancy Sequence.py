class Fancy:

    def __init__(self):
        self.division = 10 ** 9 + 7                                                                                          #Initialize division.
        self.values = []                                                                                                     #Store the values.
        self.k = 1                                                                                                           #Initialize the k of y = kx + b.
        self.b = 0                                                                                                           #Initialize the b of y = kx + b.

    def append(self, v: int) -> None:                                                       
        self.values.append((v - self.b) % self.division * pow(self.k, self.division - 2, self.division) % self.division)     #Given the current value v and the overall opeartion effects til now, try to reverse engineering the equivalent number of v when there are no operations.
                                                                                                                             #Since the effect is y = kx + b, get kx first. Then use Fermat's Little Theorem, which states that a ^ (MOD - 2) % MOD is the modular inverse of a when MOD is prime.
    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.division                                                                              #Increase inc to self.b.

    def multAll(self, m: int) -> None:
        self.k = (self.k * m) % self.division                                                                                #Multiply m to self.k.
        self.b = (self.b * m) % self.division                                                                                #Multiply m to self.b.

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):                                                                                          #If idx is greater than or equal to the length of values, return -1 as there is no corresponding value.
            return -1  
        return (self.k * self.values[idx] + self.b) % self.division                                                          #Apply the overall operation effects as a linear equation to self.values[idx] and return result.

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(v)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
