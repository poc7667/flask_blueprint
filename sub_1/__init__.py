# -*- coding: utf8 -*-
from flask import Blueprint

sub_1_mod = Blueprint('sub_1', __name__)

import sub_1.web
