MAX_day = 20

Fib{MAX_day} = {0}
for i in range(0, MAX_day):
    if i == 0:
        Fib[0] = 0
    elif i == 1:
        Fib[1] = 1
    else:
        Fib[i] = Fib[i-1] + Fib[i-2]
    print(Fib[i], end=',')
