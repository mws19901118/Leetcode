class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = Counter(secret)                                 #Count each number in secret.
        bull, cow = 0, 0
        for i, x in enumerate(guess):                           #First pass find all bulls and update count.
            if x == secret[i]:
                bull += 1
                count[x] -= 1
        for i, x in enumerate(guess):                           #Second pass find all cows(does not equal to corresponding number in secret and count not equal to 0) and update count.
            if x != secret[i] and count[x] != 0:
                cow += 1
                count[x] -= 1
        return str(bull) + "A" + str(cow) + "B"
