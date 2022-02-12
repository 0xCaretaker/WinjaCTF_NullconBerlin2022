from flask import Flask,redirect,render_template
app = Flask(__name__)

@app.route('/home/<user>')
def hello_user(user):
   if "__import__" in user:
      message = "Morty saved you again Rick!! No __import__ allowed for those Hackers."
      return render_template('index.html', message = message)
   if "import" in user:
      message = "Morty saved you again Rick!! No import allowed for those Hackers."
      return render_template('index.html', message = message)
   message = eval('"Hello '+user+'"')
   return render_template('index.html', message = message)

@app.route('/')
def nothing():
   return render_template('index.html')

@app.route('/home')
def homepage1():
   return redirect('/home/caretaker')

@app.route('/home/')
def homepage2():
   return redirect('/home/caretaker')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
