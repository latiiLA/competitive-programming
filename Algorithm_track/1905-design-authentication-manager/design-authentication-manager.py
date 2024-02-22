class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.generatedTokens = {} #stores the grenerated tokes expiry time  (currentTime + timeToLive)
        self.timeToLive = timeToLive 

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.generatedTokens[tokenId] = self.timeToLive + currentTime        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.generatedTokens and self.generatedTokens[tokenId] > currentTime:
            self.generatedTokens[tokenId] = self.timeToLive + currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0

        for tokenId in self.generatedTokens:
            if self.generatedTokens[tokenId] > currentTime:
                count += 1
        
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)