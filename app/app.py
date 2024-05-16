from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route('/')
def index():
    # return jsonify(
    #     status=True,
    #     message='Welcome to the Dockerized Flask app!'
    # )
    return render_template('index.html')

# @app.route('/todo')
# def todo():
#     _todos = db.todo.find()

#     item = {}
#     data = []
#     for todo in _todos:
#         item = {
#             'id': str(todo['_id']),
#             'todo': todo['todo']
#         }
#         data.append(item)

#     return jsonify(
#         status=True,
#         data=data
#     )

# @app.route('/todo', methods=['POST'])
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
     app.run()
