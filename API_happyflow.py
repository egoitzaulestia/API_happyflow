# from flask import Flask, request, jsonify
import os


os.chdir(os.path.dirname(__file__))

# import pandas as pd
from flask import Flask, request, jsonify
# from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import pickle

app = Flask(__name__)
cors = CORS(app)
app.config['DEBUG'] = True


@app.route('/')
def home():
    return jsonify({'message': 'Let\'s fucking DOOOOOOOOO IIIIIIIIIIITTTTTTT !!!!!!!!!! '})


@app.route('/predict', methods=['GET'])
def predict():
    try:
        model = pickle.load(open('modelo.pkl','rb'))

        surface = int(request.args.get('surface'))
        bedrooms = int(request.args.get('bedrooms'))
        restrooms = int(request.args.get('restrooms'))

        input_data = [[surface, bedrooms, restrooms]]
        prediction = model.predict(input_data)

        return jsonify({'prediction': float(prediction[0])})
    except (ValueError, TypeError, FileNotFoundError):
        return jsonify({'error': 'Asegúrate de proporcionar surface, bedrooms y restrooms como parámetros en la URL.'}), 400


# app.run()

# if __name__ == '__main__':
  #  app.run(debug=True, host="0.0.0.0", port=5001)
