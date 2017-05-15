import os
from flask import Flask, request, render_template

app = Flask(__name__)

HOST_IP = os.environ['HOST_IP']

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def convert_xor():
    entered_text = request.form['text']

    # Start byte to compare with
    result = int('00', 16)

    # Empty result string
    result_string = ""

    for i, element in enumerate(entered_text.split()):
        # Start XOR comparation
        result = int(element, 16) ^ result
        # If first byte then start to fill the result string
        if i == 0:
            result_string = "0x" + element
        # Else: continue to fill the result string
        else:
            result_string = result_string + " + 0x" + element

    # Convert result string to hexdecimal view
    result = "%X" % result
    result = str(result).upper()
    result_string = result_string.upper() + " = "

    return render_template("index.html",
                           result_string=result_string,
                           result=result)


if __name__ == "__main__":
    app.run(host=HOST_IP,
            threaded=True)