class Solution(object):
    def findKth(self, dist, K):                                             #Find the K-th distance in dist.
        if len(dist) == 1:
            return dist[0][0]
        randomD = dist[0][0]
        lower = filter(lambda x: x[0] < randomD, dist[1:])
        upper = filter(lambda x: x[0] > randomD, dist[1:])
        if len(lower) == K - 1:
            return randomD
        elif len(lower) < K - 1:
            return self.findKth(upper, K - 1 - len(lower))
        else:
            return self.findKth(lower, K)
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist = map(lambda p: (p[0] * p[0] + p[1] * p[1], p), points)      #Convert the list of point to a list of tuple where the first element is distance to origin and second element is point.
        
        kthD = self.findKth(dist, K)                                      #Find the K-th closet distance.
        
        return map(lambda x: x[1], filter(lambda x: x[0] <= kthD, dist))  #Covert all tuples whose distance is smaller than or equal to kthD back to point.
