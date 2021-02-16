import csv
from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

# initialize Flask application and an API
app = Flask(__name__)
api = Api(app)

path = r'C:\Users\OXXO\Downloads\recommends.csv'

class product(Resource):
    def out_stuff(self, path):
        with open(path) as csvfile :
            data = csv.reader(csvfile)
            for row in data:
                yield row

    def get(self, sku, sim=0):
        recoms = []
        sim = float(sim)
        for i in product.out_stuff(self, path):
            if i[1]==sku and sim==0:
                recoms.append(i)
            elif i[1]==sku and sim>0:
                if float(i[2]) > sim:
                   recoms.append(i)
        return recoms, 201

# registering Video as Resource
api.add_resource(product, "/prod/<string:sku>/<string:sim>")

if __name__ == "__main__":
    app.run(debug=True)
