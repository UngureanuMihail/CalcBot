operations = set()
operations.add('+')
s1 = '1+2'
s2 = '1 + 2'
s3 = '1+ 2'
s4 = '1 +2'

def my_parce(s,op):
    l=[]
    tmp = ''
    for c in s:
        if c not in op and c != ' ':
            tmp += c
        else:
            if tmp:
                l.append(tmp)
            if c in op:
                l.append(c)
            tmp = ''
    l.append(tmp)
    return l

print(my_parce(s1,operations))
print(my_parce(s2,operations))
print(my_parce(s3,operations))
print(my_parce(s4,operations))
