#Write a Python program to print the following pattern. (15)
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15

def print_pattern(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

print_pattern(4)