#1251
#using brute force method
word = input()
chunks = ["", "", ""]
i = 1
j = 2
last = len(word)
flag = 0
while i != last - 2:
    chunks[0] = ''.join(reversed(word[0:i]))
    chunks[1] = ''.join(reversed(word[i:j]))
    chunks[2] = ''.join(reversed(word[j:]))
    reverse = ''.join(chunks)
    if flag == 0: 
        final = reverse
        flag = 1
    if reverse < final: final = reverse
    j += 1
    if j == last: 
        i += 1
        j = i + 1
print(final)