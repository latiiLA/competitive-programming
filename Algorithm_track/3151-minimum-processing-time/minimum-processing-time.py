class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True) # reverse sort the tasks HINT of this question is helpful

        processorTime.sort() # Sort the processing time
        minimumProcessingTime = float('-inf') # store minimum processing time

        # Loop through the elements and find maximum of the processing time, divide tasks for each processor by 4 tasks
        i = 0
        while i < len(processorTime):
            j = i * 4
            minimumProcessingTime = max(minimumProcessingTime, max(tasks[j : j + 4]) + processorTime[i])
            print(tasks[i:i+4])            
            i += 1
        
        return minimumProcessingTime