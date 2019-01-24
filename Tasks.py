# task1

# # inp = "07:05:45PM"
# # inp = "12:05:45AM"
# # inp = "12:05:45PM"
# inp = "06:05:45AM"
#
# if inp[:2] == "12" and inp[-2:] == "AM":
#     result = "00" + inp[2:-2]
#     print(result)
#
# if int(inp[:2]) < 12 and inp[-2:] == "AM":
#     result = inp[:-2]
#     print(result)
#
# elif inp[:2] == "12" and inp[-2:] == "PM":
#     result = inp[:-2]
#     print(result)
# else:
#     result = str(int(inp[:2]) + 12) + inp[2:-2]
#     print(result)


# # task2
#
# a = [73, 67, 38, 33]
#
# for i in a:
#     modulo = i % 5
#     modified = i - modulo + 5
#
#     if modified - i < 3 and i >= 38:
#         print(modified)
#     elif modified - i > 2 and i >= 38:
#         print(i)
#     else:
#         print(i)


# # task 3
# x1 = 21
# v1 = 6
# x2 = 47
# v2 = 3
#
#
# def kangaroo(x1, v1, x2, v2):
#     pos_x1 = x1
#     pos_x2 = x2
#     counter = 0
#     print(counter, pos_x1, pos_x2)
#     for i in range(0, 100):
#         counter += 1
#         pos_x1 += v1
#         pos_x2 += v2
#         print(counter, pos_x1, pos_x2)
#
#
# kangaroo(x1, v1, x2, v2)
#
# # solution
#
# # !/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# # Complete the kangaroo function below.
# def kangaroo(x1, v1, x2, v2):
#     # x1, x2 starting positions
#     # v1, v2 distance that kangaroos jump
#
#     if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
#         return "YES"
#     else:
#         return "NO"
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     x1V1X2V2 = input().split()
#
#     x1 = int(x1V1X2V2[0])
#
#     v1 = int(x1V1X2V2[1])
#
#     x2 = int(x1V1X2V2[2])
#
#     v2 = int(x1V1X2V2[3])
#
#     result = kangaroo(x1, v1, x2, v2)
#
#     fptr.write(result + '\n')
#
#     fptr.close()



# sock merchant failing case:

list = [44, 55, 11, 15, 4, 72, 26, 91, 80, 14, 43, 78, 70, 75, 36, 83, 78, 91, 17, 17, 54, 65, 60, 21, 58, 98, 87, 45, 75, 97, 81, 18, 51, 43, 84, 54, 66, 10, 44, 45, 23, 38, 22, 44, 65, 9, 78, 42, 100, 94, 58, 5, 11, 69, 26, 20, 19, 64, 64, 93, 60, 96, 10, 10, 39, 94, 15, 4, 3, 10, 1, 77, 48, 74, 20, 12, 83, 97, 5, 82, 43, 15, 86, 5, 35, 63, 24, 53, 27, 87, 45, 38, 34, 7, 48, 24, 100, 14, 80, 54]


def sockMerchant(ar):
    ar.sort()
    pairs = 0

    while len(ar) != 1:
        try:
            if ar[0] == ar[1]:
                pairs += 1
                ar.pop(0)
                ar.pop(0)
            else:
                ar.pop(0)
        except IndexError:
            return pairs

    return pairs

print(sockMerchant(list))

