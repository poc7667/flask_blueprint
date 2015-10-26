# -*- coding: utf8 -*-
from sub_1 import sub_1_mod

from flask import Flask, Response, request

app = Flask(__name__)

@app.route("/hihi", methods=['GET'])
def hihi():
    return make_response(["hihi"], VERSION)
