class Solution:
    def maxA(self, n: int) -> int:
        a = [0] * (n + 1)                                                                             #Initialize the array of max characters after each types.
        for i in range(1, n + 1):                                                                     #Iterate from 1 to n.
            a[i] = max(a[i - 1] + 1, a[max(0, i - 4)] * 3, a[max(0, i - 5)] * 4)                      #a[i] is the max of typing after a[i - 1], pasting a[i - 4] twice and pasting a[i - 5] three times. No need to paste more or less, since it does not provide as much as gain.
        return a[-1]                                                                                  #Return a[-1].
