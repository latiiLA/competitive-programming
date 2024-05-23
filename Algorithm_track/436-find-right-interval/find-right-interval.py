class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Binary Search Approach
        # store the index of elements before sorting only the first element is enough
        dictionary = {}
        for index, interval in enumerate(intervals):
            dictionary[interval[0]] = index
        
        # sort the intervals only the second element is enough
        sorted_intervals = sorted(intervals, key=lambda x:x[0])

        result = [-1] * len(intervals) # initialize the return array

        # use binary serach over sorted array to find the value of the intervals
        # search the index from the previously stored index and update the result list
        for i, interval in enumerate(intervals):
            index = bisect_left(sorted_intervals, [interval[1], float('-inf')])

            if index != len(intervals):
                result[i] = dictionary[sorted_intervals[index][0]]

        return result