import sys

count = 1

def hanoi(n, A, B , C):
    global count
    if n == 1:
        print("{0}:  Move sheet {1} from {2} to {3}\n".format(count, n, A, C))
    else:
        hanoi(n-1, A, C, B)
        print("{0}:  Move sheet {1} from {2} to {3}\n".format(count, n, A, C))
        hanoi(n-1, B, A, C)


hanoi(3, 'A', 'B', 'C')
