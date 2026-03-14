import math as m
import random as rand

def finding_prime(number):
    num = abs(number)
    if num < 4: return True
    for x in range(2,num):
        if num%x == 0:
            return False
    return True

def finding_prime_sqrt(number):
    num = abs(number)
    if num <4: return True
    for x in range(2, int(m.sqrt(num)) + 1):
        if number % x == 0:
            return False
    return True

def finding_prime_fermat(number):
    if number <= 102:
        for a in range(2, number):
            if pow(a, number-1, number) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = rand.randint(2, number - 1)
            if pow(a, number-1, number) != 1:
                return False
        return True
    
def find():
    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number2: "))    
    prime1 = finding_prime(number1)
    print("prime1: ",prime1)
    prime2 = finding_prime(number2)
    print("prime2: ",prime2)
    prime3 = finding_prime_sqrt(number1)
    print("prime3: ",prime3)
    prime4 = finding_prime_sqrt(number2)
    print("prime4: ",prime4)
    prime5 = finding_prime_fermat(number1)
    print("prime5: ", prime5)
    prime6 = finding_prime_fermat(number2)
    print("prime6: ", prime6)
if __name__ == "__main__":
    find()