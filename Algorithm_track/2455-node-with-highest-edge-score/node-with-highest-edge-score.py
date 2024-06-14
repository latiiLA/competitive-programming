class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        dictionary = defaultdict(int)
        max_score = float('-inf')
        max_node = -1
        
        # First register the value of the incoming edges/indegree for each nodes
        for i, edge in enumerate(edges):
            dictionary[edge] += i
        
        # Update the result if the maximum indegree encountered
        for node, score in dictionary.items():
            if max_score < score or (max_score == score and max_node > node):
                max_score = score
                max_node = node

        return max_node   