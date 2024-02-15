class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_count = defaultdict(list) # default dict dictionary created to store group elements with their indices

        grouped = [] # list to be returned after grouping

        # groups elements to their specific group to the dictionary
        for i, group in enumerate(groupSizes):
            group_count[group].append(i)

        # groups elements from the abpve dictionary based on their group size of their groups
        for group in group_count:
            temp_list = []
            for i in range(len(group_count[group])):
                if len(temp_list) == group:
                    grouped.append(temp_list)
                    temp_list = []

                if len(temp_list) <= group:
                    temp_list.append(group_count[group][i])

            if len(temp_list) <= group:
                grouped.append(temp_list)

        return grouped                

            