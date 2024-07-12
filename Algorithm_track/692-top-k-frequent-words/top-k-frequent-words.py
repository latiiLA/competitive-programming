class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency_of_words = defaultdict(int)
        # build frequency dictionary
        for word in words:
            frequency_of_words[word] += 1

        # print(frequency_of_words)

        # create heap from the dictionary values
        heap = []
        for word, freq in frequency_of_words.items():
            heappush(heap, (-freq, word))

        # print(heap)

        # populate your result with maximum k values from your heap
        result = []
        for _ in range(k):
            result.append(heappop(heap)[1])

        return result        