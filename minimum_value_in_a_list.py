
"""
Program: To find the index of the minimum value in the list
Programmer: Dr. Sajad Ahmad Rather
"""
#Sample_example = [400,45,20,33,22]

Num_of_elements = int(input('How many values you want in a list: '))

list = []
for temp_1 in range(Num_of_elements):
    number = int(input('Enter a number: '))
    list.append(number)
print(f'Your entered list is: {list}')

sorted_list = sorted(list)

#print(sorted_list)

for temp in range(len(list)):
    num = list[temp]
    q = sorted_list[0]
    if num == q:
        print(f'Index of the minimum value {num} is: {temp}')
