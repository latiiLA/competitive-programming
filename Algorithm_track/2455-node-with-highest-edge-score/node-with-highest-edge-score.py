class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        count = Counter(edges)
        dictionary = defaultdict(int)
        result = [0, float('-inf')]
        
        # First register the value of the incoming edges/indegree for each nodes
        # At the same time update the result value if the maximum indegree encountered
        for i, edge in enumerate(edges):
            dictionary[edge] += i
            if result[1] < dictionary[edge]:
                result[1] = dictionary[edge]
                result[0] = edge
            elif result[1] == dictionary[edge] and edge < result[0]:
                result[1] = dictionary[edge]
                result[0] = edge


        return result[0]        


