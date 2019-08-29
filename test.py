#斐波那契数列输出测试
def fibonacci(n):
    x, y,count= 0,1,0
    while count<n:
        print(x,end=" ")
        #x,y=y,x+y这种方式，等价于先进行等式右边的计算，然后再将结果赋值给等式的左边
        x, y = y, x+y
        count+=1

if __name__ == '__main__':
    fibonacci(10)




