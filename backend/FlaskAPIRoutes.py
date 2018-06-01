import yaml
from flask import Blueprint, render_template,request
from wtforms import Form, TextField, validators
#import BOTO_BL as bbto

adhocTestOne = Blueprint('adhocTestOne', __name__, template_folder='templates')
APIroutes = [adhocTestOne]

@adhocTestOne.route('/adhocTestOne')
def adhocktestroute():
	c = request.args.get('c')
	t = request.args.get('t')
	return "The arguments are c:" + str(c) + " and t:" + str(t) 

