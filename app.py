from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
	data = request.get_json()
	height = data['height']
	weight = data['weight']
	bmi = weight / (height ** 2)
	return jsonify({'bmi': round(bmi, 2)})

@app.route('/bmr', methods=['POST'])
def bmr():
	data = request.get_json()
	height = data['height']
	weight = data['weight']
	age = data['age']
	gender = data['gender']

	if gender == 'male':
		bmr = 88.362 + (13.997 * weight) + (4.799 * height) - (5.677 * age)
	elif  gender == 'female':
		bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

	return jsonify({'bmr': round(bmr, 2)})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
