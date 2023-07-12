str = input()
a = ''
for i in str:
    if i.islower():
        a += i.upper()
    else:
        a += i.lower()
print(a)