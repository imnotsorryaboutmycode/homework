--- task 1 ---

def customer_salary():
    try:
        time = float(input('Enter work hours: '))
        salary = int(input('Enter salary per hour: '))
        bonus = int(input('Enter bonus: '))
        res = time * salary + bonus
        return('Customer full salary with bonus is: '+str(res))
    except ValueError:
        return print('ValueError')
        
print(customer_salary())

--- task 2 ---

input_list = [1, 3, 3, 300, 1000, 5, 100, 2, 13]
output_list = [el for num, el in enumerate(input_list) if input_list[num - 1] < input_list[num]]
print('Input list is '+str(input_list))
print('Output list is '+str(output_list))

--- task 3 ---

print('Numbers from 20 to 240 multiple 20 or 21 -' + str([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]))

--- task 4 ---

input_list = [1, 2, 3, 4, 4, 4, 1, 100, 1, 5, 6, 7, 10]
ouput_list = [el for el in input_list if input_list.count(el) < 2]
print(ouput_list)

--- task 5 ---

from functools import reduce

def mult_all_even_nums(el_p, el):
    return el_p * el

print('List of even numbers: '+str([el for el in range(99, 1001) if el % 2 == 0]))
print('Result of multiplication all list numbers: '+str(reduce(mult_all_even_nums, [el for el in range(99, 1001) if el % 2 == 0])))

--- task 6 ---

'''A)'''
from itertools import count

for el in count(int(input('WARNING! It is endless cycle. Enter start number: '))):
    print(el)

'''B)'''
from itertools import cycle

my_list = ['SPAM', 123, 'ENDLESS CYCLE']
exit_flag = input('WARNING! It is endless cycle. Enter Q to exit or enter any symbol to start ')

if exit_flag.upper() == 'Q':
    exit
else:
    for el in cycle(my_list):
        print(el)
        
--- task 7 ---

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 16:
        print(i)
        x += 1
    else:
        break
