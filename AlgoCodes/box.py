#Program to print a Box
#Modified Line No. 1
import os
os.system('cls')
#
i = 0
j = 0
print("Start")
while i < 30:
    print("=", end = " ")
    i = i + 1
i = 0
print()
while j < 10:
    print("=", end = " ")
    while i < 28:
        print(" ", end = " ")
        i = i + 1
    print("=")
    i = 0
    j = j + 1
while i < 30:
    print("=", end = " ")
    i = i + 1
print()
print("End")