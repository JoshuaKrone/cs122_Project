# import the Flask class from the flask module
from flask import Flask

# import the render_template function
from flask import render_template

#Allows to request information from websites
from flask import request

# create a Flask object called app
app = Flask(__name__)

# define a route to the home page
# create a template_display function
@app.route("/")
@app.route("/home")
def Data_On_The_Field():
    # render the cs122.html script
    return render_template("Data_On_The_Field.html")

@app.route("/games")
def games():

    #Retrieve date put in by User
    game_date = request.arg.get("game_date")

    #Send selected date to the games template
    return render_template("games.html", game_date = game_date)

@app.route("/games_stats")
def games_stats():
    pass