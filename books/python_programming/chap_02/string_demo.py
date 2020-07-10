mystr = 'xxxSPAMxxx'
print(mystr.find('SPAM'))

mystr = 'xxaaxxaa'
print(mystr.replace('aa', 'SPAM'))

mystr = 'xxxSPAMxxx'
print('SPAM' in mystr)
print('Ni' in mystr)
print(mystr.find('Ni'))

mystr = '\t Ni\n'
print(mystr.strip())
print(mystr.rstrip())

mystr = 'SHRUBBERY'
print(mystr.lower())
print(mystr.isalpha())
print(mystr.isdigit())

mystr = 'aaa,bbb,ccc'
print(mystr.split(','))

mystr = 'a b\nc\nd'
print(mystr.split())

# todo 这个现象和我预想的并不一样
mystr = 'NI'
print(mystr.join(['aaa', 'bbb', 'ccc']))
print(' '.join(['aaa', 'bbb', 'ccc']))

# todo 这个难道就是修改字符串的方案
mychars = list('Lorreta')
print(mychars)
mychars.append('!')
print(''.join(mychars))

mystr = 'xxaaxxaa'
print('SPAM'.join(mystr.split('aa')))

import string

print(string.ascii_lowercase)
print(string.whitespace)

print(int('42'))
print(eval('42'))

print(str(42))
print(repr(42))

print("%d" % 42)
print('{:d}'.format(42))
print("42" + str(1))
print(int("42") + 1)
