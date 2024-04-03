class Codec:
    # def Solution(self):
    step = 0
    dictionary = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url = "http://tinyurl.com/"
        url = url + str(self.step)
        self.dictionary[url] = longUrl
        self.step += 1
        return url
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dictionary[shortUrl]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))