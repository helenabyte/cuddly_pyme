fname = input('Enter the file name:')
fhand = open(fname)
count = 0
tot = 0.0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue

    count = count+1
    print(count)
    pos = line.find(":")
    print(pos)
    extract= line[pos+2:]
    print(extract)
    fl = float(extract)
    print(fl)
    tot = tot+fl

print("Averge Spam Confidence: ", tot/count )
