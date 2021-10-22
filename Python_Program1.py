"""
For a given number, check whether the number is a prime number or not.

def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
n = int(input("Enter the Number:"))
check = prime(n)
if check:
    print("Your Number is Prime")
else:
    print("Your Number is Not Prime")


n = int(input("Enter the Number:"))
flag = False
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            flag = True
            break
if flag:
    print("The Number is Not Prime Number")
else:
    print("The Number is Prime Number")
_____________________________________________________________________________________________________
Ask the user to enter a number. Then find all the primes factors for the number.

n = int(input("Enter the Number:"))
l = []
l1 = 2
while n > 2:
    if n % l1 == 0:
        l.append(l1)
        n = n / l1
    else:
        l1 = l1 + 1
print(l)
__________________________________________________________________________________________
Ask the user to enter a number. Then find all the primes up to that number.



def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def all_primes(num):
    primes = []
    for n in range(2, num + 1):
        if is_prime(n) is True:
            primes.append(n)
    return primes


num = int(input("Enter upper limit: "))
primes = all_primes(num)
print(primes)
_______________________________________________________________________________________________
Find the smallest prime factor for the given number.



def get_smallest_factor(num):
    factor = 2
    while num % factor != 0:
        factor += 1
    return factor


num = int(input('Enter your number: '))

smallest_factor = get_smallest_factor(num)

print('The smallest prime factor is: ', smallest_factor)

n = int(input("Enter the Number:"))
l = []
l1 = 2
while n > 2:
    if n % l1 == 0:
        l.append(l1)
        n = n / l1
    else:
        l1 = l1 + 1
print(min(l))

"""
