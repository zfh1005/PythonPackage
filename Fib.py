import time

'''
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

'''    
def cache(function):
    caches = {}
    def _cache(*args, **kw):
        key = 'f' + str(args[0])
        if key in caches:
            return caches[key]
        result = function(*args, **kw)
        caches[key] = result
        print(caches[key])
        return caches[key]
    return _cache

@cache
def f(n):
    if n < 2:
        return n
    else:
        return f(n-2) + f(n-1)


  

if __name__ == "__main__":
    start = time.time()
    print (f(654))
    #print (fibonacci(40))
    print(time.time() - start)  