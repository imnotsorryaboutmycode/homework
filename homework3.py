--- task 1 ---

def division_func(*args):

    try:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
        res = numerator / denominator
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "denominator cant be zero"

    return res

print(division_func())

--- task 2 ---

def user_info_func (name, surname, birthday, city, email, telephone):
     return name+' '+surname+' '+birthday+' '+city+' '+email+' '+telephone
     
print(user_info_func(surname = 'Vasya', 
                     name = 'Petrov', 
                     birthday = '1995-12-12', 
                     city = 'Moscow', 
                     email = 'test@test.ru', 
                     telephone = '123'))
                     
--- task 3 ---

def my_func(x, y, z):
    sum_2_max = [x, y, z]
    min_num = min(sum_2_max)
    sum_2_max.remove(min_num)
    return(sum(sum_2_max))
    
print(my_func(100, -100, 200))

--- task 4 ---

def my_func(x, y):
    return 1 / x ** abs(y)

print(my_func(2, -3))

--- task 5 ---

def inf_sum_func ():
    sum_res = 0
    exit_flag = False
    while exit_flag == False:
        number = input('Enter string with numbers separated by "space" to sum values of them (or enter Q to exit): ').split()
        inc = 0
        for _ in range(len(number)):
            if number[_].upper() == 'Q':
                exit_flag = True
                break
            else:
                inc = inc + int(number[_])
        sum_res = sum_res + inc
        print(sum_res)

inf_sum_func()

--- task 6 ---

def int_func (*args):
    word = input("Enter string: ")
    return word.title()

print(int_func())
