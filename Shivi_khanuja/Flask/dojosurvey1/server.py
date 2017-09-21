from flask import Flask, render_template, redirect, session , request, flash

app = Flask (__name__)

app.secret_key = "secret"

def validate(form_data):
    errors = False

    if len(form_data['name']) == 0:
        flash("Name can not be blank")
        errors = True
    return errors


@app.route ('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    errors = validate(request.form)
    if errors:
        return redirect('/')
    else:
        session['survey'] = request.form
        return redirect('/result')

@app.route('/result')
def result():
    data = session['survey']

    return render_template('result.html', data=data)

app.run(debug=True)