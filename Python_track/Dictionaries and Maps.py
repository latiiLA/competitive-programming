# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phonebook = {}

for i in range(n):
    key, value = input().split(" ")
    phonebook[key] = value
    
while True:
    try:
        name = input()
        
        if name in phonebook:
            print(f"{name}={phonebook[name]}")
        else:
            print("Not found")
    except EOFError:
        break
