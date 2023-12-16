#!/bin/python
import sys
import socket
from bisect import bisect
import time

host="77.231.0.30"
port=3119
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def nc(host,port):
    try :
        client.connect((host,port))
        print("connected")
        next=client.recv(1024)
        data=b''
        while (next!=b''):
            data=next
            msg=data.decode('ascii')
            print(msg)
            n=msg.splitlines()[2]
            print("challenge:", n)
            result=calculate_task(int(n))
            print("asw:", result)
            client.send(str(result).encode('utf-8'))
            next=client.recv(1024)
            
    except ConnectionRefusedError:
        print("Connection closed")


#udregning af primtal optil limit
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
    result=0
    for i in range(len(primes)-1,-1,-2):
       result+=addedprimesall[i] 
    return result

def task2(primes):
    result=0 
    for i in range(len(primes)-1,-1,-3):
        result+=sumprimesall[i]
    return result

def task3(primes):
    result=0
    for i in range(len(primes)-1,-1,-5):
        mod = (primes[i]* primes[i-1])% 31337
        for digit in str(mod):
            if int(digit) % 2 == 1:
                result+=1
    return result
    

def calculate_task(N):
    sum_result=0
    primes=primesall[:bisect(primesall,N)]
    n7=base7(N)
    primes7=primes7all[:bisect(primes7all,n7)]
    sum_result+=task1(primes)
    sum_result+=task2(primes7)
    sum_result+=task3(primes)
    return sum_result   

#convert base10 til base7
def base7(num):
    if num == 0:
        return 0
    res=''
    while num > 0:
        num,re=divmod(num,7)
        res=str(re)+res
    return int(res)
 
#pre-calc primes op til p
p=100000000
start=time.perf_counter()
print("calculating primes")
primesall = sieve_of_eratosthenes(p)  
#convert alle primes til base7
primes7all=[]
for i in range(0,len(primesall)):
    primes7all.append(base7(primesall[i]))
end=time.perf_counter()
print(f"done with primes, took: {end-start:0.4f}")

#pre-calc task1
start=time.perf_counter()
print("calculating adding primes")
addedprimesall=[]
for prime in primesall:
    if prime > 9:
        first=int(str(prime)[0])
        last=prime%10
    else:
        first=prime
        last=prime
    addedprimesall.append(first+last)
end=time.perf_counter()
print(f"done with adding primes, took: {end-start:0.4f}")

#pre-calc task2
start=time.perf_counter()
print("calculating sum primes")
sumprimesall=[]
for prime in primes7all:
    sumprimesall.append(sum([int(digit) for digit in str(prime)]))
end=time.perf_counter()
print(f"done with adding primes, took: {end-start:0.4f}")

#Test eksempler
print("N =", 23, "  Svar =", calculate_task(23))
print("N =", 97, "  Svar =", calculate_task(97))
print("N =", 997, "  Svar =", calculate_task(997))
print("N =", 549979, "  Svar =", calculate_task(549979))

#start=time.perf_counter()
#print("calculating task")
#print("N =", 89392837, "  Svar =", calculate_task(89392837))
#end=time.perf_counter()
#print(f"done with task, took: {end-start:0.4f}")
#nc(host,port)