#User function Template for python3
from collections import Counter

def isSubset( a1, a2, n, m):
    count = dict(Counter(a1))
    
    for a in a2:
        if a in count:
            if count[a] == 0:
                return "No"
            else:
                count[a] -= 1
        else:
            return "No"
    
    return "Yes"
