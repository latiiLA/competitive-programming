class Solution:
    def frequencySort(self, s: str) -> str:
        charFreq = defaultdict(int)

        for char in s:
            charFreq[char] += 1

        freqMaxHeap = []

        for char, freq in charFreq.items():
            heappush(freqMaxHeap, (-freq, char))

        result = []
        while freqMaxHeap:
            freq, char = heappop(freqMaxHeap)
            for _ in range(-freq):
                result.append(char)

        return "".join(result)