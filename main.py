from waitress import serve
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def main():

    return render_template(template_name_or_list='home.html')


@app.route('/set-reminder')
def update():

    return render_template(template_name_or_list='reminder.html')


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8085)
