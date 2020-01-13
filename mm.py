def html(a,b,c):
    import math
    if a+b<=c or c+b<=a or a+c<=b:
        print('三边不能构成三角形')
        return
    else:
        x = (a+b+c)/2
        s = math.sqrt(x*(x-a)*(x-b)*(x-c))
        return s
    
