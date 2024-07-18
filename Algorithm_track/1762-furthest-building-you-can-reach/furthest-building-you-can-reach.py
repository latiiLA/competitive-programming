class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        index = 0

        # use ladder as until you run out of ladder
        # build heap using the height different when using ladder
        while index < n - 1:
            if not ladders:
                break
            if heights[index + 1] > heights[index]:
                heappush(heap, heights[index + 1] - heights[index])
                ladders -= 1
           
            index += 1

        print(heap, index)

        # Check if the minimum of the heap is less than less than the current height diff use ladder for this and brick for for difference on the heap
        # heap track ladder usage 
        while index < n - 1:
            diff = heights[index + 1] - heights[index]
            if diff <= 0:
                index += 1
                continue
            elif heap and heap[0] < diff and heap[0] <= bricks:
                bricks -= heappop(heap)
                heappush(heap, diff)
            elif bricks >= diff:
                bricks -= diff
            else:
                break
            index += 1
            # print(heap, bricks, diff)

        # print("outside", bricks, heap)
        
        return index
