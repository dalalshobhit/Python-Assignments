import re

# read data file
txtFile = open("regex_sum_288742.txt")

floatNumbers = list()

for line in txtFile:
    line = line.rstrip()
    # read all numbers in file
    numbers = re.findall('([0-9]+)', line)
    if len(numbers) <1 : continue
    # create a num list with float numbers for each line
    num = [float(i) for i in numbers]
    # create a single list of all lists
    floatNumbers.append([float(i) for i in numbers])

# add all the numbers in a list of lists and print sum
print int(sum(sum(x) for x in floatNumbers))