from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('homepage.html', phrase = "hello", times=5)

@app.route('/success')
def success():
    return 'Screw You, go back to sleep!'

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/say/<name>')
def coding(name):
    print(name)
    return "Hello " + name

@app.route('/repeat/<wordToSay>/<int:numTimes>')
def repeat(wordToSay, numTimes):
    return wordToSay * numTimes







if __name__=="__main__":
    app.run(debug=True)
