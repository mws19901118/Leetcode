class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        language_set = {i + 1:set(x) for i, x in enumerate(languages)}        #Convert the languages of each user to a set per user.
        language_user = {i + 1:set() for i in range(n)}                       #Store the user set of each language
        for i, x in enumerate(languages):                                     #Traverse languages and compute the user set of each language.
            for y in x:
                language_user[y].add(i + 1)
        teach = set()                                                         #Store the set of users who has at least one friend that cannot communicate with.
        for u, v in friendships:                                              #Traverse friendships.
            if not language_set[u] & language_set[v]:                         #If no intersection between the languages u speaks and languages v speaks, u and v cannot communicate.
                teach.add(u)                                                  #Add u to teach.
                teach.add(v)                                                  #Add v to teach.
        return min(len(teach - x) for x in language_user.values())            #Find the languages already covered the most users in teach set, then the rest are minimum number of users to teach.
