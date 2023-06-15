 ## Importing the Flask class and request,make_response,jsonify  variable from FLASK
from flask import Flask, request, make_response,jsonify
# Importing the dbhelper , apiHelper   and dbcreds module
import dbhelper
import apiHelper
import dbcreds
# Import the Cross-Origin Resource Sharing (CORS) module
from flask_cors import CORS
# Creating a Flask application instance
app=Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)
# Candy table with (Get) requests
# GET  REQUEST
# Added Route decorator for handling get requests to the  '/api/candy' endpoint getting a candy
@app.get('/api/candy')
    #  Created  Get request handler function that handles the Get data sent from candy 
def get_all_candy():
        # Call the 'get_all_candy()' procedure from the 'dbhelper' module and store the result in a variable
        results = dbhelper.run_procedure('CAll get_all_candy()',[])
        # Checking if the results are of type list
        if(type(results)==list):
        # And if so convert the results in to json file and send a HTTP  status code 200 that represents that the process returned with result successfully
            return make_response(jsonify(results), 200)
        else:
            # or if not came with 500 HTTP satatus code response indicating server error with result representing the database procedure result 
            return make_response(jsonify(results), 500) 
# Candy table with (Post) requests
# POST REQUEST
# Added Route decorator for handling get requests to the  '/api/candy' endpoint adding a candy
@app.post('/api/candy')
def post_new_candy():
        # if error is type string/str then that means we have an error  send HTTP status code  error message with code 400 to show there was an error with the request sent,
        #  and the other code wont  continue to excute
        error=apiHelper.check_endpoint_info(request.json,["name","image_url","description"]) 
        if (error !=None):
         return make_response(jsonify(error), 400)
        #  if there is no error, code will continue to excute and return results from the procedure call function and add a  tokenr to the database
        results = dbhelper.run_procedure('CAll add_new_candy(?,?,?)',[request.json.get("name"),request.json.get("image_url"),request.json.get("description")])
          # Checking if the results are of type list
        if(type(results)==list):
        # And if so convert the results in to json file and send a HTTP  status code 200 that represents that the process returned with result successfully
             return make_response(jsonify(results), 200)
        else:
            # or if not came with 500 HTTP satatus code response indicating server error with result representing the database procedure result 
            return make_response(jsonify(results), 500) 
        # Candy table with (Get) requests
# Candy table with (DELETE) requests
# DELETE REQUEST
# Added Route decorator for handling get requests to the  '/api/candy' endpoint deleting a candy
@app.delete('/api/candy')
def delete_candy():
          # if error is type string/str then that means we have an error  send HTTP status code  error message with code 400 to show there was an error with the request sent,
        #  and the other code wont  continue to excute
        error=apiHelper.check_endpoint_info(request.json,["id"]) 
        if (error !=None):
         return make_response(jsonify(error), 400)
        #  if there is no error, code will continue to excute and return results from the procedure call function and add a  tokenr to the database
        results = dbhelper.run_procedure('CAll delete_candy(?)',[request.json.get("id")])
         # Checking if the results are of type list
        if(type(results)==list):
        # And if so convert the results in to json file and send a HTTP  status code 200 that represents that the process returned with result successfully
             return make_response(jsonify(results), 200)
        else:
            # or if not came with 500 HTTP satatus code response indicating server error with result representing the database procedure result 
            return make_response(jsonify(results), 500) 
        
# Check the production mode and run the application accordingly
if (dbcreds.production_mode == True):
    print("Running in Production Mode")
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing/Development Mode!")

app.run(debug=True)
