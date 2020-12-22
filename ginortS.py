'''
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
'''
# Sample Input
# Sorting1234
# Sample Output
# ginortS1324

st = input()
lc, uc = '', ''
ev, dig, od = '', '', ''

for c in st:
    if c.islower():
        lc = lc + c

    elif c.isupper():
        uc = uc + c

    else:
        dig = dig + c

for d in dig:
    if int(d) % 2 == 0:
        ev = ev + d
    else:
        od = od + d

result = sorted(lc) + sorted(uc) + sorted(od) + sorted(ev)
print(''.join(result))
