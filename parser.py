## wanted to do it with reddit comments first, but the comments were too messy and took way too long to clean them, and testing it on vsauce made alot of sense so I did it with vsauce
## this basically opens the comments file from pushapi and counts and writes the comments to a text file

import json
import io
comments = []

for line in open('comments', 'r'):
    comments.append(json.loads(line))  
with io.open("myfile.txt", "w", encoding="utf-8") as f:     
    for i in comments:

        f.writelines(str(i["body"]))
f.close()     
