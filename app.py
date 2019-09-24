from flask import Flask, render_template, request, flash
from flask_pymongo import MongoClient
from forms import ContactForm
from flask_mail import Message, Mail

mail = Mail()

app = Flask(__name__, template_folder="templates")
app.secret_key = '1a2b3c4d'
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'assistenza.preventech@gmail.com'
app.config["MAIL_PASSWORD"] = 'Progetto1'
app.config['MONGO_DBNAME'] = 'maps'

mail.init_app(app)

client = MongoClient("mongodb+srv://user:user@preventechdb-swyud.mongodb.net/test?retryWrites=true&w=majority")
db = client.maps


@app.route('/')
def fullmap():
    # carica i segnaposti
    markers = list()
    for i in db.coord.find({}, {"_id": 0}):
        markers.append(i)

    return render_template(
        'index.html',
        fullmap=fullmap,
        markers=markers
    )


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender=form.email.data, recipients=['assistenza.preventech@gmail.com'])
            msg.body = """
      From: %s &lt;%s&gt;
      %s
      """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('contact.html', success=True)

    elif request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run()
