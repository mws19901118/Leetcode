class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return list(set(y for x, y in paths) - set(x for x, y in paths))[0]        #Return the only element that is in destinations but not in starts.
