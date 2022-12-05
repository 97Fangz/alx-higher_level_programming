#!/usr/bin/python3
def print_last_digit(num):
    if num < 0:
        num = -num
    last = num % 10
    print(last, end='')
    return last
