if __name__ == '__main__':
    N = int(input())
    list_operation = []
    commands = []
    
    for i in range(N):
        commands.append(input())
        
    # print(commands)
        
    for command in commands:
        temp = []
        temp = command.split()
        
        if temp[0] == 'print':
            print(list_operation)
        elif temp[0] == 'insert':
            list_operation.insert(int(temp[1]), int(temp[2]))
        elif temp[0] == 'append':
            list_operation.append(int(temp[1]))
        elif temp[0] == 'remove':
            list_operation.remove(int(temp[1]))
        elif temp[0] == 'sort':
            list_operation.sort()
        elif temp[0] == 'pop':
            list_operation.pop()
        elif temp[0] == 'reverse':
            list_operation.reverse()
        elif temp[0] == 'print':
            print(list_operation)
            
        
