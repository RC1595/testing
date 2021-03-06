from flask import Flask, request, Response
from flask_cors import CORS
import mariadb
import json
import sys



app = Flask(__name__)



@app.route('/api')
def home():
    return "Hello World!"

@app.route('/api/fruit', methods=['GET', 'POST', 'PATCH'])
def fruitBasket():
    fruit_name = "dragonfruit"
    if (request.method == 'GET'):
        resp = {
            "fruitName" : fruit_name
        }
        return Response(json.dumps(resp),
                        mimetype="application/json",
                        status=200)
        
    elif request.method == 'POST':
        data = request.json
        print(data)
        if (data.get('fruitName') != None):
            resp = "Wrong fruit"
            code = 400
            if (data.get('fruitName') == fruit_name):
                resp = "Correct fruit"
                code = 201
            return Response(resp,
                            mimetype="text/plain",
                            status=code)
        else:
            return Response("ERROR, MISSING ARGUMENTS",
                            mimetype="text/plain",
                            status=400)
    elif (request.method == 'PATCH'):
        return Response("Endpoint under maintenance",
                        mimetype="text/plain",
                        status=503)
    
    else:
        print("Something went wrong")
        
if (len(sys.argv)> 1):
    mode = sys.argv[1]
    if (mode == "production"):
        import bjoern
        host = '0.0.0.0'
        port = 5000
        print("Server is running in production mode")
        bjoern.run(app, host, port)
    elif(mode == "testing"):
        from flask_cors import CORS
        CORS(app)
        print("Server is running in test mode, switch to production when needed")
        app.run(debug=True)
    else:
        print("invalid mode argument")
        exit()
else:
    print("No Argument")
    exit()

