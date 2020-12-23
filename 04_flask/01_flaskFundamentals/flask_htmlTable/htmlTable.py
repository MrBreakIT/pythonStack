from flask import Flask, render_template
app = Flask(__name__)




students = [
    {'fName' : 'Michael', 'lName' : 'Choi'},
    {'fName' : 'John', 'lName' : 'Supsupin'},
    {'fName' : 'Mark', 'lName' : 'Guillen'},
    {'fName' : 'KB', 'lName' : 'Tonel'},
    {'fName' : 'John', 'lName' : 'Pike'},
    {'fName' : 'TuPac', 'lName' : 'Shakur'},
    {'fName' : 'Ronald', 'lName' : 'McDonald'},
    {'fName' : 'Ayn', 'lName' : 'Rand'},
    {'fName' : 'Joe', 'lName' : 'Mama'},
    {'fName' : 'Dog', 'lName' : 'TheBountyHunter'},
    {'fName' : 'Bozo', 'lName' : 'TheClown'},
    {'fName' : '', 'lName' : ''},
    {'fName' : '', 'lName' : ''},
    {'fName' : '', 'lName' : ''},
    {'fName' : '', 'lName' : ''},
    {'fName' : '', 'lName' : ''},
    {'fName' : '', 'lName' : ''},
    {'fName' : '', 'lName' : ''},
    {'fName' : '', 'lName' : ''},

    ]
@app.route('/lists')
def render_lists():    
    return render_template('lists.html', First = 'fName' , Last =  'lName', Full = 'fName' + 'lName', students = students)












if __name__ == '__main__':   
    app.run(debug=True)    
