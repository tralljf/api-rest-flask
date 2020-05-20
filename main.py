from flask import Flask, jsonify, request

import json

app = Flask(__name__)

tasks = [{
  'id': 0,
  'responsavel': 'Thiago',
  'tarefa': 'Criar api',
  'status': 'Atrasado'
}, {
  'id': 1,
  'responsavel': 'Pedro',
  'tarefa': 'Criar projeto',
  'status': 'Concluido'
}]

@app.route('/api', methods=['GET', 'POST'])
def developer_all():
  if request.method == 'GET':
    return jsonify(tasks)

  if request.method == 'POST':
    task = json.loads(request.data)

    task['id'] = len(tasks)

    tasks.append(task)

    return jsonify(task)

@app.route('/api/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
  try:
    if request.method == 'GET':
      return jsonify(tasks[id])

    if request.method == 'PUT':
      data = json.loads(request.data)

      tasks[id] = data

    if request.method == 'DELETE':
      tasks.pop(id)

    return jsonify(tasks)
  except:
    return jsonify({'status': 'erro','message': 'Unexpected error!'})

if __name__ == '__main__':
  app.run(debug=True)
