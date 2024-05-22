#!/usr/bin/env python3

import ipdb 

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib = [0] * length
        fib[1] = 1
        for i in range(2, length):
            fib[i] = fib[i-1] + fib[i-2]
        print(fib)
