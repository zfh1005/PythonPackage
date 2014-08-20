#statistics every number appear times in mathPI
import os

File_PATH = 'd:\\result.txt'

dicts = {'0':0,'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0 }

def StatisticsTime():
    #open file
    f = open(File_PATH, 'r')
    #readlines
    lines = f.readlines()
    for line in lines:
        st = str(line)
        #compare every character
        i = 0
        temp = '0'
        while i < 10:
            temp = str(int('0') + i)
            i += 1
            #print(st.count(temp))
            dicts[temp] = st.count(temp)

if __name__ == "__main__":
    StatisticsTime()
    print(dicts)


