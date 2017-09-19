from flask import Flask, request, redirect, render_template, session, flash
app = Flask(__name__)
app.secret_key = 'secret_key'

# def registration_validation():
#     errors = []
#     if len(email < 5):
#         errors.append("invalid email")
#     elif len(first_name < 2):
#         errors.append('invalid first name')
#     elif len(last_name < 2):
#         errors.append('invalid last name')
#     elif len(password < 3):
#         errors.append('password must be longer than 3 characters')
#     elif len(last_name < 2):
#         errors.append('invalid last name')


@app.route("/")
def index():
    # registration_validation()
    return render_template("index.html")

@app.route('/registered', methods=["POST"])
def reg():
    session['user'] = request.form
    return redirect('/success')
    # return redirect('/')

@app.route("/success")
def success():
    data =
    return render_template("success.html", data=request.form)

app.run(debug=True)
