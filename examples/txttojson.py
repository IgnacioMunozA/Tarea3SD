import json

file = open("./outhadoop/output.txt","r")
file.readline()

files={}

for i in file:
    word, doc = i.split('\t')
    for line in doc.replace('\n','').replace(' ','').replace('(', '').split(')')[0:-1]:
        docs, aux = line.split(',')
        if word in files.keys():
            files[word][docs] =int(aux)
        else:
            files[word]={docs:int(aux)}

with open("../buscador/db.json","w") as outfile:
    json.dump(files,outfile,indent=4)            
