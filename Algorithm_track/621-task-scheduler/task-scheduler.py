class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []

        for task, value in count.items():
            heappush(heap, (-value, task))
        # print(heap)

        idle = 0

        while heap:
            current = []
            for i in range(n + 1):
                if heap:
                    value, task = heappop(heap)
                    if value != -1:
                        current.append((value + 1, task))
                elif current:
                    idle += n - i + 1
                    break

            while current:
                heappush(heap, current.pop())

        return len(tasks) + idle