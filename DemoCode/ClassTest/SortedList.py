class SortedList:
    def __init__(self, sequence = None, key = None):
        _identity = lambda x : x
        self.__key = key or _identity
        assert hasattr(self.__key, "__call__")
        if sequence is None:
            self.__list = []
        elif(isinstance(sequence, SortedList) and sequence.key == self.__key):
            self.__list = sequence.__list[:]
        else:
            self.__list = sorted(list(sequence), key = self.__key)

    

    @property
    def key(self):
        return self.__key

    '''
    find the value's index in list
    used two trees serach.
    '''
    def __bisect_left(self, value):
        key = self.__key(value)
        left, right = 0, len(self.__list)
        while left < right:
            middle = (left + right) // 2
            if self.__key(self.__list[middle]) < key:
                left = middle + 1
            else:
                right = middle
        return left

    '''
    insert the new value into sorted list    
    '''
    def add(self, value):
        #find the value's index
        index = self.__bisect_left(value)
        if index == len(self.__list):
            self.__list.append(value)
        else:
            self.__list.insert(index, value)

    '''
    remove 'value' from the list
    '''
    def remove(self, value):
        #find the value's index
        index = self.__bisect_left(value)
        if index < len(self.__list) and self.__list[index] == value:
            del self.__list[index]#delete the value from list
        else:
            raise ValueError("{0}.remove(x): x is not in list".format(self.__class__.__name__))

    '''
    count value disappear time in list
    '''
    def count(self, value):
        count = 0
        #find the value's index
        index = self.__bisect_left(value)
        while (index < len(self.__list) and self.__list[index] == value):
            index += 1
            count += 1
        return count

    '''
    get value's station in list
    '''
    def index(self, value):
        #find the value's index
        index = self.__bisect_left(value)
        if index < len(self.__list) and self.__list[index] == value:
            return index
        else:
            raise ValueError("{0}.index(x): x not in list".format(self.__class__.__name__))

    '''
    delete the list[index] value from list
    '''
    def __delitem__(self, index):
        del self.__list[index]

    '''
    the list could not change the value, so raise the error
    '''
    def __setitem__(self, index):
        raise TypeError("use add() to insert a value and rely in the list to put it in the right place")

    def __iter__(self):
        return iter(self.__list)
    
    def __reversed__(self):
        return reversed(self.__list)    

    def __contains__(self, value):
        #find the value's index
        index = self.__bisect_left(value)
        return (index < len(slef.__list) and self.__list[index] == value)
    
    def clear(self):
        self.__list = []

    def pop(self, index = 1):
        return self.__list.pop(index)

    def __len__(self):
        return len(self.__list)

    def __str__(self):
        return str(self.__list)

    def __copy__(self):
        return SortedList(self, self.__key)
    
if __name__ == '__main__':
    sl = SortedList(('a', 'u', 'g', 'p', 'e', 'e2'), str.lower)
    
