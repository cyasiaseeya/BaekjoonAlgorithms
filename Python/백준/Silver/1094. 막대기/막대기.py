#1094

o = 64
ha = 0
f = 0
count = 0
i = 10
x = int(input())
while(o + f > x):
    if (o + f > x):
        o /= 2
        ha = o
    if (o + f >= x):
        ha = 0
    else:
        f += ha
        count += 1
f += o
count += 1
print(count)