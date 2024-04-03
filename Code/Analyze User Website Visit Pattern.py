class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        activity = defaultdict(list)                                                                          #Store activity of each user.
        for u, t, w in zip(username, timestamp, website):                                                     #Traverse username, timestamp and website simultaneously to group the timestamp and website by user.
            activity[u].append((t, w))
        patternScore = defaultdict(set)                                                                       #Store the distinct user of each pattern.
        for u in activity:                                                                                    #Traverse activity by user.
            activity[u].sort()                                                                                #Sort the activity of current user by timestamp.
            for i in range(len(activity[u]) - 2):                                                             #Enumerate all patterns for current user and populate patternScore.
                for j in range(i + 1, len(activity[u]) - 1):
                    for k in range(j + 1, len(activity[u])):
                        patternScore[(activity[u][i][1], activity[u][j][1], activity[u][k][1])].add(u)
        maxScore, pattern = -1, None
        for k, v in patternScore.items():                                                                     #Traverse patternScore to find the pattern with largest score(most distinct users) or the lexicographically smallest pattern if there is a tie on score.
            if maxScore < len(v) or (maxScore == len(v) and k < pattern):
                maxScore = len(v)
                pattern = k
        return list(pattern)                                                                                  #Convert pattern to list and return.
