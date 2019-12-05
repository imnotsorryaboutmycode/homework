'homework #1 py'

'---task 1---'

var1 = 123
str1 = 'TEST OUTPUT'

print (var1)
print (str1)

name = input("Enter your name: ")
surname = input("Enter your surname: ")

age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print ("Hello "+name+" "+surname+" "+str(age)+" old and "+str(height)+" tall :)")


'---task 2---'
s = int(input("Enter seconds to convert: "))

m = s // 60
s = s % 60
h = m // 60
m = m % 60

print("%02i:%02i:%02i" % (h,m,s))

'---task 3---'
n = int(input("Enter some number: "))

one_n = str(n)
two_n = one_n+one_n
three_n = one_n+one_n+one_n

magic_n = int(one_n)+int(two_n)+int(three_n)

print ("Some MAGIC")
print (magic_n)

'---task 4---'
i = int(input("Enter any number: "))

max_d = 0
while i > 10:
    d = i % 10
    i //= 10
    if d > max_d:
        max_d = d
        
print("Max digit in your number is "+str(max_d))

'---task 5---'
revenue = float(input("Enter your revenue: "))
cost = float(input("Enter your cost: "))

if revenue > cost:
    print ("Your revenue > cost")
    profit = revenue/cost
    print ("Your profit is: "+str(profit))
    
    workers = int(input("Enter number of workers: "))
    revenue_per_worker = revenue/workers
    print ("Revenue per worker is "+str(revenue_per_worker))
    
elif revenue < cost:
    print ("Your revenue < cost")
else:
    print ("Your revenue = cost")
    
'---task 6---'
a_km = int(input('Enter a km: '))
b_km = int(input('Enter b km: '))

days = 1
while a_km <= b_km:
    days = days+1
    a_km = 1.1*a_km
print("Result day is: "+str(days))
