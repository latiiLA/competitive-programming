class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(score), len(score[0])
        kth_element = []

        # this separates the third element to new list
        for i in range(rows):
            kth_element.append(score[i][k])
        
        # reverse sort the separated element
        kth_element.sort(reverse = 1)

        # create empty list to be returned
        result = [[] for _ in range(rows)]

        # get the correct index from the kth separated and sorted list and insert each rows of the score to their correct positions
        for i in range(rows):
            result[kth_element.index(score[i][k])] = score[i]
        
        return result

       