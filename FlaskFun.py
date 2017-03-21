from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def show_main_page():
    return render_template('index.html')

@app.route('/showSignUp')
def show_signup_page():
    return render_template('signUp.html')

@app.route('/signIn')
def show_signin_page():
    return render_template('signIn.html')

@app.route('/home')
def go_home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

