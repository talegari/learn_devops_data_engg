import pandas
import joblib
import numpy as np
import sklearn.datasets as datasets
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

model_load_path = "~/rf_regressor_boston.pkl" #Update with the right path

# Load the model
print("Loading the model...")
loaded_model = joblib.load(model_load_path) 

# Argument parsing
parser = reqparse.RequestParser()
parser.add_argument('input_data')


class PredictVal(Resource):
    def get(self):

        args = parser.parse_args()
        user_query = args['input_data']
        all_user_input = user_query.split(';')

        result = []
        for item in all_user_input:
            query_param_list = item.split(',')  
            temp = [int(num) for num in query_param_list]
            result.append(np.array(temp))
        result = np.asarray(result)

        # Get predictions
        prediction = loaded_model.predict(result).tolist()

        # Create JSON object
        output = {'prediction': prediction}
        
        return output


# Routing the URL to the resource
api.add_resource(PredictVal, '/')


if __name__ == '__main__':
    app.run(debug=True)



