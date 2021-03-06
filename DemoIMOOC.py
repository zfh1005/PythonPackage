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
OutPut Is:
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
C --> B
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
B --> A
C --> A
C --> B
A --> B
C --> A
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C
'''

'''
请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
提示：range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]
'''
print ([x * ( x +1 ) for x in range(1, 100, 2)])
'''
OutPut Is:
[2, 12, 30, 56, 90, 132, 182, 240, 306, 380, 462, 552, 650, 756, 870, 992, 1122, 1260, 1406, 1560, 1722, 1892, 2070, 2256, 2450, 2652, 2862, 3080, 3306, 3540, 3782, 4032, 4290, 4556, 4830, 5112, 5402, 5700, 6006, 6320, 6642, 6972, 7310, 7656, 8010, 8372, 8742, 9120, 9506, 9900]
'''


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
OutPut Is:
['HELLO', 'WORLD']
'''


'''
利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
'''
print ([x*100 + y*10 + z for x in range(1, 10) for y in range(0, 10) for z in range(0, 10) if x == z])
'''
OutPut Is:
[101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]
'''
