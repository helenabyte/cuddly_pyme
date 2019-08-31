fname = input("Enter the file name ")
fhand = open(fname)
lst = list()
for line in fhand:
    print(line.rstrip())
    sep = line.split()
    for s in sep:
        if s not in lst:
            lst.append(s)

lst.sort()
print(lst)
