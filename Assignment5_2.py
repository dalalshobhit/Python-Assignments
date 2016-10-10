minimum = None
maximum = None
numList = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
    	print num
        if minimum == None:
            minimum = num
        elif num < minimum:
            minimum = num
        
        if num > maximum:
            maximum = num
        
    except:
        print "invalid number"
        
print "Maximum is ", maximum
print "Minimum is ", minimum