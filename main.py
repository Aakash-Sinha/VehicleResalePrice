# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:55:39 2021

@author: AAKASH
"""
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('linear_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    #Fuel_Type_Diesel=0
    if request.method == 'POST':
        
        km_driven=int(request.form['km_driven'])
        
        ex_showroom_price=float(request.form['ex_showroom_price'])
        
        
        
        
        Year = int(request.form['year'])
        
        
        
        
        
        name=request.form['name']
        if(name=='Hero'):
            name_Hero=1
            name_Honda=0
            name_Royal = 0
            name_Suzuki = 0
            name_TVS = 0
            name_Yamaha = 0
        elif(name=='Honda'):
            name_Hero=0
            name_Honda=1
            name_Royal = 0
            name_Suzuki = 0
            name_TVS = 0
            name_Yamaha = 0
        elif(name=='Yamaha'):
            name_Hero=0
            name_Honda=0
            name_Royal = 0
            name_Suzuki = 0
            name_TVS = 0
            name_Yamaha = 1
        elif(name=='Royal'):
            name_Hero=0
            name_Honda=0
            name_Royal = 1
            name_Suzuki = 0
            name_TVS = 0
            name_Yamaha = 0
        elif(name=='TVS'):
            name_Hero=0
            name_Honda=0
            name_Royal = 0
            name_Suzuki = 0
            name_TVS = 1
            name_Yamaha = 0
        elif(name=='Suzuki'):
            name_Hero=0
            name_Honda=0
            name_Royal = 0
            name_Suzuki = 1
            name_TVS = 0
            name_Yamaha = 0
        else:
            name_Hero=0
            name_Honda=0
            name_Royal = 0
            name_Suzuki = 0
            name_TVS = 0
            name_Yamaha = 0
        
        
            
        
        Seller_Type=request.form['seller_type_Individual']
        if(Seller_Type=='Individual'):
            Seller_Type_Individual=1
        else:
             Seller_Type_Individual=0
             
                 # Present_Price=float(request.form['Present_Price'])
                 
        
       # Kms_Driven2=np.log(Kms_Driven)
        Owner=request.form['owner']
        if(Owner=='First Owner'):
            owner_second=0
            owner_third=0
        elif(Owner=='Second Owner'):
            owner_second=1
            owner_third=0
        elif(Owner=='Third Owner'):
            owner_second=0
            owner_third=1
            
        
        Year=2021-Year
       	
       
        prediction=model.predict([[km_driven,ex_showroom_price,Year,name_Hero,name_Honda,name_Royal,name_Suzuki,name_TVS,name_Yamaha,Seller_Type_Individual,owner_second,owner_third]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_text="Sorry you cannot sell this bike")
        else:
            return render_template('index.html',prediction_text="You Can Sell The bike at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

