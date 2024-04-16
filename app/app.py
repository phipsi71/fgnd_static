import os
from flask import Flask, request, jsonify, render_template
from werkzeug.middleware.proxy_fix import ProxyFix


application = Flask(__name__)
# application.config['APPLICATION_ROOT'] = '/dtcui'
application.wsgi_app = ProxyFix(
    application.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@application.route('/')
def index():
    # return jsonify(
    #     status=True,
    #     message='Welcome to the Dockerized Flask application!'
    # )
    return render_template('index.html')

# @application.route('/todo')
# def todo():
#     _todos = db.todo.find()

#     item = {}
#     data = []
#     for todo in _todos:
#         item = {
#             'id': str(todo['_id']),
#             'todo': todo['todo']
#         }
#         data.applicationend(item)

#     return jsonify(
#         status=True,
#         data=data
#     )

# @application.route('/todo', methods=['POST'])
# def createTodo():
#     data = request.get_json(force=True)
#     item = {
#         'todo': data['todo']
#     }
#     db.todo.insert_one(item)

#     return jsonify(
#         status=True,
#         message='Todo saved successfully!'
#     ), 201

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5020)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
