import re
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def convert_xor():
    text = request.form['text']
    list = re.split(' ', text)
    i = 0
    result = "00"
    result_string = ""
    while i < len(list):
        result = hex(int(list[i], 16) ^ int(result, 16))
        if i == 0:
            result_string = str(hex(int(list[i], 16)))
        else:
            result_string = result_string + " + " + str(hex(int(list[i], 16)))
        i += 1
    result = str(result)
    result_string = result_string.upper() + " = "
    return render_template("index.html",
                           result_string=result_string,
                           result=result)


if __name__ == "__main__":
    app.run(host="192.168.0.121",
            threaded=True)