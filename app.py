from flask import Flask,jsonify, request
 
app = Flask(__name__)
 
contacts = [
    {
        'Contacts': 9818446120,
        'Name': u'Ishita',
        'id': 1,
        'done': False
    },
    {
        'Contacts': 9818829512,
        'Name': u'Aanshi',
        'id': 2,
        'done': False
    }
]
 
@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message": "Please provide the data!"
        },400)
 
    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['Name'],
        'contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"Success",
        "message": "Task added succesfully!"
    })
   
 
@app.route("/get-data")

def get_task():
    return jsonify({
        "data" : contacts
    })
 
if (__name__ == "__main__"):
    app.run(debug=True)

