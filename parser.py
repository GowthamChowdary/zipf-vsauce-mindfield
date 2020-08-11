import json
import io
comments = []

for line in open('comments', 'r'):
    comments.append(json.loads(line))  
with io.open("myfile.txt", "w", encoding="utf-8") as f:     
    for i in comments:

        f.writelines(str(i["body"]))
f.close()     