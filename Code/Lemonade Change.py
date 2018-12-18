class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fiveDollars = 0
        tenDollars = 0
        for b in bills:
            if b == 5:
                fiveDollars += 1
            elif b == 10:
                if fiveDollars < 1:
                    return False
                fiveDollars -= 1
                tenDollars += 1
            else:
                if tenDollars > 0:          #If the bill is $20, prioritize to provide exchange in $10.
                    tenDollars -= 1
                    if fiveDollars < 1:
                        return False
                    fiveDollars -= 1
                else:
                    if fiveDollars < 3:
                        return False
                    fiveDollars -= 3
        return True
