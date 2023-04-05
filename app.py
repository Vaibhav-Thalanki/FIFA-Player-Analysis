import numpy as np
from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
mymodel = pickle.load(open("model.pkl", "rb"))  # load model
myscaler = pickle.load(open("scaler.pkl", "rb"))


@app.route('/')  # url binding
def loadhome():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])  # url binding
def user():

    # 'Aggression', 'Crossing', 'Curve', 'Dribbling', 'Finishing',
    #    'Free kick accuracy', 'Heading accuracy', 'Long shots', 'Penalties',
    #    'Shot power', 'Volleys', 'Short passing', 'Long passing',
    #    'Interceptions', 'Marking', 'Sliding tackle', 'Acceleration', 'Agility', 'Reactions','Sprint speed',
    #    'Positioning'
    
    Aggression = request.form["Aggression"]
    Crossing = request.form["Crossing"]
    Curve = request.form["Curve"]
    Dribbling = request.form["Dribbling"]
    Finishing = request.form["Finishing"]
    Freekickaccuracy = request.form["Freekickaccuracy"]
    Headingaccuracy = request.form["Headingaccuracy"]
    Longshots = request.form["Longshots"]
    Penalties = request.form["Penalties"]
    Shotpower = request.form["Shotpower"]
    Volleys = request.form["Volleys"]
    Shortpassing = request.form["Shortpassing"]
    Longpassing = request.form["Longpassing"]
    Interceptions = request.form["Interceptions"]
    Marking = request.form["Marking"]
    Slidingtackle = request.form["Slidingtackle"]
    Acceleration = request.form["Acceleration"]
    Agility = request.form["Agility"]
    Reactions = request.form["Reactions"]
    Sprintspeed = request.form["Sprintspeed"]
    Positioning = request.form["Positioning"]

    
    tobescaled = [[float(Aggression), float(Crossing), float(Curve), float(Dribbling), float(Finishing), float(
        Freekickaccuracy), float(Headingaccuracy), float(Longshots), float(Penalties), float(Shotpower), float(Volleys), float(Shortpassing), float(Longpassing), float(Interceptions), float(Marking), float(Slidingtackle), float(Acceleration), float(Agility), float(Reactions), float(Sprintspeed), float(Positioning)]]
    
    arrayofinputs = myscaler.transform(tobescaled)
    
    y = mymodel.predict(arrayofinputs)
    print(y)
    if str(y[0]) == '0':
        status = 'Defence Position'
    elif str(y[0]) == '1':
        status = 'Attack Position'
    return render_template("result.html", output="The prediction is that the player is of "+status)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
