class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dictionary = collections.defaultdict(set)
        for a, b in roads:
            dictionary[a].add(b)
            dictionary[b].add(a)

        answer = 0
        for i in range(n):
            for j in range(i + 1, n):
                answer = max(answer, len(dictionary[i]) + len(dictionary[j]) - (i in dictionary[j]))
        return answer