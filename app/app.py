from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():

    title = '<H1>Entete http</h1>'
    content = ""
    
    for key,val in request.headers.items():
        content = content + key + "=>"+ val + "<br>"

    return title + content

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)