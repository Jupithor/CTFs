from bisect import bisect

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes


def task1(primes):
    task1=0
    for i in range(len(primes)-1, -1, -2):
        p = primes[i]
        first=p
        last=p
        if p > 9:
            first=int(str(p)[0])
            last=int(str(p)[-1])
        task1+=first+last 
    return task1

def task2(primes):
    task2=0 
    for i in range(len(primes)-1, -1, -3):
        p=primes[i]
        b7=base7(p)
        for digit in str(b7):  
            task2 += int(digit)
    return task2

def task3(primes):
    task3=0
    for i in range(len(primes)-1, -1, -5):
        p1 = primes[i]
        p2 = primes[i - 1]
        mod = (p1 * p2) % 31337
        for digit in str(mod):
            if int(digit) % 2 == 1:
                task3+=1
    return task3
    

def calculate_task(N):
    primesall = sieve_of_eratosthenes(1000)  # Adjust the multiplier as needed
    primes=primesall[:bisect(primesall,N)]
    sum_result = 0
    sum_result+=task1(primes)    
    sum_result+=task2(primes)    
    sum_result+=task3(primes) 
    return sum_result   
        


def base7(num):
    result = ""
    while num > 0:
        result = str(num % 7) + result
        num //= 7
    return int(result)

# Test med eksempler
print("N =", 23, "  Svar =", calculate_task(23))
print("N =", 97, "  Svar =", calculate_task(97))
print("N =", 997, " Svar =", calculate_task(997))