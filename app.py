# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Index route, Home page. List all routes that are available.
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to the 'Home' page. <br> The available routes are: \
        <br>/api/v1.0/precipitation\
        <br>/api/v1.0/stations\
        <br>/api/v1.0/tobs\
        <br>/api/v1.0/<start> and /api/v1.0/<start>/<end>\"


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)
