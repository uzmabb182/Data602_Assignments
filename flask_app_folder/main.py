
from flask import Flask, request, render_template

app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/calculate', methods=["GET", "POST"])
def calculate():

    if request.method == "POST":
        # getting input with name = number in HTML form
        num = int(request.form.get("number"))
        return "Mutiplication by 5 is: " + str(num * 5)

    return render_template('calculate.html')
    

@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
        # getting input with name = lname in HTML form
        last_name = request.form.get("lname")
        return "Your name is "+ first_name + last_name

    return render_template('login.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)