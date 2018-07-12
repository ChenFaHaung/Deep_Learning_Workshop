import csv
from operator import itemgetter

exampleFile = open('example.csv')
exampleReader =	csv.reader(exampleFile)
#el = list(exampleReader)
data = []
for row in exampleReader:
    last = int(row[len(row) - 1])
    newlst = row[0:len(row)-1]
    newlst.append(last)
    data.append(newlst)

data.sort(key = itemgetter(len(data[0]) - 1))
for col in data:
    print('Row #'+str(data.index(col)+1)+''+str(col))