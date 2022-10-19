class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count, heap, result = Counter(words), [], []          #Count each word.
        for x, c in count.items():                            #Push the count and word into a max heap.
            heapq.heappush(heap, (-c, x))
        for _ in range(k):                                    #Pop the top k count and word pair from heap and append word to result.
            c, x = heapq.heappop(heap)
            result.append(x)
        return result                                         #Return result.
        
