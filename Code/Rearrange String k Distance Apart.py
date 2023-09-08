class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        c = Counter(s)                                              #Count each distinct character in s.
        heap = [(-value, key) for key, value in c.items()]          #Use a max heap to store the count and character, representing the available characters.
        heapq.heapify(heap)
        dq = deque()                                                #Use deque to store the used characters in past k - 1 characters.
        result = []                                                 #Initialize result.
        for i in range(len(s)):                                     #Iterate the length of s.
            if dq and i - dq[0][0] >= k:                            #If dq is not empty and the start of queue is on index which is at least k characters away from current character, release it and its count from dq and push them to heap. 
                heapq.heappush(heap, dq.popleft()[1])
            if not heap:                                            #If heap is empty, we cannot find any character to put on current index, so return "" directly.
                return ""
            count, character = heapq.heappop(heap)                  #Pop the top of heap, since we always want to put characters whose count is higest first to reduce chance of not able to arrange in the future.
            result.append(character)                                #Set current character to the character just popped from heap.
            if count + 1 < 0:                                       #If the remain count is greater than 0, append it and its count with current index to dq.
                dq.append((i, (count + 1, character)))
        return "".join(result)                                      #Join result and return.
