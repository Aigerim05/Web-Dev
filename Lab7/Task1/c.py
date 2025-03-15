######## for loop

# Task A

# a = int(input())
# b = int(input())

# if a % 2 != 0:
#     a += 1

# for i in range(a, b + 1, 2):
#     print(i, end=" ")


# Task B
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# for i in range(a, b + 1):
#     if i % d == c: 
#         print(i, end=" ")


# Task C
# import math

# a = int(input())
# b = int(input())

# start = math.ceil(math.sqrt(a))
# end = math.floor(math.sqrt(b))

# for i in range(start, end + 1):
#     print(i * i, end=" ")


# Task D
# x = input()
# d = input()
# count = 0

# for digit in x:
#     if digit == d:
#         count += 1

# print(count)


# Task E
# x = input()
# sum_digits = 0

# for digit in x:
#     sum_digits += int(digit)

# print(sum_digits)


# Task F
# x = input()
# result = ""

# for digit in reversed(x):
#     result += digit

# print(int(result))


# Task G
# x = int(input())

# for i in range(2, x + 1):
#     if x % i == 0:
#         print(i)
#         break


# Task H
# x = int(input())

# for i in range(1, x + 1):
#     if x % i == 0:
#         print(i, end=" ")

# Task I
# import math

# x = int(input())
# count = 0

# for i in range(1, int(math.sqrt(x)) + 1):
#     if x % i == 0:
#         count += 2 if i != x // i else 1

# print(count)


# Task J
# total = 0

# for _ in range(100):
#     total += int(input())

# print(total)


# Task K
# n = int(input())
# total = 0

# for _ in range(n):
#     total += int(input())

# print(total)


# Task L
# binary_number = input()
# decimal_number = 0
# power = 1  

# for digit in reversed(binary_number):
#     decimal_number += int(digit) * power
#     power *= 2

# print(decimal_number)

# Task M
# n = int(input())
# count = 0

# for _ in range(n):
#     if int(input()) == 0:
#         count += 1

# print(count)




######## while loop

# Task A
# n = int(input())

# i = 1
# while i * i <= n:
#     print(i * i)
#     i += 1



# Task B

# n = int(input())

# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break


# Task C
# n = int(input())
# power = 1

# while power <= n:
#     print(power, end=" ")
#     power *= 2



# Task D
# n = int(input())

# while n > 1:
#     if n % 2 != 0:
#         print("NO")
#         break
#     n //= 2
# else:
#     print("YES")



# Task E
n = int(input())
k = 0
power = 1

while power < n:
    power *= 2
    k += 1

print(k)


