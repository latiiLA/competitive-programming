class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = defaultdict(list)
        trusted = []
        # returns 1 when there is only one person.
        if n == 1:
            return 1

        # loops through the trust list and creates a dictionary with they count of vote. while doing that it also keeps tract of voters in trusted list
        for trst in trust:
            trust_count[trst[1]] = trust_count.get(trst[1], 0) + 1
            trusted.append(trst[0])

        # loops through the dictionary and finds where all people votes for one person excepts himself
        for trst in trust_count:
            if trst in trusted and trust_count[trst] == n - 1:
                return -1
            if trust_count[trst] == n - 1:
                return trst
        
        # this does not do anything. it just stays there for beauty. haha
        return -1