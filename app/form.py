from flask_wtf import Form
# from flask_wtf import FlaskForm 
from wtforms.fields.html5 import URLField
from wtforms.validators import url

class GetLinkForm(Form):
# class GetLinkForm(FlaskForm):	
    long_url = URLField(validators=[url()])