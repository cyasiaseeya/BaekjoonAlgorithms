#1193

num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
if line % 2 == 0:
    numer = num
    denom = line - num + 1

elif line % 2 == 1:
    numer = line - num + 1
    denom = num

print(f'{numer}/{denom}')