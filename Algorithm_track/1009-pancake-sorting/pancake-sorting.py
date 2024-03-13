class Solution:

    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        k = []

        for i in range(n):
            # find index of maximum element
            max_ = max(arr[:n - i])
            max_index = arr.index(max_) + 1

            # reverse the array until the maximum element including
            arr[:max_index] = reversed(arr[:max_index])
            k.append(max_index)

            # reverse the array until n - i
            arr[:n - i] = reversed(arr[:n - i])
            k.append(n - i)

        return k
