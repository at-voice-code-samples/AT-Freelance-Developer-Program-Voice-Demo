import os
from flask import Flask, request, render_template
from flask_api import status

app = Flask(__name__)


def entry_phrase():
    response = '<?xml version="1.0"?>'
    response += '<Response>'
    response += '<GetDigits timeout="30" finishOnKey="#" callbackUrl="https://limitless-mountain-80043.herokuapp.com/voice/say">'
    response += '<Play url="http://197.248.0.197:8081/ad846fec309505710462e90a4b48bcb7.mp3">'
    response += '</Play>'
    response += '</GetDigits>'
    #response += '<Say>Hi, welcome to the Africas Talking Freelance Developer Program demo app. We have a little question for you. How old is Africas Talking? Dial in your guess and press hash</Say>'
    response += '</Response>'

    return response


def success_flow():
    response = '<?xml version="1.0"?>'
    response += '<Response>'
    response += '<Say voice="man">'
    response += 'Awesome! You got it right! Africas Talking has been around for almost a decade!'
    response += '</Say>'
    response += '</Response>'

    return response


def error_flow_too_high():
    response = '<?xml version="1.0"?>'
    response += '<Response>'
    response += '<Say voice="man">'
    response += 'Hi, sorry, thats not quite it. Guess a little lower. Call back to try again. Goodbye.'
    response += '</Say>'
    response += '</Response>'

    return response


def error_flow_too_low():
    response = '<?xml version="1.0"?>'
    response += '<Response>'
    response += '<Say voice="man">'
    response += 'Hi, sorry, thats not quite it. Guess a little higher. Call back to try again. Goodbye.'
    response += '</Say>'
    response += '</Response>'


def error_flow():
    response = '<?xml version="1.0"?>'
    response += '<Response>'
    response += '<Say voice="man">'
    response += 'Hi, sorry, thats not quite it. Something is wrong with the input you provided. Call back to try again. Goodbye.'
    response += '</Say>'
    response += '</Response>'


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return 'Everything is ok!', status.HTTP_200_OK
    elif request.method == "POST":
        return entry_phrase()
    else:
        return 'I think something is up', status.HTTP_400_BAD_REQUEST


@app.route('/voice/say', methods=["GET", "POST"])
def say_func():
    digits = request.values.get("dtmfDigits")
    print(digits)

    if digits == "9":
        return success_flow()
    elif digits > "9":
        return error_flow_too_high()
    elif digits < "9":
        return error_flow()
    else:
        return 'I think something is up', status.HTTP_400_BAD_REQUEST


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
