#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 1
# print('素数:')
# i = 2
# while(i < 100):
#     j = 2
#     while(j <= (i/j)):
#         if not(i%j): break
#         j = j + 1
#     if (j > i/j): print (i, ' ')
#     i = i + 1

# print("Good bye!")


# 2
num=[];
i=2
for i in range(2,100):
    j=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        num.append(i)
print(num)

