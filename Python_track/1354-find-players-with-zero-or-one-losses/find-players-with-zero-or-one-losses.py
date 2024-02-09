class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # dictionary to capture number of wins and loses of each players
        winner_dictionary = {}
        lose_one_dictionary = {}
        
        # tracks the winners and those only lost once
        winners = []
        lost_one = []

        # This loops through the matches list and counts the wins and loses
        for match in matches:
            if match[0] in winner_dictionary:
                winner_dictionary[match[0]] += 1
            else:
                winner_dictionary[match[0]] = 1

            if match[1] in lose_one_dictionary:
                lose_one_dictionary[match[1]] += 1
            else:
                lose_one_dictionary[match[1]] = 1

        # Loop through the winner dictionary finds the winners
        for i in winner_dictionary:
            if i not in lose_one_dictionary:
                winners.append(i)
        
        # Loop through the lose dictionary finds those who only lost once
        for i in lose_one_dictionary:
            if lose_one_dictionary[i] == 1:
                lost_one.append(i)

        return [sorted(winners), sorted(lost_one)]
        

