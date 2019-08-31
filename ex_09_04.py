fname = input('Enter the file name:')
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)

counts = dict()

for line in fhand:
    line = line.rstrip()
    flist = line.split()

    if len(flist) < 1 or flist[0] != "From": continue

    email = flist[1:2]

    for name in email:
        counts[name] = counts.get(name,0)+1

#print(counts)

bigcount = None
bigword = None

for name,freq in counts.items():
    if bigcount == None or freq>bigcount:
        bigword = name
        bigcount = freq

print(bigword, bigcount)
