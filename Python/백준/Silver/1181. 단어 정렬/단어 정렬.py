#1181

words = []
n = int(input())
words = set(input().strip() for _ in range(n))
words = sorted(words, key = lambda x: (len(x), x)) #Python sorts tuples in a specific order, first by the element, then by the second element

for word in words:
    print(word)