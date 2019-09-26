from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, TextField, validators, ValidationError
class ContactForm(Form):
#Di seguito viene indicato come è costruito il form che poi verra richiamato nel nostro HTML.
  name = TextField("Nome",  [validators.Required("Inserire il nome.")])
  email = TextField("Email",  [validators.Required("Inserire email."), validators.Email("Inserire email.")])
  message = TextAreaField("Nome + Indirizzo + Coordinate",  [validators.Required("Inserire indirizzo erogatore incluse coordinate.")])
  submit = SubmitField("Invia")