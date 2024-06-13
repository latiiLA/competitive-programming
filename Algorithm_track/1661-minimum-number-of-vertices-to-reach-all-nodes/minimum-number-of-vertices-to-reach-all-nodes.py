class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        list_j = set()
        answer = set()

        for i, j in edges:
            if j not in list_j:
                list_j.add(j)

        for i, j in edges:
            if i not in list_j and i not in answer:
                answer.add(i)

        return answer

        