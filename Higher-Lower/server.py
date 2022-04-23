from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>""<b>"'Guess a number between 0 and 9'"</b>""</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


random_number = randint(0, 9)
print(random_number)


@app.route('/<int:number>')
def get_number(number):

    if number > random_number:
        return '<h1>'"Too high,try again"'</h1>'\
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif number < random_number:
        return '<h1>'"Too low,try again"'</h1>'\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1>"'You Found Me!'"</h1>"\
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"



if __name__ == "__main__":
    app.run(debug=True)
