name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle :
	line = line.rstrip()
	if line == "": continue
	words = line.split()
	if words[0] != "From" : continue
	time = words[5].split(":")
	counts[time[0]] = counts.get(time[0], 0) + 1
    #can label time[0] a separate variabke

list = list()

for key,value in counts.items() :
	list.append((key,value))

slist= sorted(list)

for key,value in slist: #or any other name for 2 iter vs
    print(key,value)
