from flask import Flask, request, jsonify, json 

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
	data = request.data
	json_data = json.loads(data)
	string = json_data["string_to_cut"]
	cut = cut_string(string)
	return jsonify(
		return_string=cut 
	)

def cut_string(string):
	final_string = ""
	for i in range(2, len(string), 3):
		final_string += string[i]
	return final_string

if __name__ == "__main__":
	app.run()