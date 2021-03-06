from flask import Flask, flash, render_template, request, redirect, url_for
from celery import Celery
from flask_mail import Mail, Message

flaskApp = Flask(__name__)
flaskApp.config.from_object("config")
flaskApp.config.update(
    broker_url=flaskApp.config['CELERY_RESULT_BACKEND'],
    result_backend=flaskApp.config['CELERY_BROKER_URL']
)


flaskApp.secret_key = flaskApp.config['SECRET_KEY']

# set up celery client
client = Celery(flaskApp.name, broker=flaskApp.config['CELERY_BROKER_URL'])
client.conf.update(flaskApp.config)

mail = Mail(flaskApp)

@client.task
def send_mail(data):
    """ Function to send emails in the background.
    """
    with flaskApp.app_context():
        msg = Message("Ping!",
                    sender="admin.ping",
                    recipients=[data['email']])
        msg.body = data['message']        
        mail.send(msg)


@flaskApp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        data = {}
        data['email'] = request.form['email']
        data['first_name'] = request.form['first_name']
        data['last_name'] = request.form['last_name']
        data['message'] = request.form['message']
        duration = int(request.form['duration'])
        duration_unit = request.form['duration_unit']

        # calculate time in seconds
        if duration_unit == 'minutes':
            duration *= 60
        elif duration_unit == 'hours':
            duration *= 3600
        elif duration_unit == 'days':
            duration *= 86400

        send_mail.apply_async(args=[data], countdown=duration)
        flash(f"Email will be sent to {data['email']} in {request.form['duration']} {duration_unit}")
        
        return redirect(url_for('index'))


if __name__ == '__main__':
    flaskApp.run(debug=False)
