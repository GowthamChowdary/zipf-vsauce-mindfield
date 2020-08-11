import csv
import io 
dict1=dict()
##code to get the dict
with io.open('subs.txt','r',encoding="utf-8") as f:
    for line in f:
        splits = line.split()
        for word in splits:
            if word in dict1:
                dict1[word]=dict1[word]+1

            else:
                dict1[word]=1    
f.close()
#print(dict1)

with io.open('output.csv', 'w',encoding="utf-8") as output:
    writer = csv.writer(output)
    for key, value in dict1.items():
        writer.writerow([key, value])
output.close()        