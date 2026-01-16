class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def findAllGaps(fences: List[int], edge: int) -> Set[int]:                                                          #Find all gaps can be made given fences and the edge of fences.
            allFences = sorted([1] + fences + [edge])                                                                       #Add 2 edges(1 and edge) then sort.
            return set(allFences[j] - allFences[i] for i in range(len(allFences)) for j in range(i + 1, len(allFences)))    #Put all possible distances between 2 fences in a set then return.
        hGaps, vGaps = findAllGaps(hFences, m), findAllGaps(vFences, n)                                                     #Find all horizontal gaps and vertical gaps.
        intersection = hGaps & vGaps                                                                                        #Calculate the intersection.
        return -1 if not intersection else max(intersection) ** 2 % (10 ** 9 + 7)                                           #If no intersection, we cannot make any square so return -1; otherwise, the length of max area square is the max gap in intersection, so calculate the area and take modulo then return.
