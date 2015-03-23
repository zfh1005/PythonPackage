class FuzzyBool(float):
    def __new__(cls, value = 0.0):
        return super().__new__(cls, value if 0.0 <= value <= 1.0 else 0.0)

    def __invert__(self):
        return FuzzyBool(1.0 - float(self))

    def __and__(self, other):
        return FuzzyBool(min(self, other))

    def __iand__(self, other):
        return FuzzyBool(min(self, other))

    def __or__(self, other):
        return FuzzyBool(max(self, other))

    def __ior__(self, other):
        return FuzzyBool(max(self, other))
    
    def __repr__(self):
        return ("{0}({1})".format(self.__class__.__name__, self.__value))
    
    def __bool__(self):
        return self > 0.5

    def __int__(self):
        return round(self)

    def __add__(self, other):
        raise TypeError("unsupported operand type(s) for + :"
                        "'{0}' and '{1}'".format(
                            self.__class__.name__, other.__class__.__name__))

    def __neg__(self):
        raise TypeError("bad operand type for unary - : '{0}'".format(self.__class__.__name__))

    def __eq__(self, other):
        return NotImplemetedError

    for name, operator in(("__xor__", "^"),
                          ("__ixor__", "^="),
                          ("__add__", "+"),
                          ("__iand__", "+="),
                          ("__rand__", "+"),
                          ("__sub__", "-"),
                          ("__isub__", "-="),
                          ("__rsub__", "-"),
                          ("__mul__", "*"),
                          ("__imul__", "*="),
                          ("__rmul__", "*"),
                          ("__pow__", "**"),
                          ("__ipow__", "**="),
                          ("__ifloordiv__", "//="),
                          ("__rfloordiv__", "//"),
                          ("__truediv__", "/"),
                          ("__itruediv__", "/="),
                          ("__rtruediv__", "/"),
                          ("__divmod__", "%"),
                          ("__imod__", "%="),
                          ("__rmod__", "%"),
                          ("__lshift__", "<<"),
                          ("__ilshift__", "<<="),
                          ("__rlshift__", ">>"),
                          ("__rshift__", "<<"),
                          ("__irshift__", "^"),
                          ("__rrshift__", "^"),
                          ):
        message = ("unsupported operand type(s) for {0}:"
                   "'{{self}}'{{join}}{{args}}".format(operator))
        exec("def {0}(self, *args):\n"
             "    types = [\"'\" + arg.__class__.__name__ + \"'\""
             "for arg in args]\n"
             "    raise TypeError(\"{1}\".format("
             "self = self.__class__.__name__, "
             "join = (\" and \" if len(args) == 1 else \",\"),"
             "args = \",\".join(types)))".format(name, message))

if __name__ == '__main__':
    fb = FuzzyBool(0.4)
    fb.__lshift__(0.9)

        
    
    
    
    
    
