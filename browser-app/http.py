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
    package = ""

    for i, hexbyte in enumerate(entered_text.split()):
        # Start XOR comparation
        result = int(hexbyte, 16) ^ result
        # If first byte then start to fill the result string
        if i == 0:
            package = "0x" + hexbyte
        # Else: continue to fill the result string
        else:
            package += " + 0x" + hexbyte.upper()

    if package:
        # Convert result string to hexdecimal view
        result = "0x{0:X}" .format(result)
        package += " = "
    else:
        package = "Enter something in the textbox"
        result = "No result"

    return render_template("index.html",
                           package=package,
                           result=result)


if __name__ == "__main__":
    app.run(host=HOST_IP,
            threaded=True)