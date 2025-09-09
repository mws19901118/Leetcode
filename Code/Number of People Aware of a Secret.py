class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        division = 10 ** 9 + 7                                                                                             #Initialize division.
        dp = [1]                                                                                                           #Initialize dp array, dp[i] means the people learn the secret at day i + 1.
        count = 0                                                                                                          #Initialize the people who can share the secret now.
        for i in range(1, n):                                                                                              #Traverse from 1 to n - 1.
            count = (count + (0 if i < delay else dp[i - delay]) - (0 if i < forget else dp[i - forget])) % division       #Update count to add new people who can start to share secret and deduct the people just forget the secret.
            dp.append(count)                                                                                               #Append count to dp.
        return sum(dp[-forget:]) % division                                                                                #Return the sum of people who haven't forgot the secret then take modulo and return.
