from collections import defaultdict
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        voteCounter = []                                      #For each postion, count the vote for each team.
        for i in range(n):
            voteCounter.append(defaultdict(int))
            for j in range(len(votes)):
                voteCounter[i][votes[j][i]] += 1
        
        remaining = set(list(votes[0]))                       #Use set to store unranked teams.
        ranking = []                                          #Store the ranking in a list.
        while len(ranking) < n:                               #While ranking is not finished, find the team which should be at current rank.
            i = 0
            candidates = list(remaining)                      #Get the candidates teams whose possible to be at current rank, initally all remaining teams are candidates.
            while i < n and len(candidates) > 1:              #From the first position to the last position, narrow down candidates, the teams with highest vote count in current position, until only one candidate left.
                maxVote = -1
                candidatesThisLevel = []
                for x in candidates:
                    if voteCounter[i][x] > maxVote:
                        maxVote = voteCounter[i][x]
                        candidatesThisLevel = [x]
                    elif voteCounter[i][x] == maxVote:
                        candidatesThisLevel.append(x)
                candidates = candidatesThisLevel
                i += 1

            candidates.sort()                                 #Sort the candidates alphabetically.
            for x in candidates:                              #By order, add each candidate team to ranking and remove them from remaining teams.
                ranking.append(x)
                remaining.remove(x)

        return "".join(ranking)                               #Join ranking to string and return.
        
        
        
        
from collections import defaultdict
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        voteCounters=defaultdict(int)
        n = len(votes[0])
        for vote in votes:                                                                      #Consider the each teams vote in all position as a vector.
            for i in range(n):                                                                  #Then, we can convert it to a weight in base-26 number.
                v = vote[i]                                                                     #it's unique to each team and higher ranking team has higher weight.
                voteCounters[v]+= 26 ** (n - i)

        ranking = list(votes[0])
        ranking.sort(key = lambda x: (-voteCounters[x], string.ascii_uppercase.index(x)))       #Sort by the weight and alphabet.
        return "".join(ranking)
