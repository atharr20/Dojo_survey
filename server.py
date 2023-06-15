from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def create_user():
    session['username']= request.form['username']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comment']= request.form['comment']
    return redirect('/display')

@app.route('/display')
def display():
    return render_template('display.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
