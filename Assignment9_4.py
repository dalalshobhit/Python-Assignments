name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = 0
words = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        sender = words[5]
        

#maxValue = 0

# maxValue = max(words, key=words.get)

#for key, value in words.items():
 #   if maxValue == None: maxValue = value
  #  if maxValue < value : 
   #     maxValue = value
    #    maxWord = key

#print maxWord, maxValue
