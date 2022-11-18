
"""
Program: To find the index of the minimum value in a list
Programmer: Dr. Sajad Ahmad Rather
"""

def min_index(x):

    sorted_x = sorted(x)
    #print(sorted_x)

    for temp in range(len(x)):
        num = x[temp]
        q = sorted_x[0]
        if num == q:
            # print(f'Index of the minimum value {num} is: {temp}')
            return num, temp

def show_min_index(y):
    return f'Index of the minimum value is : {y}'



#Sample_example = [400,45,20,33,22]
#list = [400,45,20,33,22]

Num_of_elements = int(input('How many values you want in a list: '))

list = []
for temp_1 in range(Num_of_elements):
    number = int(input('Enter a number: '))
    list.append(number)
print(f'Your entered list is: {list}')

l = min_index(list)
print(l)

c = l [1]

m = show_min_index(c)
print(m)
