from flask import Flask, render_template
app = Flask(__name__)


#the request from the browser looks for a app.route that matches the request
@app.route("/")
def homePage():
    #the return gives the response
    return render_template("homepage.html")

@app.route("/nba")
def nbaPage():
    return "Place holder for the NBA page"


@app.route("/nba/teams")
def nbaTeams():
    teams = [
        {'id': 1, 'name': "Lakers", "city": "LA"},
        {'id': 2, 'name': "Clipper", "city": "LA"},
        {'id': 3, 'name': "Bulls", "city": "Chicago"},
        {'id': 4, 'name': "Wizards", "city": "DC"}
    ]
    return render_template("allTeams.html", theTeams= teams )


@app.route("/nba/teams/<teamName>")
def showTeam(teamName):
    return f"placeholder to show infor about team: {teamName}"

@app.route("/saysomething/<wordToSay>/<int:numTimes>")
def saySomething(wordToSay, numTimes):
    return wordToSay * numTimes






# @app.route("/nba/teams/cavs")

# @app.route("/nba/teams/lakers")

# @app.route("/nba/teams/wizards")
















if __name__ == "__main__":
    app.run(debug=True)



