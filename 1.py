# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (x and y and z and (not w))
#                 if f == 1:
#                     print(x, y, z, w)
# x w z y


# p = []
# for n in range(1, 1000):
#     b = bin(n)[2:]
#     s = sum(map(int, list(b)))
#     b = b + str(s % 2)
#     s = sum(map(int, list(b)))
#     b = b + str(s % 2)
#     r = int(b, 2)
#     if r > 123:
#         p.append(r)
#


# print(min(p))
# from itertools import product
#
# a = product("0123456789abcd", repeat=5)
# c = 0
#
# for i in a:
#     num = "".join(i)
#     if num[0] != "0":
#         if num.count("9") == 1:
#             for j in "bcd":
#                 num = num.replace(j, "*")
#             if num.count("*") <= 3:
#                 c += 1
# print(c)


# s = "9" * 81
#
# while "33333" in s or "999" in s:
#     if "33333" in s:
#         s = s.replace("33333", "99", 1)
#     if "999" in s:
#         s = s.replace("999", "3", 1)
# print(s)

# import sys
# sys.setrecursionlimit(10**6)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (n + 1) * f(n - 1)
#
# print((f(2024) + 3 * f(2023)) / f(2022))


# for a in range(1, 100000):
#     flag = True
#     for x in range(-500, 500):
#         f = (x % 33 == 0) <= ((not (x % a == 0)) <= (not (x % 242 == 0)))
#         if f == 0:
#             flag = False
#             break
#     if flag:
#         print(a)
