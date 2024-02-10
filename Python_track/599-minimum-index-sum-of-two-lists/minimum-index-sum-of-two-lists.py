class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        commons ={} # dictionary to find common elements of the list
        least_index_commons = [] # list to append list index common elements
        minimum_length = len(list1) + len(list2) # to find minimum index length of the strings

        # Finds commons elements of the list as well as the minimum list length
        for i in range(len(list1)):
            if list1[i] in list2:
                commons[list1[i]] = i + list2.index(list1[i])
                minimum_length = min(minimum_length, i + list2.index(list1[i]))

        # Finds minimum list length elements of the lists from common elements dictionary 
        for common in commons:
            if commons[common] == minimum_length:
                least_index_commons.append(common)
            
        return least_index_commons


