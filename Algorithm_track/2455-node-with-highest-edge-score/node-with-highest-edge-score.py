class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        count = Counter(edges)
        dictionary = defaultdict(int)
        
        # First register the value of the incoming edges/indegree for each nodes
        for i, edge in enumerate(edges):
            dictionary[edge] += i

        result = [0, float('-inf')]

        # Loop through the dictionary and find the one that has the maximum indegree if they are equal the smalles one
        for num in dictionary:
            if result[1] < dictionary[num]:
                result[1] = dictionary[num]
                result[0] = num
            elif result[1] == dictionary[num] and num < result[0]:
                result[1] = dictionary[num]
                result[0] = num

        return result[0]        


