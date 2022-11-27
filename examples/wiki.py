import wikipedia as wiki
import json
info=["Qatar","Vidal","Russia","Zelenski","Chile","Paraguay","China","Messi","Pepsi","ElasticSearch"]

for i in info:
    aux=wiki.page(i,auto_suggest=False)
    file="1" if info.index(i)< 5 else "2"
    with open("./"+file+"/"+str(info.index(i))+".txt","w" ,encoding="utf-8") as f:
        
        f.write('{}<tarea3sd>{}'.format(str(info.index(i)),json.dumps(aux.content)))
    
    print("Se escribió el archivo: "+i)    