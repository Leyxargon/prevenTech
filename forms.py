from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, TextField, validators, ValidationError
class ContactForm(Form):
  name = TextField("Nome",  [validators.Required("Please enter your name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  subject = TextField("Indirizzo erogatore",  [validators.Required("Please enter a subject.")])
  message = TextAreaField("Indirizzo + Coordinate",  [validators.Required("Please enter a message.")])
  submit = SubmitField("Invia")