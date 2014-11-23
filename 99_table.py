for i in range(1, 10):
    for j in  range(1, 10):
        if j <= i:
            print("%-2dx%2d = %-2d "%(j, i, i*j), end=" ")
    print("\r\n") 
