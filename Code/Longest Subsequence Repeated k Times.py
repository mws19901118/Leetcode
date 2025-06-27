class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        result = ""
        candidates = sorted([c for c, w in Counter(s).items() if w >= k], reverse = True)   #Characters in the subsequence should have at least k occurrences; sort them in descending order.
        q = deque(candidates)                                                               #Put them in a queue.
        while q:                                                                            #Iterate while q is not empty.
            curr = q.popleft()                                                              #Popleft q to get current subsequence.
            if len(curr) > len(result):                                                     #If it is longer than result, so update result.
                result = curr
            for x in candidate:                                                             #Traverse candidate.
                next = curr + x                                                             #Append it to current subsequence.
                itr = iter(s)                                                               #Use an iterator to traverse s.
                if all(x in itr for x in next * k):                                         #Make sure the new subsequence has occurred k times in s.
                    q.append(next)                                                          #If so, append next to q.
        return result
