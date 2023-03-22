# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def extractHost(url: str) -> str:                                               #Extract host name from url, removing "http://", then split by "/" and take the first one.
            return url[7:].split("/")[0]
        
        host = extractHost(startUrl)                                                    #Extract host from startUrl.
        q = [startUrl]
        visited = set([startUrl])
        while q:                                                                        #BFS.
            newq = []
            for x in q:                                                                 #For each x in q, get the urls from x.
                nextUrls = htmlParser.getUrls(x)
                for y in nextUrls:                                                      #For each url, if its host is same as host and is not visited, append it to newq and add it to visited.
                    if extractHost(y) == host and y not in visited:
                        newq.append(y)
                        visited.add(y)
            q = newq
        return list(visited)                                                            #Convert visited to list and return.
