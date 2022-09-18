from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")
auth = HTTPBasicAuth()


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    result = tasks
    print(result)
    print(request.args)
    print('done' in request.args)
    if 'done' in request.args:
        result = list(filter(lambda t: t['done'] == bool(request.args.get('done')), result))
    print(result)
    print('title' in request.args)
    if 'title' in request.args:
        result = list(filter(lambda t: t['title'] == request.args.get('title'), result))
    print(result)
    return jsonify({'tasks': result})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
    # return jsonify({'task': make_public_task(task[0])})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.form or not 'title' in request.form:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.form.get('title'),
        'description': request.form.get('description', ""),
        'done': request.form.get('done', 'False') == 'True'
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
    # return jsonify({'task': make_public_task(task)}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    if not request.form:
        abort(400)
    if 'title' not in request.form \
            and 'description' not in request.form \
            and ('done' not in request.form and type(request.form.get('done')) is not bool):
        abort(400)
    task[0]['title'] = request.form.get('title', task[0]['title'])
    task[0]['description'] = request.form.get('description', task[0]['description'])
    task[0]['done'] = request.form.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
