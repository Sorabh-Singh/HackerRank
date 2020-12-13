"""
Input Format

The first line contains the integer, .
The next  lines each contain a word.

Output Format

Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
"""
from collections import Counter
words = Counter([input() for _ in range(int(input()))])
print(len(words))
for keys, values in words.items():
    print(values, end=' ')

# second approach:

words = Counter([input() for _ in range(int(input()))])
print(len(words))
print(*words.values())
