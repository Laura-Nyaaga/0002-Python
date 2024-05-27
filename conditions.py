def print_numbers(n):
    numbers = range(n)
    for number in numbers: 
        print(number)
print_numbers(10)

def print_odd_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number%2 != 0:
           print (number)
print_odd_numbers(100)

def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
           print(number)
print_even_numbers(20)

def check_odd_even(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is not even")
check_odd_even(50)

def check_divisibilty(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
            print(f"{number} is divisible by 2")
        elif number%3 == 0:
            print(f"{number} is divisible by 3")
        elif number%5 == 0:
            print(f"{number} is divisible by 5")
        else:
            print(f"{number}is not divisible by 2,3,5")
check_divisibilty(100)            

def fizzbuzz(n):
    num = range(n)
    for number in num:
        if number%3 == 0:
            print('fizz')
        elif number%5 == 0:
            print("buzz")
        else:
            print("fizzbuzz")
fizzbuzz(100)

def countdown(n):
    while n>0:
        print(n)
        n-=1
countdown(10)        

def countdown_to_five(n):
    while n > 0:
        print(n)
        if n==5:
            break
        n-=1
countdown_to_five(40)

def divisible_by_seven(n):
    x = 0
    while x <= n:
        x += 1
        if x%7!=0:
            continue
        print(f"{x} is divisible by seven")
divisible_by_seven(30)        

def oddd_numbers():
    n = 0
    while n<100:
        n+=1
        if n % 2 == 0:
            continue
    print(f"{n} is odd number")
