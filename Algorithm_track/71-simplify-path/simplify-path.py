class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        print(path)
        path = path.split("/")
        print(path)

        # separate the directories into list. then remove unnecessary values. also move back if .. exits ans directories not empty
        for value in path:
            if stack and value == "..":
                stack.pop()
            elif value not in [".", "", ".."]:
                stack.append(value)
        
        return "/" + "/".join(stack)
