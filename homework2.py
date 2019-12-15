--- task 1 ---

my_random_list = [{1: 'A', 2:'B'}, False, 'Max', 123, None, 13.13, (1,2)]

for i in my_random_list:
    print(type(i))
    
--- task 2 ---

str_list = input('Enter int list separated by a space: ')
my_list = str_list.split()
j = 0

for i in range(int(len(my_list)/2)):
    my_list[j], my_list[j + 1] = my_list [j + 1], my_list[j]
    j += 2
print(my_list)

--- task 3 ---

month = int(input("Enter month number "))
seasons_list = ['winter', 'spring', 'summer', 'spring']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'spring'}

if month == 12 or month == 1 or month == 2:
    print(seasons_dict.get(1)+' from dict')
    print(seasons_list[0]+' from list')
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2)+' from dict')
    print(seasons_list[1]+' from list')
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3)+' from dict')
    print(seasons_list[2]+' from list')
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4)+' from dict')
    print(seasons_list[3]+' from list')
else:
    print("Error, not a valid month")
    
--- task 4 ---

my_str = input("Enter string ")
my_word = []
rn = 0
for i in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    rn += 1
    print(str(rn)+' '+str(my_word[i] [0:10]))
    
--- task 5 ---

my_list = [7, 5, 3, 3, 2]
print(my_list)
new_num = int(input("Enter your number: "))

for i in range(len(my_list)):
    if my_list[-1] > new_num:
        my_list.append(new_num)
        break
    elif my_list[0] < new_num:
        my_list.insert(0, new_num)
        break
    elif my_list[i] == new_num:
        my_list.insert(i + 1, new_num)
        break
    elif my_list[i] > new_num and my_list[i + 1] < new_num:
        my_list.insert(i + 1, new_num)
        break

print(my_list)

--- task 6 ---

goods = []

while input("Add new product yes/no? ") == 'yes':
    prod_num = int(input("Enter new product number: "))
    my_dict = dict({'Product name': input("Enter product name: "), 
                    'Price': input("Enter product price: "),
                    'Count': input("Enter product count: "), 
                    'Units': input("Enter units name: ")})
    goods.append(tuple([prod_num, my_dict]))
print(goods)
''' как сделать для аналитики не знаю...'''
