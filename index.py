from flask import *
from flask_mail import Mail

app = Flask(__name__)
app.secret_key = 'ABC'


app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'sahilvanarse4@gmail.com',
    # MAIL_PASSWORD = 'gyebcqdjeeypscon',
    MAIL_PASSWORD = 'bbmqjrtckjbpwbog',
)
mail=Mail(app)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/about')
def about():
    return render_template('about1.html')

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method=='POST':
          name = request.form['name']
          email = request.form['email']
          message = request.form['message']
          mail.send_message('Received New Feedback !!!', 
                               sender=email,
                               recipients=['sahilvanarse4@gmail.com'],
                               body = name + "\n" +message + "\n"
                               )
    return render_template('contact1.html')

if __name__ == '__main__':
    app.run(debug=True)
