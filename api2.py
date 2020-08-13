from flask import Flask,  jsonify
from flask_restful import Api, Resource, reqparse, request

app = Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

users = [
    {
        "id": 1,
        "login": "walid",
        "pasword": "walid@yahoo.fr"
    },
    
    {
        "id": 2,
        "login": "jacob",
        "password": "jacob.wallas@gmail.com"
    },
    {
        "id": 3,
        "login": "peter",
        "password": "peter.pan@yahoo.com"
    },
    {
        "id": 4,
        "login": "mourad",
        "password": "mourad_abidi@gmail.com"
    },
    {
        "id": 5,
        "login": "montassar",
        "password": "montasar.abidi@yahoo.com"
    }
]

class User(Resource):
    @app.route('/api/v1/users/',  methods=['GET'])
    @app.route('/api/v1/users',  methods=['GET'])
    def getall():
        return jsonify({"message":"affichage des utilisateurs","users":users})

    def get(self, id):
        for user in users:
            if(id == user["id"]):
                return user, 200
        return "User not found", 404
    @app.route('/api/v1/users', methods=['POST'])
    def post():
        id = request.args.get("id")
        login = request.args.get("login")
        password = request.args.get("password")
        
        
        for user in users:
            if(id == user["id"]):
                return "user with id {} already exists".format(id), 400

        user = {
            "id": id,
            "login": login,
            "password": password
        }
                     

        users.append(user)
        return user, 201
    @app.route('/api/v1/users', methods=['PUT'])
    def put():
        id = request.args.get("id")
        login = request.args.get("login")
        password = request.args.get("password")
        

        for user in users:
            if(id == user["id"]):
                user["login"] = login
                user["password"] = password
                return user, 200
        user = {
            "id": id,
            "login": args["login"],
            "password": args["password"] 
        }
                         

        
        users.append(user)
        return user, 201

    def delete(self, id):
        global users
        users = [user for user in users if user["id"] != id]
        return "{} is deleted.".format(id), 200
      
api.add_resource(User, '/api/v1/users/<int:id>')

app.run(debug=True, port=8080)
