class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        print(v1, v2)

        for i in range(min(len(v1), len(v2))):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        if len(v1) > len(v2):
            if sum(v1[len(v2):]) > 0:
                return 1
        elif len(v1) < len(v2):
            if sum(v2[len(v1):]) > 0:
                return -1  


        return 0
