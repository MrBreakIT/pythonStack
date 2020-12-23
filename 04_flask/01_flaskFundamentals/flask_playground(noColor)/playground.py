from flask import Flask, render_template
app = Flask(__name__)


@app.route("/play/<int:number>/<color>")
def playboxes(number, color):
    return render_template("index.html", num=number, color=color)












if __name__ == "__main__":
    app.run(debug=True)
