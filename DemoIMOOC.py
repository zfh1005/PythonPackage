'''
汉诺塔 (http://baike.baidu.com/view/191666.htm) 的移动也可以看做是递归函数。
我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：
如果a只有一个圆盘，可以直接移动到c；
如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。
请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：
move(n, a, b, c)
例如，输入 move(2, 'A', 'B', 'C')，打印出：
A --> B
A --> C
B --> C
'''
def move(n, a, b, c):
    if n==1:
        print (a, '-->', c)
    else:
        move(n-1,a,c,b)#将前n-1个盘子从x移动到y上
        print (a, '-->', c)#将最底下的最后一个盘子从x移动到z上
        move(n-1,b,a,c)#将y上的n-1个盘子移动到z上
        
move(10, 'A', 'B', 'C')


'''
请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
提示：range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]
'''
print ([x * ( x +1 ) for x in range(1, 100, 2)])


'''
请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
提示：
1. isinstance(x, str) 可以判断变量 x 是否是字符串；
2. 字符串的 upper() 方法可以返回大写的字母。
'''
def toUppers(L):
    return [str.upper(x) for x in L if  isinstance(x, str)]

print (toUppers(['Hello', 'world', 101]))


'''
利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
'''
print ([x*100 + y*10 + z for x in range(1, 10) for y in range(0, 10) for z in range(0, 10) if x == z])

