# mensa bulletin Aug 2021 quadratic polynomials
#
# this program will find the three 4-digit numbers that are the sum of their digits to the 4th power
#
# no import math


for i in range(999, 9999):  # brute force check each 4 digit number to see whether it meets criteria
    first = i % 10
    second = (i // 10) % 10
    third = (i // 100) % 10
    fourth = (i // 1000) % 10
    if i == first**4 + second**4 + third**4 + fourth**4:
        print(i)