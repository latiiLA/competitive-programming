class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dictionary = Counter(nums)
        result = []

        # create initial dictionary take each elements while decreasing their count
        while len(dictionary) > 0:
            temp_list = []
            for num in list(dictionary.keys()):
                temp_list.append(num)
                dictionary[num] -= 1
                if dictionary[num] == 0:
                    del dictionary[num]
            result.append(temp_list)

        return result

        # This is amazing approach i have found after from the submissions
        # res = []
        # count = defaultdict(int)
        # for n in nums:
        #     row = count[n]
        #     if len(res) == row:
        #         res.append([])
            
        #     res[row].append(n)
        #     count[n] += 1
        #     print(res)
        
        # return res
