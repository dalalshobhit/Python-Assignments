name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()

# Split lines to get hour 
for line in handle:
    line = line.rstrip()
    if line == "": continue
    words = line.split()
    if words[0] != "From" : continue
    time = words[5].split(":")
    count[time[0]] = count.get(time[0], 0) + 1

list = list()
    
for key,val in count.items():
    list.append((key, val))

list.sort()

for hour, count in list:
    print hour, count

