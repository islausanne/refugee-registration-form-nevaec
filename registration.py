from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    email = request.form['email']
    gender = request.form['gender']
    country_of_origin = request.form['country_of_origin']
    date_arrival = request.form['date_arrival']
    num_dependants = request.form['num_dependants']
    medical_conditions = request.form['medical_conditions']
    dietary_requirements = request.form['dietary_requirements']
    current_location = request.form['current_location']





if __name__ == '__main__':
    app.run(debug=True)