import sha

import string

BASE2  = '01'

BASE10 = '0123456789'

BASE16 = '0123456789ABCDEF'

BASE30 = '123456789ABCDEFGHJKLMNPQRTVWXY'

BASE36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

BASE62 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'

BASEMAX = string.printable

def BaseConvert(number, fromdigits, todigits, ignore_negative = True):
   
    
        if not ignore_negative and str(number)[0] == '-':

                number = str(number)[1:]

                neg = 1

        else:

                neg = 0

        x = long(0)

        for digit in str(number):

                x = x * len(fromdigits) + fromdigits.index(digit)




        res = ''

        while x > 0:

                digit = x % len(todigits)

                res = todigits[digit] + res

                x /= len(todigits)




        if neg:

                res = '-' + res

        return res


def SHAToBase30(digest):


        tdigest = ''.join([ c for i, c in enumerate(digest) if i / 2 * 2 == i ])

        result = BaseConvert(tdigest, BASE16, BASE30)

        while len(result) < 17:

                result = '1' + result
        return result

def AddHyphens(code):


        return code[:5] + '-' + code[5:10] + '-' + code[10:15] + '-' + code[15:]



LicenseID='CN123-12345-12345-12345'

#Copy the Request Code from the dialog

RequestCode='RW51R-C46YJ-M6FG8-5YVFE'

hasher = sha.new()

hasher.update(RequestCode)

hasher.update(LicenseID)

digest = hasher.hexdigest().upper()

lichash = RequestCode[:3] + SHAToBase30(digest)

lichash=AddHyphens(lichash)

#Calculate the Activation Code

data=[7,123,23,87]

tmp=0

realcode=''

for i in data:

        for j in lichash:

                tmp=(tmp*i+ord(j))&0xFFFFF

        realcode+=format(tmp,'=05X')

        tmp=0
        
act30=BaseConvert(realcode,BASE16,BASE30)

while len(act30) < 17:

        act30 = '1' + act30

act30='AXX'+act30

act30=AddHyphens(act30)

print ("The Activation Code is: "+act30)


