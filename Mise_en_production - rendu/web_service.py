from flask import Flask, jsonify
import os
import numpy as np
import pickle
from flask import Flask, render_template, request 
# import pickleapp = Flask(__name__) # Load the model


app = Flask(__name__)

filename = 'Titanic_prediction.pkl'
le_model = pickle.load(open(filename,'rb'))


@app.route('/predict',methods=['POST'])
def predict():
  
    data = request.get_json(force=True)    
    
    prediction=data['features']  
    output = le_model.predict(prediction) 

    print ('ici cest',output, type(output))

    return jsonify(output[0][0])
    

if __name__ == '__main__':
    
    app.run(debug=True)





