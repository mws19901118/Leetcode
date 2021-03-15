class Codec:
    def __init__(self):
        self.cache = {}
        self.urlPrefix = "http://tinyurl.com/"
        self.randomLength = 6
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        randomString = ''.join(random.choices(string.ascii_uppercase + string.digits, k = self.randomLength))       #Generate random string.
        shortUrl = self.urlPrefix + randomString                                                                    #Join url prefix and random string to get shorteded url.
        self.cache[shortUrl] = longUrl                                                                              #Put it in cache as key and long url as value.
        return shortUrl                                                                                             #Return short url.

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl not in self.cache:                                                                              #If shortUrl not in cache, return none.
            return None
        return self.cache[shortUrl]                                                                                 #Otherwise return the corresponding long url.

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
