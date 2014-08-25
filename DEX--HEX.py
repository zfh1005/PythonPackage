
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

def hex2dec(string_num):
    return str(int(string_num.upper(), 16))

def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])



MMAC = 'ffffffabcdef'
print(MMAC)     
mac = hex2dec(MMAC)    
print(mac)
mac1 = int(mac) + 3
MAC = dec2hex(mac1)
print(MAC)
            