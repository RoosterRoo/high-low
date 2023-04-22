from flask import Flask
import random

app = Flask(__name__)

low_url = 'https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif?cid=ecf05e47uyqvaq580779hh4zfymply6jm9i7zncpy63vtftd&rid=giphy.gif&ct=g'
high_url = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
correct_url = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'
home_url = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'

answer = random.randint(1, 100)


@app.route('/')
def guess():
    return f'<h1>Guess a number between 1-100 in the url</h1>' \
           f'<img src={home_url} />'


@app.route('/<int:number>')
def is_correct_guess(number):
    if number == answer:
        return f'<h1>You found the answer!!!</h1>' \
               f'<img src={correct_url} />'
    elif number > answer:
        return f'<h1>Too high, bro!!!</h1>' \
               f'<img src={high_url} />'
    else:
        return f'<h1>Too low, yo!!!</h1>' \
               f'<img src={low_url} />'


if __name__ == '__main__':
    app.run(debug=True)


