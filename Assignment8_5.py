fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()

for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        email = line[1]
        print email
        lst.append(email)
        
count = len(lst)
print "There were", count, "lines in the file with From as the first word"
