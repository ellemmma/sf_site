from flask import Flask, render_template, request

app = Flask(__name__) #привет, меня можно ревьювить :)
@app.route("/")
def go():
    filename = 'programm.csv'
    with open(filename, 'w') as file_object:
        file_object.write('name')
        file_object.write(',')
        file_object.write('email')
        file_object.write(',')
        file_object.write('answer')
        file_object.write("\n")
    return render_template("1.htm")
print("obnimashki")
@app.route('/answer', methods=['POST'])
def nn():
   name = request.form['name']
   email = request.form['email']
   answer = request.form['message']
   filename = 'programm.csv'
   with open(filename, 'a') as file_object:
       file_object.write(name)
       file_object.write(',')
       file_object.write(email)
       file_object.write(',')
       file_object.write(answer)
       file_object.write("\n")
   return render_template("1.htm")
@app.route('/index.html')
def index():
   return render_template('index.html')
if __name__ == '__main__':
     app.run(debug=True)
