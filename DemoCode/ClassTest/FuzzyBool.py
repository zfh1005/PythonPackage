class FuzzyBool():
    #struct function
    def __init__(self, value = 0.0):
        self.__value = value if 0.0 <= value <= 1.0 else 0.0

    #NOT(!) operation
    def __invert__(self):
        return FuzzyBool(1.0 - self.__value)

    #AND(&) operation
    def __and__(self, other):
        return FuzzyBool(min(self.__value, other.__value))

    #AND(&=) operation
    def __iand__(self, other):
        self.__vaule = min(self.__value, other.__value)
        return self

    #OR(||) operation
    def __or__(self, other):
        return FuzzyBool(max(self.__value, other.__value))

    #OR(&=) operation
    def __ior__(self, other):
        self.__vaule = max(self.__value, other.__value)
        return self

    #repr operation
    def __repr__(self):
        return ("{0}({1})".format(self.__class__.__name__, self.__value))

    #str operation
    def __str__(self):
        return str(self.__value)

    #bool operation
    def __bool__(self):
        return self.__value > 0.5

    #int operation
    def __int__(self):
        return round(self.__value)

    #float operation
    def __float__(self):
        return self.__value

    #lt operation
    def __lt__(self):
        return self.__value < other.__value
    
    #float operation
    def __eq__(self):
        return self.__value == other.__value

    #hash operation
    def __hash__(self):
        return hash(self)

    #format operation
    def __format__(self, format_spec):
        return format(self.__vaule, format_spec)

    #format operation
    def __format__(self, format_spec):
        return self.__vaule.__format(format_spec)

    @staticmethod
    def conjunction(*fuzzies):
        return FuzzyBool(min([float(x) for x in fuzzies]))
    @staticmethod
    def disjunction(*fuzzies):
        return FuzzyBool(max([float(x) for x in fuzzies]))


if __name__ == '__main__':
    fb = FuzzyBool(0.1)
    print(fb.__repr__())
        
