class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        division = 10 ** 9 + 7                                                                                                #Initialize division.
        @cache                                                                                                                #Cache result.
        def dp(unplayed: int, remain: int) -> int:                                                                            #Suppose we fix the sequence of unplayed songs from 1 to n, use DP to find out the number of playlist with given unplayed songs and remain slots.
            if unplayed > remain or unplayed < 0:                                                                             #If there are more unplayed songs than remain slots or negative unplayed songs, both is invalid case so return 0.
                return 0
            elif unplayed == remain:                                                                                          #If there are exactly same unplayed songs and remain slots, we should just play all unplayed songs, so return 1.
                return 1
            return (dp(unplayed - 1, remain - 1) + max(n - unplayed - k, 0) * dp(unplayed, remain - 1)) % division            #1. play a unplayed song at current slot, then keep dp.
                                                                                                                              #2. we have played n - unplayed songs and we can replay max(n - unplayed - k, n) songs at current slot, the keep dp.
                                                                                                                              #Sum up dp results from these 2 scenarios and take the modulo then return. 

        return dp(n, goal) * math.factorial(n) % division                                                                     #Get dp(n, goal) and multiply it with n! (because we have fixed the sequence but there are n! such sequence) then take the modulo and return.
