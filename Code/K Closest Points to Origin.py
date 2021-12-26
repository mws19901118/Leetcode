class Solution:
    def findK(self, distances: List[tuple], k: int) -> int:                                                                                     #Find the k-th smallest distance. 
        randomD = distances[0][2]
        lower, upper = list(filter(lambda x: x[2] <= randomD, distances[1:])), list(filter(lambda x: x[2] > randomD, distances[1:]))
        if len(lower) == k - 1:
            return randomD
        elif len(lower) > k - 1:
            return self.findK(lower, k)
        else:
            return self.findK(upper, k - len(lower) - 1)
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(p[0], p[1], p[0] * p[0] + p[1] * p[1]) for p in points]                                                                   #Convert the list of point to a list of tuple where the first 2 elements are point and third element is distance to origin.
        kth = self.findK(distances, k)                                                                                                          #Find the k-th smallest distance.
        return [[d[0], d[1]] for d in distances if d[2] <= kth]                                                                                 #Return the points whose distance is no larger than k-th smallest distance.
