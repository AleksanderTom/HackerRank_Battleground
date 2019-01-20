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