from flask import Flask, render_template

app = Flask(__name__, template_folder='template')



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
