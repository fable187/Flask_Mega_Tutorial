# finally, this is importing the entire app + routes by importing app from app
from app import app

if __name__ == '__main__':
    app.run(debug=True)