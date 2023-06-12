from flask import Flask,request, make_response,jsonify
import json
import dbhelper

app=Flask(__name__)


def check_endpoint_info(sent_data, expected_data):
    for data in expected_data:
        if(sent_data.get(data) == None):
          return f"The {data} parameter is required!"
        
@app.post('/api/clients')
def post_new_client():
    valid_check=check_endpoint_info(request.json, ['username','password','is_preimium'])
    if(type(valid_check)==str):
            return  valid_check
    username=request.json.get('username')
    password=request.json.get('password')
    is_preimium= request.json.get('is_preimium')
    results = dbhelper.run_procedure('CAll add_new_client(?,?,?)',[username,password,is_preimium])  
    if(type(results)==list):
        return make_response(jsonify(results), 200)
        
    else:
      return make_response(jsonify(results), 400)
    
@app.patch('/api/clients')
def change_password():
    valid_check=check_endpoint_info(request.json, ['username','old_password_input','new_password_input'])
    if(type(valid_check)==str):
            return  valid_check
    username=request.json.get('username')
    old_password_input=request.json.get('old_password_input')
    new_password_input= request.json.get('new_password_input')
    results = dbhelper.run_procedure('CAll change_password(?,?,?)',[username,old_password_input,new_password_input])  

    if(type(results)==list):
        return make_response(jsonify(results), 200)
        
    else:
      return make_response(jsonify(results), 400)
    

@app.get('/api/satus')
def get_status():

    results = dbhelper.run_procedure('CAll return_status()',[])  

    if(type(results)==list):
        return make_response(jsonify(results), 200)
        
    else:
      return make_response(jsonify(results), 500)
    
app.run(debug=True)
