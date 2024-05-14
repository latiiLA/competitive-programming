class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.votes = Counter()
        self.result = []
        self.times = times
        # [0, 1, 1, 0, 0, 1, 0]
        # 0 = 1, 1 = 1
        # [0,  1, 3, ]
        winner = [-1, -1]
        
        for i in range(len(persons)):
            self.votes[persons[i]] += 1
            # maximum = max(maximum, self.votes[persons[i]])
            if self.votes[persons[i]] >= winner[1]:
                self.result.append(persons[i])
                winner[0] = persons[i]
                winner[1] = self.votes[persons[i]]
            else:
                self.result.append(winner[0])

        # print("res", self.result)
    def q(self, t: int) -> int:
        ans = bisect.bisect_left(self.times, t)
        # print("index", ans)
        if t in self.times:
            return self.result[ans]
        else:
            return self.result[ans - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)