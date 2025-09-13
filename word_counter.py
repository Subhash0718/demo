s = input("Enter a sentence: ").lower()
l = s.split()
d = {}

for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print(d)
