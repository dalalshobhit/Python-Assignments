text = "X-DSPAM-Confidence:    0.8475";
colonPos = text.find(":")
num = text[colonPos+1:]
number = num.split()

for x in number:
    flNum = float(x)
    print flNum
    



