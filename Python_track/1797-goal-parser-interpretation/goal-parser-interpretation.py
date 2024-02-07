class Solution:
    def interpret(self, command: str) -> str:
        result_of_command = ""

        for i in range(len(command)):
            if command[i] == "G":
                result_of_command += "G"
            elif command[i] == "(" and command[i+1] == ")":
                result_of_command += "o"
                i += 1
            elif command[i] == "(" and command[i+1] == "a":
                result_of_command += "al"
                i += 3
        
        return result_of_command

        # return command.replace('()','o').replace('(al)', 'al')