#useless file to delete
from flask import Flask, render_template
# from flask_restful import Resource, Api

app = Flask(__name__)
# api = Api(app)


@app.route('/')
# def hello_world():
#     return 'Hello World!'

def accueil():
    return render_template('index.html')

# class Accueil(Resource):
#     def get(self):
#         return render_template('index.html')


# api.add_resource(Accueil, '/')

if __name__ == '__main__':
    app.run(debug=True)