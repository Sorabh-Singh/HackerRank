'''
Explanation

Delete the following characters from the strings make them anagrams:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
It takes  deletions to make both strings anagrams.
'''
# a = 'cde'
# b = 'dcf'
from collections import Counter
def makeAnagram(a, b):
    li1 = list(a)
    li2 = list(b)
    print(list(list(set(li1) -set(li2)) + list(set(li2) -set(li1))))
    ct_a = Counter(a)
    ct_b = Counter(b)
    print(ct_a, ct_b)
    ct_a.subtract(ct_b)
    print(ct_a)
    print(ct_a.values())
    return sum(abs(i) for i in ct_a.values())

print(makeAnagram('cde', 'dcf'))