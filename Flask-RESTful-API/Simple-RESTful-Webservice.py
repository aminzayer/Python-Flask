from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/getcustomer')
def get_incomes():
    
    with open('data.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    
    return jsonify(json_object)


@app.route('/addcustomer', methods=['POST'])
def add_customer():
    My_Customer = request.get_json()
    
    print(My_Customer)
    # Writing to sample.json
    with open("Python-Flask/Flask-RESTful-API/data.json", "w") as outfile:
        json.dump(My_Customer, outfile)

    return "Customer Added Successfully", 204

app.run()
