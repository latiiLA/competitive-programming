n = int(input())

maximum_num_passenger = []
max_current_passenger = 0

for i in range(n):
    a, b = input().split()
    max_current_passenger = max_current_passenger + int(b) - int(a)
    maximum_num_passenger.append(max_current_passenger)
    # print(maximum_num_passenger)
    
for i in maximum_num_passenger:
    max_current_passenger = max(max_current_passenger, i)

print(max_current_passenger) 
