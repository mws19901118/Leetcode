class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = defaultdict(int)                                                                 #Count the number of lost of each player.
        players = set()                                                                         #Store all players in set.
        for w, l in matches:                                                                    #Traverse matches.
            players.add(w)                                                                      #Add winder to players.
            players.add(l)                                                                      #Add loser to players.
            lost[l] += 1                                                                        #Increase lost count for loser.
        players = sorted(list(players))                                                         #Sort players.
        return [[x for x in players if x not in lost], [x for x in players if lost[x] == 1]]    #Return the zero loss players and one loss players.
