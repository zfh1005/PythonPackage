for i in range(1, 10):
    for j in  range(1, 10):
        if j <= i:
            print("%2d "%(i*j), end=" ")
    print("\r\n")
