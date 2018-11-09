# Product service
from flask import Flask
from flask_restful import Resourcem Api

app = Flask(__name__)
api = Api(app)

class Prodcut(Resource):
    def get(self):
        return{
                'product': ['Ice cream',
                            'Chocolate',
                            'Fruit']
                }
api.add_resource(Product,'/')

if __name__ == '__main__':
    # listening on port 80
    app.run(host='0.0.0.0', port=80, debug=True)

