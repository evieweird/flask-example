from flask import Flask, render_template

application = Flask(__name__, template_folder='template')



@application.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html', 'database.html')