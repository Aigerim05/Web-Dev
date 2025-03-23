# Task A
# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(0, n, 2):  
#     print(arr[i], end=" ")


# Task B
# n = int(input())
# arr = list(map(int, input().split()))

# for x in arr:
#     if x % 2 == 0:
#         print(x, end=" ")


# Task C
# n = int(input())
# arr = list(map(int, input().split()))

# count = 0
# for x in arr:
#     if x > 0:
#         count += 1

# print(count)


# Task D
# n = int(input())
# arr = list(map(int, input().split()))

# count = 0
# for i in range(1, n):
#     if arr[i] > arr[i - 1]:
#         count += 1

# print(count)

# Task E
# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(1, n):
#     if arr[i] * arr[i - 1] > 0:
#         print("YES")
#         break
# else:
#     print("NO")


# Task F

# n = int(input())
# arr = list(map(int, input().split()))
# count = 0

# for i in range(1, n - 1):
#     if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
#         count += 1

# print(count)


# Task G
# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(n // 2):
#     arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

# for num in arr:
#     print(num, end=" ")


num = input()
sum = 0
a = list(map(int, num.split()))
for i in a:
    sum += i


