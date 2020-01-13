x=input('请输入参数')
x= int(x)
y= input('请再次输入一个参数')
y= int(y)
z=x+y
print(z)

a=input('请输入任意半径大小')
a=int(a)
b=3.14*(a**2)
print('计算圆的面积是:%d'%b)

length = 4
width = 5
area = length*width
print('长方形面积%d'%area)

import math
a= int(input('输入a'))
b= int(input('输入b'))
c= int(input('输入c'))
deta = b**2-4*a*c 
if deta >= 0:
    x1 = (-b+math.sqrt(dela)/2*a)
    x2 = (-b-math.sqrt(dela)/2*a)
    print(x1,x2)
if deta == 0:
    x1 = x2 = (-b/2*a)
    print(x1,x2)
else:
    print('This isreal solution')
