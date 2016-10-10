fname = raw_input("Enter a file name: ")
openFile = open(fname)
for line in openFile :
    line = line.rstrip().upper()
    print line