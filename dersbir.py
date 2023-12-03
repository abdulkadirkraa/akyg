from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Students(Resource):
    def get(self):
        data = pd.read_csv('students.csv')
        data = data.to_dict('records')
        return {'data': data}, 200

    def post(self):
        json = request.get_json()
        req_data = pd.DataFrame({
            'name': [json['name']],
            'age': [json['age']],
            'department': [json['department']],
            'average': [json['average']]
        })
        data = pd.read_csv('students.csv')
        data = pd.concat([data, req_data], ignore_index=True)
        data.to_csv('students.csv', index=False)
        return {'message': 'Student record successfully added.'}, 200

    def delete(self):
        name = request.args['name']
        data = pd.read_csv('students.csv')

        if name in data['name'].values:
            data = data[data['name'] != name]
            data.to_csv('students.csv', index=False)
            return {'message': 'Student record successfully deleted.'}, 200
        else:
            return {'message': 'Student record not found.'}, 404

# Add URL endpoints
api.add_resource(Students, '/students')

if __name__ == '__main__':
    app.run()
