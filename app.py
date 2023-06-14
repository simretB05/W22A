from flask import Flask, request, make_response,jsonify
import json
import dbhelper
import apiHelper

app=Flask(__name__)
@app.get('')
def ():
    results = dbhelper.run_procedure('CAll ()',[])
    if(type(results)==list):
        _json= json.dumps(results,default=str)
        return _json
    else:
        return 'sorry please try again'
app.run(debug=True)
