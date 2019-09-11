# import math
# #判断某个数是否为素数
# def primeNum(n):
#     flag=True
#     if(n>1):
#       sqrt_num=int(math.sqrt(n))
#       # print('sqrt result is',sqrt_num)
#       for i in range(2,sqrt_num+1):#加1的目的是因为range方法只会执行到sqrt_num减1的时候；
#           # print(i)
#           if(n%i==0):
#             #print('%d 不是素数'%n)
#             flag=False
#             break
#       else:
#           #print('%d 是素数'%n)
#           flag=True
#     else:
#       print("请重新输入数据，素数的计算最小从2开始")
#     return flag
# #判断某个范围内的素数的个数并进行数据输出
# def primeNums(n,m):
#     print('%d到%d范围内的素数有：'%(n,m))
#     for i in range(n,m+1):
#       # print('范围内输出的数据为：',i)
#       if(primeNum(i)==True):
#         print(i,end=" ")
#
# if __name__ == '__main__':
#     primeNums(2,20)
from random import choice
list=[1,2,3,4]

print(choice(list))
