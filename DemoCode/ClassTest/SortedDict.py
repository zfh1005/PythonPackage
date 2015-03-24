from SortedList import SortedList

class SortedDict(dict):
    def __init__(self, dictionary = None, key = None, **kwargs):
        dictionary = dictionary or {}
        super().__init__(dictionary)
        if kwargs:
            super.update(kwargs)
        self.__keys = SortedList(super().keys(), key)

    '''
    updata the dictionary 
    '''
    def updata(self, dictionary = None, **kwargs):
        if dictionary is None:
            pass
        elif isinstance(dictionary, dict):
            super().update(dictionary)
        else:
            for key, value in dictionary.items():
                super().__setitem__(key, value)
        if kwargs:
            super().update(kwargs)
        self.__keys = SortedList(super().keys(), self.__keys.key)

    @classmethod
    def fromkeys(cls, iterable, value = None, key = None):
        return cls({k : value for k in iterable}, key)

    '''
    set dict[key] = value
    '''
    def __setitem__(self, key, value):
        if key not in self:
            self.__keys.add(key)
        return super().__setitem__(key, value)

    '''
    delete the dict[key] items
    '''
    def __delitem__(self, key):
        try:
            self.__keys.remove(key)
        except ValueError:
            raise KeyError(key)
        return super().__delitem__(key)

    '''
    set the dictionary to default statue
    '''
    def setdefault(self, key, value = None):
        if key not in self:
            self.__keys.add(key)
        return super().setdefault(key, value)

    '''
    delete the lastest item dict[len(keys) - 1] from the dictionary
    '''
    def pop(self, key, *args):
        if key not in self:
            if len(args) == 0:
                raise KeyError(key)
            return args[0]
        self.__keys.remove(key)
        return super().pop(key, args)  

    '''
    delete the lastest item from the dictionary
    '''
    def popitem(self):
        item = super().popitem()
        self.__keys.remove(item[0])
        return item

    '''
    clear the all keys from the dictionary
    '''
    def clear(self):
        super().clear()
        self.__keys.clear()

    '''
    get the dict's value list
    '''
    def values(self):
        for key in self.__keys:
            yield self[key]

    '''
    get the dict's key list
    '''
    def keys(self):
        for key in self.__keys:
            yield self.__key

    '''
    get the dict's item list
    '''
    def items(slef):
        for key in self.__keys:
            yield (key, self[key])
    '''
    get the dict's key list
    '''
    def __iter__(self):
        return iter(self.__keys)

    def __repr__(self):
       return object.__repr__(self)

    '''
    get the dict's string describe
    '''
    def __str__(self):
        return ("{" + ",".join(["{0!r}:{1!r}".format(k, v) for k, v in self.items()]) + "}")

    '''
    get a copy of the dictionary
    '''    
    def copy(self):
        d = SortedDict()
        super(SortedDict, d).update(self)
        d.__keys = self.__keys.copy()
        return d

    '''
    get the value's index
    '''
    def value_at(self, index):
        return self[self.__keys[index]]

    '''
    set the value at the index
    '''
    def set_value_at(self, index, value):
        self[self.__keys[index]] = value
    
if __name__ == '__main__':
    sd = SortedDict(dict(a = '25', v = '38', ac = '94', d = '74', h = '34', x = '24'))
