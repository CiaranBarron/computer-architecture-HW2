import math
import multiprocessing
import time

def my_func(x):  
    s = math.sqrt(x)  
    return s

def my_func_verbose(x):
    s = math.sqrt(x)
    print("Task", multiprocessing.current_process(), x, s)
    return s

def check_prime(num, *args):
    prnt=False
    if args:
        if "print" in args:
            prnt=True
    
    if prnt:
        print("ok")
    t1 = time.time()
    res = False
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                if prnt:
                    print(num,"is not a prime number")
                    print(i,"times",num//i,"is",num)
                    print("Time:", int(time.time()-t1))
                break
        else:
            if prnt:
                print(num,"is a prime number")
                print("Time:", time.time()-t1) 
            res = True
            # if input number is less than
            # or equal to 1, it is not prime
    return res, (time.time()-t1)