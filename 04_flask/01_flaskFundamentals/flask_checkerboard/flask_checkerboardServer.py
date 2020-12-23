from flask import Flask, render_template
app = Flask(__name__)


@app.route("/checkers/<int:X>/<int:Y>")
def checkers(X,Y):
    num = X/2
    num2 = Y/2
    print("*****  in the method  *****")
    return render_template("checkerboard.html", X=int(num),Y=int(num2) )





























if __name__ == "__main__":   
    app.run(debug=True)    
