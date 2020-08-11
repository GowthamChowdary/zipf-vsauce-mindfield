import csv
import io 
dict1=dict()
##count and make a dict from the subs txt file
with io.open('fname','r',encoding="utf-8") as f:
    for line in f:
        splits = line.split()
        for word in splits:
            if word in dict1:
                dict1[word]=dict1[word]+1

            else:
                dict1[word]=1    
f.close()
#writes to the csv file
with io.open('output.csv', 'w',encoding="utf-8") as output:
    writer = csv.writer(output)
    for key, value in dict1.items():
        writer.writerow([key, value])
output.close()        
