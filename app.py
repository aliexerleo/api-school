from flask import Flask, jsonify, request
from connection import create_connection
import query


app = Flask(__name__)


@app.route('/all-courses')
def all_courses():
	
	data = query.all_courses()
	if data:
		return jsonify({'message':data})
	else:
		return jsonify({'message':'Internal error'})


@app.route('/asignatures-sixth')
def asignatures_sixth():
	data = query.asignatures_sixth()
	if data:
		return jsonify({'message':data})
	else:
		return jsonify({'message':'Internal error'})


@app.route('/asignatures-seventh')
def asignatures_seventh():
	data = query.asignatures_seventh()
	if data:
		return jsonify({'message':data})
	else:
		return jsonify({'message':'Internal error'})



@app.route('/asignatures-eighth')
def asignatures_eighth():
	data = query.asignatures_eighth()
	if data:
		return jsonify({'message':data})
	else:
		return jsonify({'message':'Internal error'})


@app.route('/asignatures-ninth')
def asignatures_ninth():
	data = query.asignatures_ninth()
	if data:
		return jsonify({'message':data})
	else:
		return jsonify({'message':'Internal error'})



@app.route('/asignatures-tenth')
def asignatures_tenth():
	data = query.asignatures_tenth()
	if data:
		return jsonify({'message':data})
	else:
		return jsonify({'message':'Internal error'})


@app.route('/asignatures-eleventh')
def asignatures_eleventh():
	data = query.asignatures_eleventh()
	if data:
		return jsonify({'message':data})
	else:
		return jsonify({'message':'Internal error'})


@app.route('/courses')
def courses():
	#request_params = request.args.to_dict()
	#data = query.courses(request_params['id'])
	_id = request.args['id']
	data = query.courses(_id)
	if data:
		return jsonify({'message':data})
	else:
		return jsonify({'message':'Internal error'})





if __name__ == '__main__':
	app.run(debug=True)
