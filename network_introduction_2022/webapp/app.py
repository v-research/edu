from flask import Flask, render_template, request, flash
#from os import urandom

app = Flask(__name__)

#app.secret_key = urandom(24).hex()

@app.route('/', methods=('GET', 'POST'))
def index():
	if request.method == 'POST':
		secret_message = request.form['secret_message']

		if not secret_message:
			flash('You must send a message!')
		else:
			print(secret_message)
	return render_template('index.html')

if __name__ == '__main__':
	#app.run(debug=True, host='0.0.0.0', ssl_context='adhoc', port=13800)
	app.run(debug=True, host='0.0.0.0', port=13800)
