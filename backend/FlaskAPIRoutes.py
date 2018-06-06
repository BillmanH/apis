import yaml
from flask import Blueprint, render_template,request
from wtforms import Form, TextField, validators
import os

import Azure_functions as az

adhocTestOne = Blueprint('adhocTestOne', __name__, template_folder='templates')
APIroutes = [adhocTestOne]

@adhocTestOne.route('/adhocTestOne')
def adhocktestroute():
	if "UserID" in request.cookies:
		if request.cookies["UserID"] == "testCookie":
			return "User Accepted" + str(os.getcwd())
		else: return (str(request.cookies))
	else:
		return "This user is not accepted"

