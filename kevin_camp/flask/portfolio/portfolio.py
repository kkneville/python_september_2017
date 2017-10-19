from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def portfolio():
	return render_template('index.html')

@app.route('/projects')
def projects():
	projects = ['Columbia', 'Hertz', 'Prana', 'Office Depot']
	return render_template('projects.html', projects=projects)

@app.route('/about')
def about():
	return render_template('about.html')

app.run(debug=True)
