import os

def reseverFac(x):
    if x == 0:
        return 1
    else:
        return x * reseverFac(x - 1)
        
        
def onePascalFac(x):
    result = 1
    i = 2
    while i <= x:
        result *= i
        i += 1
    return result
    


def oneSICPFac(x, acc = 1):
    if(x > 1):
        return (oneSICPFac((x - 1), acc *x))
    else:
        return acc    

def oneCFac(x):
    result = i = 1;
    while(i <= x):
        result *= i;
        i += 1;
    return result
 
def onePythonFac(x):
    res = 1
    for i in range(2, x + 1):
        res *= i
    return res
         
def LPythonFac(x):
    return x > 1 and x * LPythonFac(x - 1) or 1     
 
def LLPythonFac(x):
    f = lambda x: x and x * f(x -1) or 1
    return f(x) 

'''
def ZPythonFac(x):
    f = lambda x: reduce(int.__mul__, range(2, x + 1), 1)
    return f(x) 
'''

def HPythonFac(x, acc = 1):
    if x:
        return HPythonFac(x.__sub__(1), acc.__mul__(x))
    return acc     
 
print(reseverFac(6)) 
print(onePascalFac(6)) 
print(oneSICPFac(6)) 
print(oneCFac(6)) 
print(onePythonFac(6)) 
print(LPythonFac(6)) 
print(LLPythonFac(6)) 
#print(ZPythonFac(6)) 
print(HPythonFac(6)) 
