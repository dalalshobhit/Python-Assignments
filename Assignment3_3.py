try:
    score = raw_input("Enter score:")
    s = float(score)
except:
    print "Enter numeric score"
    exit()
    

if s < 0.0 or s > 1.0 :
    print "Value out of range"
    exit()
elif s >= 0.9 :
    print "A"
elif s >= 0.8 :
    print "B"
elif s >= 0.7 :
    print "C"
elif s >= 0.6 :
    print "D"
else :
    print "F"