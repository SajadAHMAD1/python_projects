
"""
Program: To find the LCM (Least Common Multiple) of two numbers
Programmer: Dr. Sajad Ahmad Rather
"""
#a = 15
#b = 87

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

e = []
f = []

i = 2
while a > 1:
    if a % i == 0:
        e.append(i)
        a = a / i
        i = i - 1
    i = i + 1
print(f'Prime Factors of a: {e}')

j = 2
while b > 1:
    if b % j == 0:
        f.append(j)
        b = b / j
        j = j - 1
    j = j + 1
print(f'Prime Factors of a: {f}')

# composite_numbers = []
# prime_numbers =[]
# for x in range(2,1000):
#     if (x%x == 0) and (x%1 == 0):
#         for y in range(2,1000):
#             if (y!=x) and (x%y == 0):   # Composite Numbers: (y!=x) and (x%y == 0)
#                 composite_numbers.append(x)
# actual_com_num = list(set(composite_numbers))
# print(f'Composite numbers: {actual_com_num}')
# for z in range(2,1000):
#     if z not in actual_com_num:
#         prime_numbers.append(z)
# print(f'Prime numbers: {prime_numbers}')
#
# c = []
# d = []
# for p in range(len(prime_numbers)):
#     l = prime_numbers[p]
#     #print(l)
#     if a%l == 0:
#         c.append(l)
#     if b%l == 0:
#          d.append(l)
# print(f'Prime factors of a: {c}')
# print(f'Prime factors of b: {d}')
#
# #
# print('After checking (For a)')
# ### Multiplication of prime factors (Number 1)
# temp = 1
# for p1 in range(len(c)):
#     temp = temp * c[p1]
# print(f'Product: {temp}')
# ### If multiplication is equal to the given number (Number 1)
# e = []
# if temp == a:
#     print(f'Modified Prime factors of a: {c}')
#     e.append(c)
#     print(f'e =={c}')
#
# ### If multiplication is not equal to the given number(Number 1)
# #e = []
# elif temp != a:
#     for p2 in range(len(c)):
#         temp_1 = c[p2]
#         print(temp_1)
#         if a%temp_1 == 0:
#              e.append(temp_1)
#     print(e)
#     #print(len(e))
#     p3 = 0
#     while p3 < len(e):
#             num = c[p3]
#             temp = temp * num
#             if temp == a:
#                 e.append(num)
#                 break
#             elif temp != a:
#                 e.append(num)
#                 p3 = p3 + 1
#                 #continue
#            # p3 = p3 + 1
# print(f'Modified Product_a: {temp}')
# print(print(f'Modified Prime factors of a: {e}'))



print('\n')
#print('<<<<<LCM Calculation>>>>>')
#print(prime_numbers)
sorted_e = sorted(e)
#print(f"sorted_e: {sorted_e}")
e1 = list(set(e))
#print(f'e1== {e1}')
times_a = []
elem_a = []
ll = 1
if sorted_e == e1:
     #print('Prime factors are single time')
     for nep in range(len(sorted_e)):
         times_a.append(ll)
     #print(f'a: Times list: {times_a}')
     elem_a = sorted_e
     #print(f'a: Element list: {elem_a}')
     for temp_a in range(len(times_a)):
          print(f'a: {elem_a[temp_a]} is repeated {times_a[temp_a]} time')

if sorted_e!= e1:
    for num_a in range(len(sorted_e)):
        lim_a = sorted_e[num_a]
        c_a = sorted_e.count(lim_a)
        if lim_a not in elem_a:
            times_a.append(c_a)
            elem_a.append(lim_a)
    #print(f'a: Times list: {times_a}')
    #print(f'a: Element list: {elem_a}')
    for temp_a in range(len(times_a)):
        print(f'a: {elem_a[temp_a]} is repeated {times_a[temp_a]} time')

#print('After checking (For b)')
# ### Multiplication of prime factors (Number 2)
# temp2 = 1
# for p1 in range(len(d)):
#     temp2 = temp2 * d[p1]
# print(f'Product: {temp2}')
#
# ### If multiplication is equal to the given number (Number 2)
# f = []
# if temp2 == b:
#     print(f'Modified Prime factors of b: {d}')
#     f.append(d)
#     print(f'e =={d}')
#
# ### If multiplication is not equal to the given number(Number 2)
#
# elif temp2 != b:
#     for p2 in range(len(d)):
#         temp_3 = d[p2]
#         #print(temp_3)
#         if b%temp_3 == 0:
#              f.append(temp_3)
#     print(f'f == : {f}')
#     p4 = 0
#     while p4 < len(f):
#         num = d[p4]
#         temp2 = temp2 * num
#         if temp2 == b:
#             f.append(num)
#             break
#         elif temp2 != b:
#             f.append(num)
#             p4 = p4 + 1
#
#         #     continue
#         # p4 = p4 + 1
# print(f'Modified Product_b: {temp2}')
# print(f'Modified Prime factors of b: {f}')

