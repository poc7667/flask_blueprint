# -*- coding: utf8 -*-
from flask import Flask, Response, request, url_for

app = Flask(__name__)
VERSION = "1.0.0"

from sub_1 import sub_1_mod
app.register_blueprint(sub_1_mod, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8888)
