#statistics every number appear times in mathPI
import os

File_PATH = 'd:\\result.txt'

dicts = {'0':0,'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '.':0 }

def StatisticsTime():
    #open file
    f = open(File_PATH, 'r')
    #readlines
    lines = f.readlines()
    for line in lines:
        st = str(line)
        #compare every character
        i = 0
        while i < 10:
            temp = str(int('0') + i)
            i += 1
            #print(st.count(temp))
            dicts[temp] = st.count(temp)
        dicts['.'] = st.count('.')
        
if __name__ == "__main__":
    StatisticsTime()
    print(dicts)
    i = 0 
    sum = 0
    std = str(dicts.values())
    temp = std.rsplit(',')
    print(temp)
    temp1 = temp
    while(i < len(temp)):
        if i == 0:
            temp1[i] = temp[i].split('[')[-1]
        elif i == len(temp) - 1:
            temp1[i] = temp[i].split(']')[0]
        else:
            temp1[i] = temp[i]    
        sum += int(temp1[i])
        i += 1
        
    print(temp1)
    print(sum)

