fname = input('Enter the file name:')
if len(fname) < 1 :
    fname = "mbox-short.txt"
fhand = open(fname)



count = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    count = count+1
    fline = line.split()
    #print(fline)
    print(fline[1])

print("There were", count, "lines in the file with From as the first word")