#print('\n')
#print('<<<<<LCM Calculation>>>>>')
#print(prime_numbers)
# lm1 = sorted(c)
# #print(lm1)
sorted_f = sorted(f)
#print(f"sorted_f: {sorted_f}")

f1 = list(set(f))
# print(f1)
times = []
elem = []
mm = 1
if sorted_f == f1:
     #print('Prime factors are single time')
     for nep in range(len(sorted_f)):
         times.append(mm)
     #print(f'a: Times list: {times}')
     elem = sorted_f
     #print(f'a: Element list: {elem}')
     for temp_a in range(len(times)):
          print(f'a: {elem[temp_a]} is repeated {times[temp_a]} time')



if sorted_f!= f1:
    for num in range(len(sorted_f)):
        lim = sorted_f[num]
        c = sorted_f.count(lim)
        if lim not in elem:
            times.append(c)
            elem.append(lim)
    #print(f'b: Times list: {times}')
    #print(f'b: Element list: {elem}')
    for temp in range(len(times)):
        print(f'b: {elem[temp]} is repeated {times[temp]} time')

# Comparision of two matrices for equality

print('\n')
#print(f'a: Times list: {times_a}')
#print(f'a: Element list: {elem_a}')

#print(f'b: Times list: {times}')
#print(f'b: Element list: {elem}')

k = []
for i in range(len(elem_a)):
    i1 = elem_a[i]
    for j in range(len(elem)):
        i2 = elem[j]
        if i1 == i2:
            i3 = i2
            k.append(i3)
#print(f'Comparison and equality elements: {k}')


# For a
k1 = []
for num_aaa in range(len(k)):
    lim_aaa = k[num_aaa]
    if lim_aaa in sorted_e:
         #print(lim_aaa)
         c_aa = sorted_e.count(lim_aaa)
         k1.append(c_aa)
#print(f'a: Repeated by: {k1}')

# For b

k2 = []
for temp_b in range(len(k)):
    lim_aa = k[temp_b]
    if lim_aa in sorted_f:
         #print(lim_aaa)
         c_aaa = sorted_f.count(lim_aa)
         k2.append(c_aaa)
#print(f'b: Repeated by: {k2}')

# Find greater value for similar elements in two lists
k3 = []
for temp_2 in range(len(k1)):
    temp_3 = k1[temp_2]
    temp_4 = k2[temp_2]
    if temp_3 >temp_4:
        c_4 = temp_3
        k3.append(c_4)
    elif temp_3 < temp_4:
        c_4 = temp_4
        k3.append(c_4)
    elif (temp_3 > 1) and (temp_4 > 1) and (temp_3 == temp_4):
        c_4 = temp_4
        k3.append(c_4)
    elif (temp_3 == 1) and (temp_4 == 1):
        c_4 = temp_4
        k3.append(c_4)
#print(f'a,b: Greater value:{k3}')


# Product of similar elements and their 'repeated greater value' in the two lists
temp_8 = 1
for temp_5 in range(len(k)):
    temp_6 = k[temp_5]
    #print(temp_6)
    temp_7 = k3[temp_5]
    #print(temp_7)
    temp_8 = temp_8 * (temp_6 ** temp_7)
#print(f'Product of Similar Elements: {temp_8}')

#Remove similar elements in 'a'
for temp_9 in range(len(k)):
    temp_10 = k[temp_9]
    while temp_10 in sorted_e:
        sorted_e.remove(temp_10)
#print(sorted_e)

# Remove similar elements in 'b'
for temp_11 in range(len(k)):
    temp_12 = k[temp_11]
    while temp_12 in sorted_f:
        sorted_f.remove(temp_12)
#print(sorted_f)

## Product of remaining elements in a
temp_15 = 1
for temp_13 in range(len(sorted_e)):
    temp_14 = sorted_e[temp_13]
    temp_15 = temp_15 * ( temp_14 ** 1)
#print(f'Product of remaining elements in a: {temp_15}')
##Product of remaining elements in b
temp_18 = 1
for temp_16 in range(len(sorted_f)):
    temp_17 = sorted_f[temp_16]
    temp_18 = temp_18 * (temp_17 ** 1)
#print(f'Product of remaining elements in b: {temp_18}')
#
print('>>>>>LCM<<<<<')
lcm = temp_8 * temp_15 * temp_18
print(f'The value of LCM is: {lcm}')
