from flask import Flask, request, render_template
import wikipedia as wiki
import json
app = Flask(__name__)

info=["Qatar","Vidal","Russia","Zelenski","Chile","Paraguay","China","Messi","Pepsi","ElasticSearch"]

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/buscador', methods=['GET'])
def buscador():
    file= open("./db.json","r")
    buscador= request.args['buscador']
    db=json.load(file)

    if(buscador not in db):
        return "no está esa palabra"

    urls= []
    while(len(db[buscador])>0):
        aux = 0
        files = ""
        for i in db[buscador]:
            if(aux < int(db[buscador][i])):
                aux= db[buscador][i]
                files= i
        db[buscador].pop(files)             
        urls.append(wiki.page(info[int(files)],auto_suggest=False).url)
        url=''
    for j in urls:
        url += "Url: "+j+"\n"
    return url

if __name__ == '__main__':
    app.run(debug=True)