from flask import Flask, request, json
from sqlalchemy import or_,and_
import configs
from exts import db  
from models import * 

app = Flask(__name__)
app.config.from_object(configs)
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/example', methods=['GET'])  # only 'get'
def example():
    id = request.values.get('id')
    # get data from database
    res = User.query.filter(User.id == id).first()
    if res is None:
        return json.dumps({'states': 'failed'})
    
    return json.dumps({
        'states': 'success',
        'data': {'id': res.id, 'username': res.username, 'password': res.password}
        })

@app.route('/example2', methods=['POST'])  # only 'get'
def example2():
    # get data from request
    id = int(request.values.get('id'))
    username = str(request.values.get('username'))
    password = str(request.values.get('password'))
    user = User(id=id, username=username, password=password)
    
    # add data to database
    db.session.add(user)
    db.session.commit()
    
    return json.dumps({'states': 'success'})

# TODO: add your api, and you can use postman to test it

# TODO: Learn how to use sqlalchemy to operate database, the document is here: https://docs.sqlalchemy.org/en/20/index.html

if __name__ == '__main__':
    app.run(port=5000, debug=True)